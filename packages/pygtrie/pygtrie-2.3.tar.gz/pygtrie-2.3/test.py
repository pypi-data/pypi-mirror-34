#!/usr/bin/python

"""trie module unit tests."""

__author__ = 'Michal Nazarewicz <mina86@mina86.com>'
__copyright__ = ('Copyright 2014-2017 Google LLC',
                 'Copyright 2018 Michal Nazarewicz <mina86@mina86.com>')


import array
import base64
import collections
import pickle
import sys
import unittest

import pygtrie


# pylint: disable=missing-docstring,invalid-slice-index

def _update_trie_factory(trie_cls, *args, **kw):
    t = trie_cls()
    t.update(*args, **kw)
    return t


def _setter_trie_factory(trie_cls, d):  # pylint: disable=invalid-name
    t = trie_cls()
    for k, v in d.items():
        t[k] = v
    return t


_TRIE_FACTORIES = ((
    'TrieFromNamedArgs',
    lambda trie_cls, d: trie_cls(**d)
), (
    'TrieFromTuples',
    lambda trie_cls, d: trie_cls(d.items())
), (
    'TrieFromDict',
    lambda trie_cls, d: trie_cls(d)
), (
    'TrieFromTrie',
    lambda trie_cls, d: trie_cls(trie_cls(d))
), (
    'CopyOfTrie',
    lambda trie_cls, d: trie_cls(d).copy()
), (
    'UpdateWithNamedArgs',
    lambda trie_cls, d: _update_trie_factory(trie_cls, **d)
), (
    'UpdateWithTuples',
    lambda trie_cls, d: _update_trie_factory(trie_cls, d.items())
), (
    'UpdateWithDict',
    _update_trie_factory
), (
    'Setters',
    _setter_trie_factory
))


class TrieTestCase(unittest.TestCase):
    # The below need to be overwritten by subclasses

    # A Trie class being tested
    _TRIE_CLS = pygtrie.Trie

    # A key to set
    _SHORT_KEY = 'foo'
    # Another key which has all but the last component equal to the ones in
    # _SHORT_KEY.
    _SHORT_KEY2 = 'foO'
    # Another key to set such that _SHORT_KEY is it's prefix
    _LONG_KEY = _SHORT_KEY + 'bar'
    # A key that is not set but _LONG_KEY is it's prefix
    _VERY_LONG_KEY = _LONG_KEY + 'baz'
    # A key that is not set and has no relation to other keys
    _OTHER_KEY = 'qux'
    # A list of prefixes of _SHORT_KEY
    _SHORT_PREFIXES = ('', 'f', 'fo')
    # A list of prefixes of _LONG_KEY which are not prefixes of _SHORT_KEY nor
    # _SHORT_KEY itself
    _LONG_PREFIXES = ('foob', 'fooba')

    @classmethod
    def path_from_key(cls, key):
        """Turns key into a path as used by Trie class being tested."""
        return key

    @classmethod
    def key_from_path(cls, path):
        """Turns path as used by Trie class being tested into a key."""
        return tuple(path)

    # End of stuff that needs to be overwritten by subclasses

    def __init__(self, *args, **kw):
        super(TrieTestCase, self).__init__(*args, **kw)
        # Python 2 compatibility.  Noisy code to confuse pylint so it does not
        # issue deprecated-method warning. pylint: disable=invalid-name
        for new, old in (('assertRegex', 'assertRegexpMatches'),
                         ('assertRaisesRegex', 'assertRaisesRegexp')):
            if not hasattr(self, new):
                setattr(self, new, getattr(self, old))

    def key_from_key(self, key):
        """Turns a key into a form that the Trie will return e.g. in keys()."""
        return self.key_from_path(self.path_from_key(key))

    # pylint: disable=invalid-name

    def assertNodeState(self, t, key, prefix=False, value=None):
        """Asserts a state of given node in a trie.

        Args:
            t: Trie to check the node in.
            key: A key for the node.
            prefix: Whether the node is a prefix of a longer key that is in the
              trie.
            value: If given, value associated with the key.  If missing, node
                has no value associated with it.
        Raises:
            AssertionError: If any assumption is not met.
        """
        if prefix:
            self.assertTrue(t.has_subtrie(key))
            self.assertTrue(bool(t.has_node(key) & pygtrie.Trie.HAS_SUBTRIE))
        else:
            self.assertFalse(t.has_subtrie(key))
            self.assertFalse(bool(t.has_node(key) & pygtrie.Trie.HAS_SUBTRIE))
        if value is None:
            o = object()
            self.assertNotIn(key, t)
            key_error_exception = pygtrie.ShortKeyError if prefix else KeyError
            self.assertRaises(key_error_exception, lambda: t[key])
            self.assertRaises(key_error_exception, t.pop, key)
            self.assertIsNone(t.get(key))
            self.assertIs(o, t.get(key, o))
            self.assertIs(o, t.pop(key, o))
            self.assertFalse(t.has_key(key))
            self.assertNotIn(self.key_from_key(key), list(t.iterkeys()))
            self.assertNotIn(self.key_from_key(key), t.keys())
            self.assertEqual(pygtrie.Trie.HAS_SUBTRIE if prefix else 0,
                             t.has_node(key))
        else:
            self.assertIn(key, t)
            self.assertEqual(value, t[key])
            self.assertEqual(value, t.get(key))
            self.assertEqual(value, t.get(key, object()))
            self.assertTrue(t.has_key(key))
            self.assertTrue(bool(t.has_node(key) & pygtrie.Trie.HAS_VALUE))
            self.assertIn(self.key_from_key(key), list(t.iterkeys()))
            self.assertIn(self.key_from_key(key), t.keys())

    def assertFullTrie(self, t, value=42):
        """Asserts a trie has _SHORT_KEY and _LONG_KEY set to value."""
        self.assertEqual(2, len(t))
        for prefix in self._SHORT_PREFIXES + self._LONG_PREFIXES:
            self.assertNodeState(t, prefix, prefix=True)
        self.assertNodeState(t, self._SHORT_KEY, prefix=True, value=value)
        self.assertNodeState(t, self._LONG_KEY, value=value)
        self.assertNodeState(t, self._VERY_LONG_KEY)
        self.assertNodeState(t, self._OTHER_KEY)

    def assertShortTrie(self, t, value=42):
        """Asserts a trie has only _SHORT_KEY set to value."""
        self.assertEqual(1, len(t))
        for prefix in self._SHORT_PREFIXES:
            self.assertNodeState(t, prefix, prefix=True)
        for key in self._LONG_PREFIXES + (
                self._LONG_KEY, self._VERY_LONG_KEY, self._OTHER_KEY):
            self.assertNodeState(t, key)
        self.assertNodeState(t, self._SHORT_KEY, value=value)

        self.assertRegex(str(t), r'Trie\([^:]*: [^:]*\)')
        self.assertRegex(repr(t), r'Trie\(\(\(.*, .*\),\)\)')

    def assertEmptyTrie(self, t):
        """Asserts a trie is empty."""
        self.assertEqual(0, len(t), '%r should be empty: %d' % (t, len(t)))

        for key in self._SHORT_PREFIXES + self._LONG_PREFIXES + (
                self._SHORT_KEY, self._LONG_KEY, self._VERY_LONG_KEY,
                self._OTHER_KEY):
            self.assertNodeState(t, key)

        self.assertRaises(KeyError, t.popitem)

        self.assertEqual('Trie()', str(t))
        self.assertEqual('Trie()', repr(t))

    def _do_test_basics(self, trie_factory):
        """Basic trie tests."""
        d = dict.fromkeys((self._SHORT_KEY, self._LONG_KEY), 42)
        t = trie_factory(self._TRIE_CLS, d)

        self.assertFullTrie(t)

        self.assertEqual(42, t.pop(self._LONG_KEY))
        self.assertShortTrie(t)

        self.assertEqual(42, t.setdefault(self._SHORT_KEY, 24))
        self.assertShortTrie(t)

        t[self._SHORT_KEY] = 24
        self.assertShortTrie(t, 24)

        self.assertEqual(24, t.setdefault(self._LONG_KEY, 24))
        self.assertFullTrie(t, 24)

        del t[self._LONG_KEY]
        self.assertShortTrie(t, 24)

        self.assertEqual((self.key_from_key(self._SHORT_KEY), 24), t.popitem())
        self.assertEmptyTrie(t)

        t[self._LONG_KEY] = '42'
        self.assertRaisesRegex(pygtrie.ShortKeyError, str(self._SHORT_KEY),
                               t.__delitem__, self._SHORT_KEY)

    def _do_test_invalid_arguments(self, trie_factory):
        """Test various methods check for invalid arguments."""
        d = dict.fromkeys((self._SHORT_KEY, self._LONG_KEY), 42)
        t = trie_factory(self._TRIE_CLS, d)

        self.assertRaisesRegex(
            ValueError, 'update.. takes at most one positional argument,',
            t.update, (self._LONG_KEY, 42), (self._VERY_LONG_KEY, 42))

        self.assertRaisesRegex(TypeError, r'slice\(.*, None\)',
                               lambda: t[self._SHORT_KEY:self._LONG_KEY])
        self.assertRaisesRegex(TypeError, r"slice\(.*, 'foo'\)",
                               lambda: t[self._SHORT_KEY:self._LONG_KEY:'foo'])
    def _do_test_clear(self, trie_factory):
        """Test clear method."""
        d = dict.fromkeys((self._SHORT_KEY, self._LONG_KEY), 42)
        t = trie_factory(self._TRIE_CLS, d)
        self.assertFullTrie(t)
        t.clear()
        self.assertEmptyTrie(t)

    def _do_test_iterator(self, trie_factory):
        """Trie iterator tests."""
        d = dict.fromkeys((self._SHORT_KEY, self._LONG_KEY), 42)
        t = trie_factory(self._TRIE_CLS, d)

        self.assertEqual([42, 42], t.values())
        self.assertEqual([42, 42], list(t.itervalues()))

        short_key = self.key_from_key(self._SHORT_KEY)
        long_key = self.key_from_key(self._LONG_KEY)

        expected_items = [(short_key, 42), (long_key, 42)]
        self.assertEqual(expected_items, t.items())
        self.assertEqual(expected_items, list(t.iteritems()))

        self.assertEqual([short_key, long_key], list(t))
        self.assertEqual([short_key, long_key], t.keys())
        self.assertEqual([short_key, long_key], list(t.iterkeys()))

    def _do_test_subtrie_iterator(self, trie_factory):
        """Subtrie iterator tests."""
        d = dict.fromkeys((self._SHORT_KEY, self._LONG_KEY), 42)
        t = trie_factory(self._TRIE_CLS, d)

        long_key = self.key_from_key(self._LONG_KEY)
        prefix = self._LONG_PREFIXES[0]

        self.assertEqual([42, 42], t.values(prefix=self._SHORT_KEY))
        self.assertEqual([42, 42], list(t.itervalues(prefix=self._SHORT_KEY)))
        self.assertEqual([42], t.values(prefix=prefix))
        self.assertEqual([42], list(t.itervalues(prefix=prefix)))

        expected_items = [(long_key, 42)]
        self.assertEqual(expected_items, t.items(prefix=prefix))
        self.assertEqual(expected_items, list(t.iteritems(prefix=prefix)))

        self.assertEqual([long_key], t.keys(prefix=prefix))
        self.assertEqual([long_key], list(t.iterkeys(prefix=prefix)))

    def _do_test_shallow_iterator(self, trie_factory):
        """Shallow iterator test."""
        d = dict.fromkeys((self._SHORT_KEY, self._LONG_KEY), 42)
        t = trie_factory(self._TRIE_CLS, d)

        self.assertEqual([42], t.values(shallow=True))
        self.assertEqual([42], list(t.itervalues(shallow=True)))

        short_key = self.key_from_key(self._SHORT_KEY)

        expected_items = [(short_key, 42)]
        self.assertEqual(expected_items, t.items(shallow=True))
        self.assertEqual(expected_items, list(t.iteritems(shallow=True)))

        self.assertEqual([short_key], t.keys(shallow=True))
        self.assertEqual([short_key], list(t.iterkeys(shallow=True)))

    def _do_test_splice_operations(self, trie_factory):
        """Splice trie operations tests."""
        d = dict.fromkeys((self._SHORT_KEY, self._LONG_KEY), 42)
        t = trie_factory(self._TRIE_CLS, d)

        self.assertEqual([42, 42], list(t[self._SHORT_KEY:]))
        self.assertEqual([42], list(t[self._LONG_PREFIXES[0]:]))

        t[self._SHORT_KEY:] = 24
        self.assertShortTrie(t, 24)

        self.assertEqual([24], list(t[self._SHORT_KEY:]))
        self.assertRaises(KeyError, lambda: list(t[self._LONG_PREFIXES[0]:]))

        t[self._LONG_KEY:] = 24
        self.assertFullTrie(t, 24)

        del t[self._SHORT_KEY:]
        self.assertEmptyTrie(t)

    def _do_test_find_one_prefix(self, trie_factory):
        """Shortest and longest prefix finding methods test."""
        d = dict.fromkeys((self._SHORT_KEY, self._LONG_KEY), 42)
        t = trie_factory(self._TRIE_CLS, d)

        short_pair = (self.key_from_key(self._SHORT_KEY), 42)
        long_pair = (self.key_from_key(self._LONG_KEY), 42)
        none_pair = (None, None)

        def assert_pair(expected, got):
            self.assertEqual(expected, tuple(got))
            self.assertEqual(expected[0], got.key)
            self.assertEqual(expected[1], got.value)
            if expected[0]:
                self.assertTrue(got)
            else:
                self.assertFalse(got)
                self.assertFalse(got.is_set)
                self.assertFalse(got.has_subtrie)
                self.assertIsNone(got.get())

        assert_pair(short_pair, t.shortest_prefix(self._VERY_LONG_KEY))
        assert_pair(short_pair, t.shortest_prefix(self._LONG_KEY))
        assert_pair(short_pair, t.shortest_prefix(self._VERY_LONG_KEY))
        assert_pair(short_pair, t.shortest_prefix(self._LONG_PREFIXES[-1]))
        assert_pair(short_pair, t.shortest_prefix(self._SHORT_KEY))
        assert_pair(none_pair, t.shortest_prefix(self._SHORT_PREFIXES[-1]))
        assert_pair(none_pair, t.shortest_prefix(self._OTHER_KEY))

        assert_pair(long_pair, t.longest_prefix(self._VERY_LONG_KEY))
        assert_pair(long_pair, t.longest_prefix(self._LONG_KEY))
        assert_pair(long_pair, t.longest_prefix(self._VERY_LONG_KEY))
        assert_pair(short_pair, t.longest_prefix(self._LONG_PREFIXES[-1]))
        assert_pair(short_pair, t.longest_prefix(self._SHORT_KEY))
        assert_pair(none_pair, t.longest_prefix(self._SHORT_PREFIXES[-1]))
        assert_pair(none_pair, t.longest_prefix(self._OTHER_KEY))

    def _do_test_list_prefixes(self, trie_factory):
        """Key prefixes listing method test."""
        d = dict.fromkeys((self._SHORT_KEY, self._LONG_KEY), 42)
        t = trie_factory(self._TRIE_CLS, d)

        short_pair = (self.key_from_key(self._SHORT_KEY), 42)
        long_pair = (self.key_from_key(self._LONG_KEY), 42)

        def assert_prefixes(expected, *args):
            got = list(t.prefixes(*args))
            self.assertEqual(expected, [tuple(step) for step in got])
            for e, g in zip(expected, got):
                self.assertTrue(g)
                self.assertEqual(e[0], g.key)
                self.assertEqual(e[1], g.value)

        assert_prefixes([], self._SHORT_PREFIXES[-1])
        assert_prefixes([], self._OTHER_KEY)
        assert_prefixes([short_pair], self._SHORT_KEY)
        assert_prefixes([short_pair], self._LONG_PREFIXES[-1])
        assert_prefixes([short_pair, long_pair], self._LONG_KEY)
        assert_prefixes([short_pair, long_pair], self._VERY_LONG_KEY)

    def _do_test_walk_towards(self, trie_factory):
        """walk_towards method test."""
        d = dict.fromkeys((self._SHORT_KEY, self._LONG_KEY), 42)
        t = trie_factory(self._TRIE_CLS, d)

        def assert_step(step):
            self.assertTrue(step)
            self.assertEqual(step[0], step.key)

            is_set = step.key in (self.key_from_key(self._SHORT_KEY),
                                  self.key_from_key(self._LONG_KEY))
            self.assertEqual(is_set, step.is_set)
            self.assertEqual(step.key != self.key_from_key(self._LONG_KEY),
                             step.has_subtrie)

            if is_set:
                self.assertEqual(42, step.value)
                self.assertEqual(42, step[1])
                self.assertEqual(42, step.get('42'))
                self.assertEqual(42, step.setdefault('42'))
                self.assertEqual(42, step.value)
                step.set('42')
                self.assertEqual('42', step.value)
                step.set(42)
            else:
                self.assertRaises(KeyError, lambda: step.value)
                self.assertRaises(KeyError, lambda: step[1])
                self.assertEqual('42', step.get('42'))
                self.assertEqual(42, step.setdefault(42))
                self.assertEqual(42, step.value)
                # pylint: disable=protected-access
                step._node.value = pygtrie._SENTINEL

        def assert_steps(key, raises=False):
            try:
                n = 0
                for step in t.walk_towards(key):
                    assert_step(step)
                    n += 1
                self.assertFalse(raises)
                self.assertEqual(len(self.path_from_key(key)) + 1, n)
            except KeyError:
                self.assertTrue(raises)

        assert_steps(self._SHORT_PREFIXES[-1])
        assert_steps(self._OTHER_KEY[-1], raises=True)
        assert_steps(self._SHORT_KEY)
        assert_steps(self._LONG_PREFIXES[-1])
        assert_steps(self._LONG_KEY)
        assert_steps(self._VERY_LONG_KEY, raises=True)

    def _do_test_pickle(self, trie_factory):
        """https://github.com/google/pygtrie/issues/7"""
        d = dict.fromkeys((self._SHORT_KEY, self._LONG_KEY, self._VERY_LONG_KEY,
                           self._OTHER_KEY), 42)
        t = trie_factory(self._TRIE_CLS, d)

        pickled = pickle.dumps(t)
        u = pickle.loads(pickled)

        self.assertEqual(t, u)

    def test_prefix_set(self):
        """PrefixSet test."""
        ps = pygtrie.PrefixSet(factory=self._TRIE_CLS)

        short_key = self.key_from_key(self._SHORT_KEY)
        long_key = self.key_from_key(self._LONG_KEY)
        very_long_key = self.key_from_key(self._VERY_LONG_KEY)
        other_key = self.key_from_key(self._OTHER_KEY)

        for key in (self._LONG_KEY, self._VERY_LONG_KEY):
            ps.add(key)
            self.assertEqual(1, len(ps))
            self.assertEqual([long_key], list(ps.iter()))
            self.assertEqual([long_key], list(iter(ps)))
            self.assertEqual([long_key], list(ps.iter(self._SHORT_KEY)))
            self.assertEqual([long_key], list(ps.iter(self._LONG_KEY)))
            self.assertEqual([very_long_key],
                             list(ps.iter(self._VERY_LONG_KEY)))
            self.assertEqual([], list(ps.iter(self._OTHER_KEY)))

        ps.add(self._SHORT_KEY)

        def check_state(p):
            self.assertTrue(ps)
            self.assertEqual(1, len(p))
            self.assertEqual([short_key], list(p.iter()))
            self.assertEqual([short_key], list(iter(p)))
            self.assertEqual([short_key], list(p.iter(self._SHORT_KEY)))
            self.assertEqual([long_key], list(p.iter(self._LONG_KEY)))
            self.assertEqual([], list(p.iter(self._OTHER_KEY)))

        check_state(ps)
        ps_copy = ps.copy()
        check_state(ps_copy)
        self.assertEqual(ps, ps_copy)

        ps.add(self._OTHER_KEY)
        self.assertEqual(2, len(ps))
        self.assertEqual(sorted((short_key, other_key)), sorted(ps.iter()))
        self.assertEqual([short_key], list(ps.iter(self._SHORT_KEY)))
        self.assertEqual([long_key], list(ps.iter(self._LONG_KEY)))
        self.assertEqual([other_key], list(ps.iter(self._OTHER_KEY)))

        check_state(ps_copy)
        self.assertNotEqual(ps, ps_copy)

        ps.clear()
        self.assertFalse(ps)
        self.assertEqual(0, len(ps))
        self.assertEqual([], list(ps))

    def test_equality(self):
        """Tests equality comparison."""
        a = self._TRIE_CLS({self._SHORT_KEY: 42})
        b = self._TRIE_CLS({self._SHORT_KEY: 42})
        c = self._TRIE_CLS({self._SHORT_KEY: '42'})
        d = self._TRIE_CLS({self._SHORT_KEY2: 42})

        self.assertEqual(a, a)
        self.assertEqual(a, b)
        self.assertNotEqual(a, c)
        self.assertNotEqual(a, d)

    _PICKLED_PROTO_0 = (
        'Y2NvcHlfcmVnCl9yZWNvbnN0cnVjdG9yCnAwCihjcHlndHJpZQpUcmllCnAxCmNfX2J1aW'
        'x0aW5fXwpvYmplY3QKcDIKTnRwMwpScDQKKGRwNQpWX3Jvb3QKcDYKZzAKKGNweWd0cmll'
        'Cl9Ob2RlCnA3CmcyCk50cDgKUnA5CihscDEwCkwzTAphVmYKcDExCmFWbwpwMTIKYWcxMg'
        'phTDQyTAphTC0zTAphTDNMCmFWYgpwMTMKYVZhCnAxNAphVnIKcDE1CmFMNDJMCmFMLTFM'
        'CmFMMUwKYVZ6CnAxNgphTDQyTAphYnNWX3NvcnRlZApwMTcKSTAwCnNiLg==')

    _PICKLED_PROTO_3 = (
        'gANjcHlndHJpZQpUcmllCnEAKYFxAX1xAihYBQAAAF9yb290cQNjcHlndHJpZQpfTm9kZQ'
        'pxBCmBcQVdcQYoSwNYAQAAAGZxB1gBAAAAb3EIaAhLKkr9////SwNYAQAAAGJxCVgBAAAA'
        'YXEKWAEAAABycQtLKkr/////SwFYAQAAAHpxDEsqZWJYBwAAAF9zb3J0ZWRxDYl1Yi4=')

    def assertUnpickling(self, want, pickled):
        got = pickle.loads(base64.b64decode(pickled))
        self.assertEqual(want, got)

    def test_pickling_proto0(self):
        want = self._TRIE_CLS.fromkeys(('foo', 'bar', 'baz'), 42)
        self.assertUnpickling(want, self._PICKLED_PROTO_0)

    @unittest.skipIf(sys.version_info[0] < 3, "Protocol 3 requires Python 3+")
    def test_pickling_proto3(self):
        want = self._TRIE_CLS.fromkeys(('foo', 'bar', 'baz'), 42)
        self.assertUnpickling(want, self._PICKLED_PROTO_3)


def _construct_trie_test_cases():

    def make_test_method(method, factory):
        return lambda self: method(self, trie_factory=factory)

    for name in list(TrieTestCase.__dict__):
        if not name.startswith('_do_test_'):
            continue
        orig = getattr(TrieTestCase, name)
        for factory_name, factory in _TRIE_FACTORIES:
            method = make_test_method(orig, factory)
            method.__doc__ = '%s using %s trie factory.' % (
                orig.__doc__[:-2], factory_name)
            setattr(TrieTestCase, '%s_%s' % (name[4:], factory_name), method)

_construct_trie_test_cases()


class CharTrieTestCase(TrieTestCase):
    _TRIE_CLS = pygtrie.CharTrie

    _PICKLED_PROTO_0 = (
        'Y2NvcHlfcmVnCl9yZWNvbnN0cnVjdG9yCnAwCihjcHlndHJpZQpDaGFyVHJpZQpwMQpjX1'
        '9idWlsdGluX18Kb2JqZWN0CnAyCk50cDMKUnA0CihkcDUKVl9yb290CnA2CmcwCihjcHln'
        'dHJpZQpfTm9kZQpwNwpnMgpOdHA4ClJwOQoobHAxMApMM0wKYVZmCnAxMQphVm8KcDEyCm'
        'FnMTIKYUw0MkwKYUwtM0wKYUwzTAphVmIKcDEzCmFWYQpwMTQKYVZyCnAxNQphTDQyTAph'
        'TC0xTAphTDFMCmFWegpwMTYKYUw0MkwKYWJzVl9zb3J0ZWQKcDE3CkkwMApzYi4=')

    _PICKLED_PROTO_3 = (
        'gANjcHlndHJpZQpDaGFyVHJpZQpxACmBcQF9cQIoWAUAAABfcm9vdHEDY3B5Z3RyaWUKX0'
        '5vZGUKcQQpgXEFXXEGKEsDWAEAAABmcQdYAQAAAG9xCGgISypK/f///0sDWAEAAABicQlY'
        'AQAAAGFxClgBAAAAcnELSypK/////0sBWAEAAAB6cQxLKmViWAcAAABfc29ydGVkcQ2JdW'
        'Iu')

    @classmethod
    def key_from_path(cls, path):
        return ''.join(path)

    def test_prefix_set_pickling_proto0(self):
        pickled = (
            'Y2NvcHlfcmVnCl9yZWNvbnN0cnVjdG9yCnAwCihjcHlndHJpZQpQcmVmaXhTZXQKcD'
            'EKY19fYnVpbHRpbl9fCm9iamVjdApwMgpOdHAzClJwNAooZHA1ClZfdHJpZQpwNgpn'
            'MAooY3B5Z3RyaWUKQ2hhclRyaWUKcDcKZzIKTnRwOApScDkKKGRwMTAKVl9yb290Cn'
            'AxMQpnMAooY3B5Z3RyaWUKX05vZGUKcDEyCmcyCk50cDEzClJwMTQKKGxwMTUKTDNM'
            'CmFWZgpwMTYKYVZvCnAxNwphZzE3CmFJMDEKYUwtM0wKYUwzTAphVmIKcDE4CmFWYQ'
            'pwMTkKYVZyCnAyMAphSTAxCmFMLTFMCmFMMUwKYVZ6CnAyMQphSTAxCmFic1Zfc29y'
            'dGVkCnAyMgpJMDAKc2JzYi4=')
        want = pygtrie.PrefixSet(('foo', 'bar', 'baz'),
                                 factory=pygtrie.CharTrie)
        self.assertUnpickling(want, pickled)

    @unittest.skipIf(sys.version_info[0] < 3, "Protocol 3 requires Python 3+")
    def test_prefix_set_pickling_proto3(self):
        pickled = (
            'gANjcHlndHJpZQpQcmVmaXhTZXQKcQApgXEBfXECWAUAAABfdHJpZXEDY3B5Z3RyaW'
            'UKQ2hhclRyaWUKcQQpgXEFfXEGKFgFAAAAX3Jvb3RxB2NweWd0cmllCl9Ob2RlCnEI'
            'KYFxCV1xCihLA1gBAAAAZnELWAEAAABvcQxoDIhK/f///0sDWAEAAABicQ1YAQAAAG'
            'FxDlgBAAAAcnEPiEr/////SwFYAQAAAHpxEIhlYlgHAAAAX3NvcnRlZHERiXVic2Iu'
        )
        want = pygtrie.PrefixSet(('foo', 'bar', 'baz'),
                                 factory=pygtrie.CharTrie)
        self.assertUnpickling(want, pickled)


class StringTrieTestCase(TrieTestCase):
    _TRIE_CLS = pygtrie.StringTrie

    _SHORT_KEY = '/home/foo'
    _SHORT_KEY2 = '/home/FOO'
    _LONG_KEY = _SHORT_KEY + '/bar/baz'
    _VERY_LONG_KEY = _LONG_KEY + '/qux'
    _OTHER_KEY = '/hom'
    _SHORT_PREFIXES = ('', '/home')
    _LONG_PREFIXES = ('/home/foo/bar',)

    _PICKLED_PROTO_0 = (
        'Y2NvcHlfcmVnCl9yZWNvbnN0cnVjdG9yCnAwCihjcHlndHJpZQpTdHJpbmdUcmllCnAxCm'
        'NfX2J1aWx0aW5fXwpvYmplY3QKcDIKTnRwMwpScDQKKGRwNQpWX3NlcGFyYXRvcgpwNgpW'
        'LwpwNwpzVl9yb290CnA4CmcwCihjcHlndHJpZQpfTm9kZQpwOQpnMgpOdHAxMApScDExCi'
        'hscDEyCkwxTAphVmZvbwpwMTMKYUw0MkwKYUwtMUwKYUwxTAphVmJhcgpwMTQKYUw0MkwK'
        'YUwtMUwKYUwxTAphVmJhegpwMTUKYUw0MkwKYWJzVl9zb3J0ZWQKcDE2CkkwMApzYi4=')

    _PICKLED_PROTO_3 = (
        'gANjcHlndHJpZQpTdHJpbmdUcmllCnEAKYFxAX1xAihYCgAAAF9zZXBhcmF0b3JxA1gBAA'
        'AAL3EEWAUAAABfcm9vdHEFY3B5Z3RyaWUKX05vZGUKcQYpgXEHXXEIKEsBWAMAAABmb29x'
        'CUsqSv////9LAVgDAAAAYmFycQpLKkr/////SwFYAwAAAGJhenELSyplYlgHAAAAX3Nvcn'
        'RlZHEMiXViLg==')

    @classmethod
    def path_from_key(cls, key):
        return key.split('/')

    @classmethod
    def key_from_path(cls, path):
        return '/'.join(path)

    def test_valid_separator(self):
        t = pygtrie.StringTrie()
        t['foo/bar'] = 42
        self.assertTrue(bool(t.has_node('foo') & pygtrie.Trie.HAS_SUBTRIE))

        t = pygtrie.StringTrie(separator='.')
        t['foo.bar'] = 42
        self.assertTrue(bool(t.has_node('foo') & pygtrie.Trie.HAS_SUBTRIE))

    def test_invalid_separator(self):
        self.assertRaises(TypeError, pygtrie.StringTrie, separator=42)
        self.assertRaises(ValueError, pygtrie.StringTrie, separator='')


class SortTest(unittest.TestCase):

    def test_enable_sorting(self):
        keys = sorted(chr(x) for x in range(32, 128) if x != ord('/'))
        # In Python 3 keys are returned in insertion order so we reverse the
        # insertion here.
        t = pygtrie.StringTrie.fromkeys(reversed(keys))

        # Unless dict's hash function is weird, trie's keys should not be
        # returned in order.
        self.assertNotEqual(keys, t.keys())
        self.assertEqual(keys, sorted(t.keys()))

        t.enable_sorting()
        self.assertEqual(keys, t.keys())

        t.enable_sorting(False)
        self.assertNotEqual(keys, t.keys())


class TraverseTest(unittest.TestCase):
    _SENTINEL = object()
    _TestNode = collections.namedtuple('TestNode', 'key children value')

    @classmethod
    def _make_test_node(cls, path_conv, path, children, value=_SENTINEL):
        return cls._TestNode(path_conv(path), sorted(children), value)

    def assertNode(self, node, key, children=0, value=_SENTINEL):  # pylint: disable=invalid-name
        self.assertTrue(node)
        self.assertEqual(key, node.key)
        self.assertEqual(children, len(node.children))
        self.assertEqual(value, node.value)
        return node

    def test_traverse_empty_tree(self):
        t = pygtrie.CharTrie()
        r = t.traverse(self._make_test_node)
        self.assertNode(r, '', 0)

    def test_traverse_singleton_tree(self):
        t = pygtrie.CharTrie()
        t.update({'a': 10})

        r = t.traverse(self._make_test_node)
        self.assertNode(r, '', 1)
        self.assertNode(r.children[0], 'a', 0, 10)

    def test_traverse(self):
        t = pygtrie.CharTrie()
        t.update({'aaa': 1, 'aab': 2, 'aac': 3, 'bb': 4})

        r = t.traverse(self._make_test_node)
        # Result:
        #  <>
        #    a
        #      aa
        #        aaa:1
        #        aab:2
        #        aac:3
        #    b
        #      bb:4
        self.assertNode(r, '', 2)

        # For some reason pylint thinks a_node et al. are strings.
        # pylint: disable=no-member

        a_node = self.assertNode(r.children[0], 'a', 1)
        aa_node = self.assertNode(a_node.children[0], 'aa', 3)
        self.assertNode(aa_node.children[0], 'aaa', 0, 1)
        self.assertNode(aa_node.children[2], 'aac', 0, 3)

        b_node = self.assertNode(r.children[1], 'b', 1)
        self.assertNode(b_node.children[0], 'bb', 0, 4)

    def test_traverse_compressing(self):
        t = pygtrie.CharTrie()
        t.update({'aaa': 1, 'aab': 2, 'aac': 3, 'bb': 4})

        def make(path_conv, path, children, value=self._SENTINEL):
            children = sorted(children)
            if value is self._SENTINEL and len(children) == 1:
                # There is only one prefix.
                return children[0]
            else:
                return self._TestNode(path_conv(path), children, value)

        r = t.traverse(make)
        # Result:
        # <>
        #  aa
        #    aaa:1
        #    aab:2
        #    aac:3
        #  bb:4
        self.assertNode(r, '', 2)

        # For some reason pylint thinks a_node et al. are strings.
        # pylint: disable=no-member

        aa_node = self.assertNode(r.children[0], 'aa', 3)
        self.assertNode(aa_node.children[0], 'aaa', 0, 1)
        self.assertNode(aa_node.children[1], 'aab', 0, 2)
        self.assertNode(aa_node.children[2], 'aac', 0, 3)

        self.assertNode(r.children[1], 'bb', 0, 4)

    def test_traverse_ignore_subtrie(self):
        t = pygtrie.CharTrie()
        t.update({'aaa': 1, 'aab': 2, 'aac': 3, 'b': 4})

        cnt = [0]

        def make(path_conv, path, children, value=self._SENTINEL):
            cnt[0] += 1
            if path and path[0] == 'a':
                return None
            else:
                children = [ch for ch in children if ch is not None]
                return self._TestNode(path_conv(path), children, value)

        r = t.traverse(make)
        # Result:
        # <>
        #  b:4
        self.assertNode(r, '', 1)
        self.assertNode(r.children[0], 'b', 0, 4)
        self.assertEqual(3, cnt[0])


class RecursionTest(unittest.TestCase):
    """Test for deep recursion.

    https://github.com/google/pygtrie/issues/8
    """

    @staticmethod
    def create_trie():
        tostring = (getattr(array.array, 'tobytes', None) or # Python 3
                    getattr(array.array, 'tostring'))  # Python 3

        trie = pygtrie.Trie()
        for x in range(100):
            y = tostring(array.array('h', range(x, 1000)))
            trie.update([(y, x)])
        return trie

    def test_iterator(self):
        for _ in self.create_trie().iteritems():
            pass

    def test_copy(self):
        self.create_trie().copy()

    # This code is taken from traverse docstring
    @classmethod
    def _undirected_graph_from_trie(cls, trie):
        """Converts trie into a graph and returns its nodes."""
        Node = collections.namedtuple('Node', 'label neighbours')  # pylint: disable=invalid-name

        class Builder(object):
            def __init__(self, path_conv, path, children, _=None):
                self.node = Node(path_conv(path), [])
                self.children = children
                self.parent = None

            def build(self, queue):
                for builder in self.children:
                    builder.parent = self.node
                    queue.append(builder)
                if self.parent:
                    self.parent.neighbours.append(self.node)
                    self.node.neighbours.append(self.parent)
                return self.node

        nodes = [trie.traverse(Builder)]
        i = 0
        while i < len(nodes):
            nodes[i] = nodes[i].build(nodes)
            i += 1
        return nodes

    def test_traverse_small(self):
        """Test code that is shown in traverse's docstring; test correctness."""
        t = pygtrie.StringTrie()
        t['foo/bar/baz'] = True
        t['foo/qux/baz'] = True
        t['bar/baz/foo'] = True

        nodes = self._undirected_graph_from_trie(t)
        got = sorted((f.label, t.label) for f in nodes for t in f.neighbours)
        self.assertEqual([('', 'bar'),
                          ('', 'foo'),
                          ('bar', ''),
                          ('bar', 'bar/baz'),
                          ('bar/baz', 'bar'),
                          ('bar/baz', 'bar/baz/foo'),
                          ('bar/baz/foo', 'bar/baz'),
                          ('foo', ''),
                          ('foo', 'foo/bar'),
                          ('foo', 'foo/qux'),
                          ('foo/bar', 'foo'),
                          ('foo/bar', 'foo/bar/baz'),
                          ('foo/bar/baz', 'foo/bar'),
                          ('foo/qux', 'foo'),
                          ('foo/qux', 'foo/qux/baz'),
                          ('foo/qux/baz', 'foo/qux')], got)

    def test_traverse_large(self):
        """Test code that is shown in traverse's docstring; stress test."""
        nodes = self._undirected_graph_from_trie(self.create_trie())
        self.assertEqual((100 * 1000 - (100 * 99) / 2) * 2 + 1, len(nodes))


if __name__ == '__main__':
    unittest.main()
