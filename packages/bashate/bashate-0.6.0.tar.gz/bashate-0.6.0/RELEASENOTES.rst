=======
bashate
=======

.. _bashate_0.6.0:

0.6.0
=====

.. _bashate_0.6.0_New Features:

New Features
------------

.. releasenotes/notes/0-dash-6-748e729ee001df73.yaml @ 925500dc009be966998e70970274b0615e3199ea

- Python 3.6 support added

.. releasenotes/notes/0-dash-6-748e729ee001df73.yaml @ 925500dc009be966998e70970274b0615e3199ea

- Hidden files such as ``.bashrc`` are no longer checked for ``#!`` (E005)

.. releasenotes/notes/0-dash-6-748e729ee001df73.yaml @ 925500dc009be966998e70970274b0615e3199ea

- A basic check for ``[[`` when using non-POSIX comparisions such as ``=~`` is added

.. releasenotes/notes/0-dash-6-748e729ee001df73.yaml @ 925500dc009be966998e70970274b0615e3199ea

- Enable bashate to be called as a module ``python -m bashate ...``

.. releasenotes/notes/0-dash-6-748e729ee001df73.yaml @ 925500dc009be966998e70970274b0615e3199ea

- Enable `pre-commit.com <https://pre-commit.com>`__ support

.. releasenotes/notes/adopt-pycodestyle-output-format-f4d6e35dadfcb6f9.yaml @ b530efc0691aea663669cd97cb3406b47ad27938

- Adoped pycodestyle/pep8 default output format.


.. _bashate_0.5.1:

0.5.1
=====

.. _bashate_0.5.1_New Features:

New Features
------------

.. releasenotes/notes/python-3-4e30b9f2b9e2dcb7.yaml @ 3e76bce89de78a4f41ae9a6a948823190401bc02

- Python 3 is supported


.. _bashate_0.5.0:

0.5.0
=====

.. _bashate_0.5.0_Bug Fixes:

Bug Fixes
---------

.. releasenotes/notes/heredoc-ignore-905b29053652f90e.yaml @ 0661da9c91f38c71d7d6b7521ff23c3dcc8f2949

- Ignore contents of ``heredoc`` values.  ``heredocs`` usually contain content in a foreign syntax so ``bashate`` will no longer consider them.

.. releasenotes/notes/heredoc-ignore-905b29053652f90e.yaml @ 0661da9c91f38c71d7d6b7521ff23c3dcc8f2949

- Continuation lines are now parsed into an array, rather than a single logical-line.  This fixes continuation lines being incorrectly reported as too long.

.. releasenotes/notes/heredoc-ignore-905b29053652f90e.yaml @ 0661da9c91f38c71d7d6b7521ff23c3dcc8f2949

- Indentation now allows emacs-formatted idents, where continuation
  lines for long commands align to the first argument above (rather
  than a strict modulo of 4).  e.g.
  
  ::
  
     longcommand arg1 arg2 arg3 \
                 arg4 arg5
  
  will no longer trigger a bad indent warning.

.. releasenotes/notes/heredoc-ignore-905b29053652f90e.yaml @ 0661da9c91f38c71d7d6b7521ff23c3dcc8f2949

- Use ``bash -n`` to detect unclosed heredocs, rather than construct our own parsing.

.. releasenotes/notes/heredoc-ignore-905b29053652f90e.yaml @ 0661da9c91f38c71d7d6b7521ff23c3dcc8f2949

- Correctly check for newlines at the end of all files; even if you only specify one file to check.


.. _bashate_0.5.0_Other Notes:

Other Notes
-----------

.. releasenotes/notes/start-using-reno-eaaafddb3fbf2010.yaml @ 0661da9c91f38c71d7d6b7521ff23c3dcc8f2949

- started using reno

