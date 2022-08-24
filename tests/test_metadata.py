import ansys.tools.report as ansys_tools_report

try:
    import importlib.metadata as importlib_metadata
except ModuleNotFoundError:
    import importlib_metadata

pyansys_tools_report_version = importlib_metadata.version("pyansys-tools-report")


def test_pkg_version_method():
    """Test the correct functioning of the version() method."""

    assert ansys_tools_report.version() == pyansys_tools_report_version


def test_pkg_version_var():
    """Test the correct functioning of the __version__ var in __init__.py file method."""

    assert ansys_tools_report.__version__ == pyansys_tools_report_version
