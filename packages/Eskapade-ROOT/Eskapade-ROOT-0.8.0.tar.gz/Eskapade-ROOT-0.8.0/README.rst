=============
Eskapade-ROOT
=============

* Version: 0.8
* Released: Aug 2018

Eskapade is a light-weight, python-based data analysis framework, meant for modularizing all sorts of data analysis problems
into reusable analysis components. For documentation on Eskapade, please go to this `link <http://eskapade.readthedocs.io>`_.

Eskapade-ROOT is the ROOT-based extension of Eskapade.
For documentation on Eskapade-ROOT, please go `here <http://eskapade-root.readthedocs.io>`_.


Release notes
=============

Version 0.8
-----------

Version 0.8 of Eskapade-ROOT (August 2018) is a split off of the ``root-analysis`` module of Eskapade v0.7
into a separate package. 

This way, Eskapade v0.8 no longer depends on ROOT. This new package Eskapade-ROOT does require ROOT to install, clearly.



Installation
============

requirements
------------

Eskapade-ROOT requires ``Python 3.5+``, ``Eskapade v0.8+``, ``root_numpy 4.7.1`` and ``ROOT v6.10+``.
These are pre-installed in the Eskapade `docker <http://eskapade.readthedocs.io/en/latest/installation.html#eskapade-with-docker>`_.


pypi
----

To install the package from pypi, do:

.. code-block:: bash

  $ pip install Eskapade-ROOT

github
------

Alternatively, you can check out the repository from github and install it yourself:

.. code-block:: bash

  $ git clone git@github.com:KaveIO/Eskapade-ROOT.git eskapade-root

To (re)install the python code from your local directory, type from the top directory:

.. code-block:: bash

  $ pip install -e eskapade-root

To (re)compile the cxx library, execute the following commands from the top directory:

.. code-block:: bash

  $ cd cxx
  $ cmake esroofit
  $ cmake --build . -- -j1
  $ cd ../
  $ pip install -e .

python
------

After installation, you can now do in Python:

.. code-block:: python

  import esroofit

To load the Eskapade ROOT library in python, do:

.. code-block:: python

  from esroofit import roofit_utils
  roofit_utils.load_libesroofit()

**Congratulations, you are now ready to use Eskapade-ROOT!**


Quick run
=========

To see the available Eskapade example, do:

.. code-block:: bash

  $ export TUTDIR=`pip show Eskapade-ROOT | grep Location | awk '{ print $2"/esroofit/tutorials" }'`
  $ ls -l $TUTDIR/

E.g. you can now run:

.. code-block:: bash

  $ eskapade_run $TUTDIR/esk401_roothist_fill_plot_convert.py


For all available examples, please see the `tutorials <http://eskapade-root.readthedocs.io/en/latest/tutorials.html>`_.


Contact and support
===================

Contact us at: kave [at] kpmg [dot] com

Please note that the KPMG Eskapade group provides support only on a best-effort basis.
