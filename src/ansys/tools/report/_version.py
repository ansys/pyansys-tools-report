"""
PyAnsys Tools Report version module.

Module containing the version function for .
"""
try:
    import importlib.metadata as importlib_metadata
except ModuleNotFoundError:
    import importlib_metadata

__version__ = importlib_metadata.version("pyansys-tools-report")


def version():
    """Return the version of the PyAnsys Report Tool.

    Returns
    -------
    str
        The version of the tool being used.
    """
    return __version__
