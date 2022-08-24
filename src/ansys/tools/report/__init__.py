from ansys.tools.report.report import Report, version

try:
    import importlib.metadata as importlib_metadata
except ModuleNotFoundError:
    import importlib_metadata

__version__ = importlib_metadata.version("pyansys-tools-report")
