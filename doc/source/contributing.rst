.. _ref_contributing:

============
Contributing
============
Guidance on contributing to a PyAnsys library appears in the
`Contributing <https://dev.docs.pyansys.com/overview/contributing.html>`_ topic
in the *PyAnsys Developer's Guide*. Ensure that you are thoroughly familiar with
it and all `Guidelines and Best Practices
<https://dev.docs.pyansys.com/guidelines/index.html>`_ before attempting to
contribute to the PyAnsys Tools Report repository.
 
The following contribution information is specific to the PyAnsys Tools Report repository.

Cloning the PyAnsys Tools Report repository
-------------------------------------------
Run this code to clone and install the latest version of the repository in development
mode:

.. code::

    git clone https://github.com/pyansys/pyansys-tools-report.git
    cd pyansys-tools-report
    pip install .

    
In case of looking for the **test** requirements, run the following:

.. code::
    
    pip install .[test]


Building documentation
----------------------
To build the documentation locally you need to follow these steps at the root
directory of the repository:

.. code:: 

    pip install .[doc]
    make -C doc html

After the build completes the HTML documentation locates itself in the
``_builds/html`` directory and you can load the ``index.html`` into a web
browser. To clean the documentation you can execute this command:

.. code::

    make -C doc clean

Posting issues
--------------
Use the `PyAnsys Tools Report Issues <https://github.com/pyansys/pyansys-tools-report/issues>`_ page to
submit questions, report bugs, and request new features.


Code style
----------
PyAnsys Tools Report is compliant with `PyAnsys Development Code Style Guide
<https://dev.docs.pyansys.com/coding_style/index.html>`_.  Code style checks use
`pre-commit <https://pre-commit.com/>`_. Install this tool and
activate it executing the following commands:

.. code::

   python -m pip install pre-commit
   pre-commit install

Then, you can make used of the available configuration file ``.pre-commit-config.yml``,
which will be automatically detected by pre-commit:

.. code::

   pre-commit run --all-files --show-diff-on-failure

