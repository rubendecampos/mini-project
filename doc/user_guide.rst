
===========
User Guide
===========

The following steps below explain you how to use this package. You can then compare the
obtained result `here <https://rubendecampos.github.io/mini-project/results>`_.

The goal of this software is compute the absolute mean error of a simple algorithm that
predict the quality of a wine or the price of a house using two Machine Learning techniques:
Linear Regression and Regression Tree.


Helper function:
^^^^^^^^^^^^^^^^

The helper function should provide you enough informations on how to run this program:

.. code-block:: 

    $ python saru -h

But if you trouble understanding it, you can continue reading this section.


Selecting the dataset:
^^^^^^^^^^^^^^^^^^^^^^

You can chose the dataset that will be computed using the ``--dataset`` option.

example:

.. code-block:: 

    $ python saru --dataset red-wine

The available choices are: *wine*, *red-wine*, *white-wine* and *housing*. *Wine* is 
the combination of *red-wine* and *white-wine*.

By default: *white-wine*


Preprocessing methods:
^^^^^^^^^^^^^^^^^^^^^^

You can also chose which preprocessing method will be aplied to the set of data using 
the ``--prep`` option.

example:

.. code-block:: 

    $ python saru --prep minmax

The available choices are: *minmax*, *znorm*, *poly-minmax* and *poly-znorm*.

By default: *minmax*


Protocols:
^^^^^^^^^^

Finally, you can chose which protocol's results you want to display. This simple project
use 3 protocols and all 3 are displayed by default.

Use the ``-p`` option:

.. code-block:: 

    $ python saru -p proto1

you can also give a list of protocols:

.. code-block:: 

    $ python sart -p proto1 proto2


Go to the `result <https://rubendecampos.github.io/mini-project/results>`_ page.