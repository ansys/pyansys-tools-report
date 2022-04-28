import ansys.tools.report as report


def test_pkg_version():
    assert report.version() == "0.1.dev0"
