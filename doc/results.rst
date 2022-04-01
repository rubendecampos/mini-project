
=========
 Results
=========

Here you can find all the results given by our program with all the different
preprocessing methods for the 3 databases :

**White wine dataset**
======================

Results using the minmax method:
--------------------------------

.. testsetup::

    import subprocess
    run_commandline = lambda cmd: print(subprocess.check_output(cmd, shell=True).decode())

.. testcode:: 

    run_commandline('python run.py --dataset white-wine --prep minmax')

Result:

.. testoutput:: 
    :options: +NORMALIZE_WHITESPACE

    'proto0' table for the 'white-wine' dataset
    Using the 'minmax' method : 
    --------------------------------------------------
    Absolute error using Linear Regression  |  0.10
    Absolute error using Regression Tree    |  0.09

    'proto1' table for the 'white-wine' dataset
    Using the 'minmax' method : 
    --------------------------------------------------
    Absolute error using Linear Regression  |  0.10
    Absolute error using Regression Tree    |  0.09

    'proto2' table for the 'white-wine' dataset
    Using the 'minmax' method : 
    --------------------------------------------------
    Absolute error using Linear Regression  |  0.10
    Absolute error using Regression Tree    |  0.09


Results using the znorm method:
--------------------------------

.. testcode:: 

    run_commandline('python run.py --dataset white-wine --prep znorm')

Result:

.. testoutput:: 
    :options: +NORMALIZE_WHITESPACE

    'proto0' table for the 'white-wine' dataset
    Using the 'znorm' method : 
    --------------------------------------------------
    Absolute error using Linear Regression  |  0.66
    Absolute error using Regression Tree    |  0.65

    'proto1' table for the 'white-wine' dataset
    Using the 'znorm' method : 
    --------------------------------------------------
    Absolute error using Linear Regression  |  0.66
    Absolute error using Regression Tree    |  0.62

    'proto2' table for the 'white-wine' dataset
    Using the 'znorm' method : 
    --------------------------------------------------
    Absolute error using Linear Regression  |  0.65
    Absolute error using Regression Tree    |  0.63


Results using the poly-minmax method:
-------------------------------------

.. testcode:: 

    run_commandline('python run.py --dataset white-wine --prep poly-minmax')

Result:

.. testoutput:: 
    :options: +NORMALIZE_WHITESPACE

    'proto0' table for the 'white-wine' dataset
    Using the 'poly-minmax' method : 
    --------------------------------------------------
    Absolute error using Linear Regression  |  0.09
    Absolute error using Regression Tree    |  0.09

    'proto1' table for the 'white-wine' dataset
    Using the 'poly-minmax' method : 
    --------------------------------------------------
    Absolute error using Linear Regression  |  0.10
    Absolute error using Regression Tree    |  0.09

    'proto2' table for the 'white-wine' dataset
    Using the 'poly-minmax' method : 
    --------------------------------------------------
    Absolute error using Linear Regression  |  0.09
    Absolute error using Regression Tree    |  0.09



Results using the poly-znorm method:
------------------------------------

.. testcode:: 

    run_commandline('python run.py --dataset white-wine --prep poly-znorm')

Result:

.. testoutput:: 
    :options: +NORMALIZE_WHITESPACE

    'proto0' table for the 'white-wine' dataset
    Using the 'poly-znorm' method : 
    --------------------------------------------------
    Absolute error using Linear Regression  |  0.64
    Absolute error using Regression Tree    |  0.64

    'proto1' table for the 'white-wine' dataset
    Using the 'poly-znorm' method : 
    --------------------------------------------------
    Absolute error using Linear Regression  |  0.64
    Absolute error using Regression Tree    |  0.60

    'proto2' table for the 'white-wine' dataset
    Using the 'poly-znorm' method : 
    --------------------------------------------------
    Absolute error using Linear Regression  |  0.62
    Absolute error using Regression Tree    |  0.62


**Red wine dataset**
====================

Results using the minmax method:
--------------------------------


Results using the znorm method:
--------------------------------


Results using the poly-minmax method:
-------------------------------------


Results using the poly-znorm method:
------------------------------------


**Housing dataset**
===================

Results using the minmax method:
--------------------------------


Results using the znorm method:
--------------------------------


Results using the poly-minmax method:
-------------------------------------


Results using the poly-znorm method:
------------------------------------