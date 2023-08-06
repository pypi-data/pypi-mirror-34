Py-Spy: A fast sampling profiler for Python programs.
=====================================================

`Build Status <https://travis-ci.org/benfred/py-spy>`__ `Windows Build
status <https://ci.appveyor.com/project/benfred/py-spy>`__

Py-Spy is a fast sampling profiler for Python programs. It lets you
visualize what your Python program is spending time on without
restarting the program or modifiying the code in any way. Py-Spy is
extremely low overhead: it is written in Rust for speed and doesn’t
pause or slow down the profiled Python program. This means Py-Spy is
safe to use in production.

Py-Spy works on Linux, OSX and Windows, and supports profiling all
recent versions of the CPython interpreter (versions 2.3-2.7 and
3.3-3.7).

Installation
^^^^^^^^^^^^

Prebuilt binary wheels can be installed from PyPI with:

::

   pip install py-spy

Usage
^^^^^

py-spy works from the command line and takes either the PID of the
program you want to sample from, or the command line of the python
program you want to run:

.. code:: bash

   py-spy --pid 12345
   # OR
   py-spy -- python myprogram.py

The default visualization is a
`top-like <https://linux.die.net/man/1/top>`__ live view of your python
program:

.. figure:: ./images/console_viewer.gif
   :alt: console viewer demo

   console viewer demo

There is also support for generating `flame
graphs <http://www.brendangregg.com/flamegraphs.html>`__ from the
running process:

.. code:: bash

   py-spy --flame profile.svg --pid 12345
   # OR
   py-spy --flame profile.svg -- python myprogram.py

Which will generate a SVG file looking like:

.. figure:: ./images/flamegraph.svg
   :alt: flame graph

   flame graph

Credits
~~~~~~~

py-spy is heavily inspired by `Julia Evans <https://github.com/jvns/>`__
excellent work on `rbspy <http://github.com/rbspy/rbspy>`__. In
particular the code to generate the flamegraphs is taken directly from
rbspy, and this project use several crates
(`read-process-memory <https://github.com/luser/read-process-memory>`__
and `proc-maps <#TODO>`__) that were spun off from rbspy.


