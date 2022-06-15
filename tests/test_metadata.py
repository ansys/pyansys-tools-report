import ansys.tools.report as report


def test_pkg_version():
    """Test the correct functioning of the version() method."""

    assert report.version() == "0.1.2"
