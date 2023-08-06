Version History
---------------

2.3: 2018/08/10

- New ``walk_towards`` method allows walking a path towards given
  a node with given key accessing each step of the path.  Compared to
  prefixes method, steps for nodes without assigned values are

- Fix to ``PrefixSet.copy`` not preserving type of backing trie.

- ``StringTrie`` now checks and explicitly rejects empty separators.
  Previously empty separator would be accepted but lead to confusing
  errors later on.  [Thanks to Waren Long].

- Various documentation improvements, Python 2/3 compatibility and
  test coverage (python-coverage reports 100% \o/).

2.2: 2017/06/03

- Fixes to ``setup.py`` breaking on Windows which prevents
  installation among other things.

2.1: 2017/03/23

- The library is now Python 3 compatible.

- Value returend by ``shortest_prefix`` and ``longest_prefix`` evaluates
  to false if no prefix was found.  This is in addition to it being
  a pair of Nones of course.

2.0: 2016/07/06

- Sorting of child nodes is disabled by default for better performance.
  ``enable_sorting`` method can be used to bring back old behaviour.

- Tries of arbitrary depth can be pickled without reaching Python’s
  recursion limits.  (N.B. The pickle format is incompatible with one
  from 1.2 release).  ``_Node``’s ``__getstate__`` and ``__setstate__``
  method can be used to implement other serialisation methods such as
  JSON.

1.2: 2016/06/21  [pulled back from PyPi]

- Tries can now be pickled.

- Iterating no longer uses recursion so tries of arbitrary depth can be
  iterated over.  The ``traverse`` method, however, still uses recursion
  thus cannot be used on big structures.

1.1: 2016/01/18

- Fixed PyPi installation issues; all should work now.

1.0: 2015/12/16

- The module has been renamed from ``trie`` to ``pygtrie``.  This
  could break current users but see documentation for how to quickly
  upgrade your scripts.

- Added ``traverse`` method which goes through the nodes of the trie
  preserving structure of the tree.  This is a depth-first traversal
  which can be used to search for elements or translate a trie into
  a different tree structure.

- Minor documentation fixes.

0.9.3: 2015/05/28

- Minor documentation fixes.

0.9.2: 2015/05/28

- Added Sphinx configuration and updated docstrings to work better
  with Sphinx.

0.9.1: 2014/02/03

- New name.

0.9: 2014/02/03

- Initial release.
