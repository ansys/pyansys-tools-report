import multiprocessing
import os
import platform

import ansys.tools.report as report


def test_create_ansys_report_empty():
    """Test the creation of a Report and its correct output."""

    # Instantiate a "default" Report
    rep = report.Report()

    # Assert some of its information
    #
    # CPU Count
    assert rep.cpu_count == multiprocessing.cpu_count()
    # Architecture
    assert rep.architecture == platform.architecture()[0]
    # OS
    assert rep.system == platform.system()
    # Machine
    assert rep.machine == platform.machine()

    # Assert the output of the project info (the one we can control)
    str_empty = """
Ansys Environment Report
-------------------------------------------------------------------------------


Ansys Installation
******************
No Ansys installations provided


Ansys Environment Variables
***************************
None"""

    # Assert that the empty report is properly generated
    assert rep.project_info() == str_empty


def test_create_ansys_report_with_libs():
    """Test the creation of a Report and its correct output
    when imaginary Ansys libraries are provided."""

    # Let us imagine some ansys libraries
    my_ansys_libs = {
        "MyLib1": "v1.2",
        "MyLib2": "v1.3",
    }

    # Instantiate a Report object
    rep = report.Report(ansys_libs=my_ansys_libs)

    # Assert the output of the project info (the one we can control)
    str_report = """
Ansys Environment Report
-------------------------------------------------------------------------------


Ansys Installation
******************
Version   Location
------------------
MyLib1       v1.2
MyLib2       v1.3


Ansys Environment Variables
***************************
None"""

    # Assert that the report is properly generated
    assert rep.project_info() == str_report


def test_create_ansys_report_with_vars():
    """Test the creation of a Report and its correct output
    when imaginary Ansys variables are provided."""

    # Let us imagine some ansys variables
    os.environ["MYVAR_1"] = "VAL_1"
    os.environ["MYVAR_2"] = "VAL_2"
    my_ansys_vars = ["MYVAR_1", "MYVAR_2"]

    # Instantiate a Report object
    rep = report.Report(ansys_vars=my_ansys_vars)

    # Assert the output of the project info (the one we can control)
    str_report = """
Ansys Environment Report
-------------------------------------------------------------------------------


Ansys Installation
******************
No Ansys installations provided


Ansys Environment Variables
***************************
MYVAR_1                        VAL_1
MYVAR_2                        VAL_2"""

    # Assert that the report is properly generated
    assert rep.project_info() == str_report


def test_create_ansys_report_with_libs_and_vars():
    """Test the creation of a Report and its correct output
    when imaginary Ansys libraries and variables are provided."""

    # Let us imagine some ansys libraries
    my_ansys_libs = {
        "MyLib1": "v1.2",
        "MyLib2": "v1.3",
    }

    # Let us imagine some ansys variables
    os.environ["MYVAR_1"] = "VAL_1"
    os.environ["MYVAR_2"] = "VAL_2"
    my_ansys_vars = ["MYVAR_1", "MYVAR_2"]

    # Instantiate a Report object
    rep = report.Report(ansys_libs=my_ansys_libs, ansys_vars=my_ansys_vars)

    # Assert the output of the project info (the one we can control)
    str_report = """
Ansys Environment Report
-------------------------------------------------------------------------------


Ansys Installation
******************
Version   Location
------------------
MyLib1       v1.2
MyLib2       v1.3


Ansys Environment Variables
***************************
MYVAR_1                        VAL_1
MYVAR_2                        VAL_2"""

    # Assert that the report is properly generated
    assert rep.project_info() == str_report


def test_create_ansys_repr():
    """Test the creation of a Report and its correct output
    when directly calling the object."""

    # Let us start by creating a "default" Report
    str_rep = report.Report().__repr__()

    # Define the comparison strings
    str_start = "-" * 79 + "\nPyAnsys Software and Environment Report"
    str_end = """
Ansys Environment Variables
***************************
None"""

    # Validate the start and end of the report
    assert str_rep.startswith(str_start)
    assert str_rep.endswith(str_end)


def test_create_ansys_report_with_def_vars():
    """Test the creation of a Report and its correct output
    when imaginary Ansys variables are provided. In this case,
    default vars are expected. And it is also testing when a
    default var is provided specifically, if it is not printed twice."""

    # Let us imagine some ansys variables
    os.environ["MYVAR_1"] = "VAL_1"
    os.environ["MYVAR_2"] = "VAL_2"
    os.environ["FLUENT_VAR1"] = "FL_VAL_1"
    os.environ["FLUENT_VAR2"] = "FL_VAL_2"
    my_ansys_vars = ["MYVAR_1", "MYVAR_2", "FLUENT_VAR2"]

    # Instantiate a Report object
    rep = report.Report(ansys_vars=my_ansys_vars)

    # Assert the output of the project info (the one we can control)
    str_report = """
Ansys Environment Report
-------------------------------------------------------------------------------


Ansys Installation
******************
No Ansys installations provided


Ansys Environment Variables
***************************
MYVAR_1                        VAL_1
MYVAR_2                        VAL_2
FLUENT_VAR2                    FL_VAL_2
FLUENT_VAR1                    FL_VAL_1"""

    # Assert that the report is properly generated
    assert rep.project_info() == str_report
