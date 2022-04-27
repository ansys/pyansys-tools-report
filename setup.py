from setuptools import find_packages, setup

setup(
    name="pyansys-tools-report",
    version="0.1.dev0",
    description="Ansys tool for reporting your Python environment's package versions and hardware resources in a standardized way.",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
