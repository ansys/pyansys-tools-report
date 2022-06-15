import ansys.tools as ansys_tools
import ansys.tools.report as ansys_tools_report


def test_pkg_version_method():
    """Test the correct functioning of the version() method."""

    assert ansys_tools_report.version() == "0.1.dev0"


def test_pkg_version_var():
    """Test the correct functioning of the __version__ var in __init__.py file method."""

    assert ansys_tools.__version__ == "0.1.dev0"
