"""Sphinx documentation configuration file."""
from datetime import datetime
import os

from ansys_sphinx_theme import (
    ansys_logo_white,
    ansys_logo_white_cropped,
    pyansys_logo_black,
    watermark,
)
from ansys_sphinx_theme.latex import generate_preamble
from sphinx.builders.latex import LaTeXBuilder

from ansys.tools.report import __version__

LaTeXBuilder.supported_image_types = ["image/png", "image/pdf", "image/svg+xml"]


def get_version_match(semver):
    """Evaluate the version match for the multi-documentation."""
    if semver.endswith("dev0"):
        return "dev"
    major, minor, _ = semver.split(".")
    return ".".join([major, minor])


# Project information
project = "pyansys-tools-report"
copyright = f"(c) {datetime.now().year} ANSYS, Inc. All rights reserved"
author = "ANSYS, Inc."
release = version = __version__
cname = os.getenv("DOCUMENTATION_CNAME", default="nocname.com")

# use the default pyansys logo
html_logo = pyansys_logo_black
html_theme = "ansys_sphinx_theme"

# specify the location of your github repo
html_short_title = html_title = "PyAnsys Tools Report"
html_theme_options = {
    "switcher": {
        "json_url": f"https://{cname}/release/versions.json",
        "version_match": get_version_match(__version__),
    },
    "navbar_end": ["version-switcher", "theme-switcher", "navbar-icon-links"],
    "github_url": "https://github.com/pyansys/pyansys-tools-report",
    "show_prev_next": False,
    "show_breadcrumbs": True,
    "additional_breadcrumbs": [
        ("PyAnsys", "https://docs.pyansys.com/"),
    ],
}

# Sphinx extensions
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "numpydoc",
    "myst_parser",
    "sphinx.ext.intersphinx",
    "sphinx_copybutton",
]

# Intersphinx mapping
intersphinx_mapping = {
    "python": ("https://docs.python.org/dev", None),
    # kept here as an example
    # "scipy": ("https://docs.scipy.org/doc/scipy/reference", None),
    # "numpy": ("https://numpy.org/devdocs", None),
    # "matplotlib": ("https://matplotlib.org/stable", None),
    # "pandas": ("https://pandas.pydata.org/pandas-docs/stable", None),
    # "pyvista": ("https://docs.pyvista.org/", None),
}

# numpydoc configuration
numpydoc_show_class_members = False
numpydoc_xref_param_type = True

# Consider enabling numpydoc validation. See:
# https://numpydoc.readthedocs.io/en/latest/validation.html#
numpydoc_validate = True
numpydoc_validation_checks = {
    "GL06",  # Found unknown section
    "GL07",  # Sections are in the wrong order.
    "GL08",  # The object does not have a docstring
    "GL09",  # Deprecation warning should precede extended summary
    "GL10",  # reST directives {directives} must be followed by two colons
    "SS01",  # No summary found
    "SS02",  # Summary does not start with a capital letter
    # "SS03", # Summary does not end with a period
    "SS04",  # Summary contains heading whitespaces
    # "SS05", # Summary must start with infinitive verb, not third person
    "RT02",  # The first line of the Returns section should contain only the
    # type, unless multiple values are being returned"
}

# Favicon
html_favicon = "favicon.png"

# notfound.extension
notfound_template = "404.rst"
notfound_urls_prefix = "/../"

# static path
html_static_path = ["_static"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "markdown",
    ".md": "markdown",
}

# The master toctree document.
master_doc = "index"

# Copy button customization ---------------------------------------------------
# exclude traditional Python prompts from the copied code
copybutton_prompt_text = r">>> ?|\.\.\. "
copybutton_prompt_is_regexp = True

# MyST config options ---------------------------------------------------------
myst_heading_anchors = 3

# Generate the LaTeX preamble
latex_additional_files = [watermark, ansys_logo_white, ansys_logo_white_cropped]
latex_elements = {"preamble": generate_preamble(html_title)}
