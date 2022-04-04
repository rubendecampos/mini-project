
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

    run_commandline('saru-run --dataset white-wine --prep minmax')

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
    Absolute error using Regression Tree    |  0.10

    'proto2' table for the 'white-wine' dataset
    Using the 'minmax' method : 
    --------------------------------------------------
    Absolute error using Linear Regression  |  0.10
    Absolute error using Regression Tree    |  0.09


Results using the znorm method:
--------------------------------

.. testcode:: 

    run_commandline('saru-run --dataset white-wine --prep znorm')

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
    Absolute error using Regression Tree    |  0.64


Results using the poly-minmax method:
-------------------------------------

.. testcode:: 

    run_commandline('saru-run --dataset white-wine --prep poly-minmax')

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

    run_commandline('saru-run --dataset white-wine --prep poly-znorm')

Result:

.. testoutput:: 
    :options: +NORMALIZE_WHITESPACE

    'proto0' table for the 'white-wine' dataset
    Using the 'poly-znorm' method : 
    --------------------------------------------------
    Absolute error using Linear Regression  |  0.64
    Absolute error using Regression Tree    |  0.61

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

.. testcode:: 

    run_commandline('saru-run --dataset red-wine --prep minmax')

Result:

.. testoutput:: 
    :options: +NORMALIZE_WHITESPACE

    'proto0' table for the 'red-wine' dataset
    Using the 'minmax' method : 
    --------------------------------------------------
    Absolute error using Linear Regression  |  0.10
    Absolute error using Regression Tree    |  0.10

    'proto1' table for the 'red-wine' dataset
    Using the 'minmax' method : 
    --------------------------------------------------
    Absolute error using Linear Regression  |  0.10
    Absolute error using Regression Tree    |  0.10

    'proto2' table for the 'red-wine' dataset
    Using the 'minmax' method : 
    --------------------------------------------------
    Absolute error using Linear Regression  |  0.10
    Absolute error using Regression Tree    |  0.10


Results using the znorm method:
--------------------------------

.. testcode:: 

    run_commandline('saru-run --dataset red-wine --prep znorm')

Result:

.. testoutput:: 
    :options: +NORMALIZE_WHITESPACE

    'proto0' table for the 'red-wine' dataset
    Using the 'znorm' method : 
    --------------------------------------------------
    Absolute error using Linear Regression  |  0.62
    Absolute error using Regression Tree    |  0.65

    'proto1' table for the 'red-wine' dataset
    Using the 'znorm' method : 
    --------------------------------------------------
    Absolute error using Linear Regression  |  0.61
    Absolute error using Regression Tree    |  0.63

    'proto2' table for the 'red-wine' dataset
    Using the 'znorm' method : 
    --------------------------------------------------
    Absolute error using Linear Regression  |  0.63
    Absolute error using Regression Tree    |  0.60


Results using the poly-minmax method:
-------------------------------------

.. testcode:: 

    run_commandline('saru-run --dataset red-wine --prep poly-minmax')

Result:

.. testoutput:: 
    :options: +NORMALIZE_WHITESPACE

    'proto0' table for the 'red-wine' dataset
    Using the 'poly-minmax' method : 
    --------------------------------------------------
    Absolute error using Linear Regression  |  0.11
    Absolute error using Regression Tree    |  0.10

    'proto1' table for the 'red-wine' dataset
    Using the 'poly-minmax' method : 
    --------------------------------------------------
    Absolute error using Linear Regression  |  0.10
    Absolute error using Regression Tree    |  0.11

    'proto2' table for the 'red-wine' dataset
    Using the 'poly-minmax' method : 
    --------------------------------------------------
    Absolute error using Linear Regression  |  0.11
    Absolute error using Regression Tree    |  0.11


Results using the poly-znorm method:
------------------------------------

.. testcode:: 

    run_commandline('saru-run --dataset red-wine --prep poly-znorm')

Result:

.. testoutput:: 
    :options: +NORMALIZE_WHITESPACE

    'proto0' table for the 'red-wine' dataset
    Using the 'poly-znorm' method : 
    --------------------------------------------------
    Absolute error using Linear Regression  |  0.68
    Absolute error using Regression Tree    |  0.59

    'proto1' table for the 'red-wine' dataset
    Using the 'poly-znorm' method : 
    --------------------------------------------------
    Absolute error using Linear Regression  |  0.63
    Absolute error using Regression Tree    |  0.67

    'proto2' table for the 'red-wine' dataset
    Using the 'poly-znorm' method : 
    --------------------------------------------------
    Absolute error using Linear Regression  |  0.65
    Absolute error using Regression Tree    |  0.63


**Housing dataset**
===================

Results using the minmax method:
--------------------------------

.. testcode:: 

    run_commandline('saru-run --dataset housing --prep minmax')

Result:

.. testoutput:: 
    :options: +NORMALIZE_WHITESPACE

    'proto0' table for the 'housing' dataset
    Using the 'minmax' method : 
    --------------------------------------------------
    Absolute error using Linear Regression  |  0.07
    Absolute error using Regression Tree    |  0.08

    'proto1' table for the 'housing' dataset
    Using the 'minmax' method : 
    --------------------------------------------------
    Absolute error using Linear Regression  |  0.08
    Absolute error using Regression Tree    |  0.08

    'proto2' table for the 'housing' dataset
    Using the 'minmax' method : 
    --------------------------------------------------
    Absolute error using Linear Regression  |  0.08
    Absolute error using Regression Tree    |  0.07


Results using the znorm method:
--------------------------------

.. testcode:: 

    run_commandline('saru-run --dataset housing --prep znorm')

Result:

.. testoutput:: 
    :options: +NORMALIZE_WHITESPACE

    'proto0' table for the 'housing' dataset
    Using the 'znorm' method : 
    --------------------------------------------------
    Absolute error using Linear Regression  |  0.36
    Absolute error using Regression Tree    |  0.36

    'proto1' table for the 'housing' dataset
    Using the 'znorm' method : 
    --------------------------------------------------
    Absolute error using Linear Regression  |  0.39
    Absolute error using Regression Tree    |  0.35

    'proto2' table for the 'housing' dataset
    Using the 'znorm' method : 
    --------------------------------------------------
    Absolute error using Linear Regression  |  0.41
    Absolute error using Regression Tree    |  0.39


Results using the poly-minmax method:
-------------------------------------

.. testcode:: 

    run_commandline('saru-run --dataset housing --prep poly-minmax')

Result:

.. testoutput:: 
    :options: +NORMALIZE_WHITESPACE

    'proto0' table for the 'housing' dataset
    Using the 'poly-minmax' method : 
    --------------------------------------------------
    Absolute error using Linear Regression  |  0.07
    Absolute error using Regression Tree    |  0.08

    'proto1' table for the 'housing' dataset
    Using the 'poly-minmax' method : 
    --------------------------------------------------
    Absolute error using Linear Regression  |  0.11
    Absolute error using Regression Tree    |  0.08

    'proto2' table for the 'housing' dataset
    Using the 'poly-minmax' method : 
    --------------------------------------------------
    Absolute error using Linear Regression  |  0.07
    Absolute error using Regression Tree    |  0.07


Results using the poly-znorm method:
------------------------------------

.. testcode:: 

    run_commandline('saru-run --dataset housing --prep poly-znorm')

Result:

.. testoutput:: 
    :options: +NORMALIZE_WHITESPACE

    'proto0' table for the 'housing' dataset
    Using the 'poly-znorm' method : 
    --------------------------------------------------
    Absolute error using Linear Regression  |  0.31
    Absolute error using Regression Tree    |  0.36

    'proto1' table for the 'housing' dataset
    Using the 'poly-znorm' method : 
    --------------------------------------------------
    Absolute error using Linear Regression  |  0.46
    Absolute error using Regression Tree    |  0.38

    'proto2' table for the 'housing' dataset
    Using the 'poly-znorm' method : 
    --------------------------------------------------
    Absolute error using Linear Regression  |  0.35
    Absolute error using Regression Tree    |  0.34