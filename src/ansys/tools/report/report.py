# Copyright (C) 2022 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
PyAnsys Tools Report.

Module containing the standardized Report class for PyAnsys projects.
"""

import os
import sys

import scooby

__ANSYS_VARS_PREFIX__ = (
    "AWP",
    "ACP",
    "ANS",
    "FLUENT",
    "MAPDL",
    "DPF",
    "SIMPLORER",
    "SIWAVE",
    "CADOE",
)

__PYANSYS_LIBS__ = (
    "ansys_sphinx_theme",
    "ansys.acp.core",
    "ansys.dpf.composites",
    "ansys.dpf.core",
    "ansys.dpf.post",
    "ansys.fluent.core",
    "ansys.fluent.visualization",
    "ansys.fluent.parametric",
    "ansys.geometry.core",
    "ansys.hps.client",
    "ansys.mapdl.core",
    "ansys.mapdl.reader",
    "ansys.math.core",
    "ansys.mechanical.core",
    "ansys.meshing.prime",
    "ansys.modelcenter.workflow",
    "ansys.motorcad.core",
    "ansys.openapi.common",
    "ansys.optislang.core",
    "ansys.platform.instancemanagement",
    "ansys.pyensight.core",
    "ansys.rocky.core",
    "ansys.seascape",
    "ansys.simai.core",
    "ansys.systemcoupling.core",
    "ansys.turbogrid.core",
    "ansys.tools.report",
    "ansys.tools.versioning",
    "pyaedt",
    "pyedb",
    "pygranta",
    "pytwin",
)


class Report(scooby.Report):
    """Generate a :class:`scooby.Report` instance.

    Parameters
    ----------
    additional : list(ModuleType), list(str), optional
        List of packages or package names to add to output information.
        Defaults to ``None``.
    ncol : int, optional
        Number of package-columns in html table; only has effect if
        ``mode='HTML'`` or ``mode='html'``. Defaults to 3.
    text_width : int, optional
        The text width for non-HTML display modes. Defaults to 80.
    sort : bool, optional
        Alphabetically sort the packages. Defaults to ``False``.
    gpu : bool, optional
        Gather information about the GPU. Defaults to ``True`` but if
        experiencing rendering issues, pass ``False`` to safely generate
        a report.
    ansys_vars : list of str, optional
        List containing the Ansys environment variables to be reported.
        (e.g. ["MYVAR_1", "MYVAR_2" ...]). Defaults to ``None``.
    ansys_libs : dict {str : str}, optional
        Dictionary containing the Ansys libraries and versions to be reported.
        (e.g. {"MyLib" : "v1.2", ...}). Defaults to ``None``.
    """

    def __init__(
        self,
        additional=None,
        ncol=3,
        text_width=80,
        sort=False,
        gpu=True,
        ansys_vars=None,
        ansys_libs=None,
    ):
        """Report class constructor."""
        # Mandatory packages
        core = [
            "appdirs",
            "google.protobuf",  # protobuf library
            "grpc",  # grpcio
            "matplotlib",
            "numpy",
            "pyiges",
            "pyvista",
            "scipy",
            "tqdm",
        ]

        if os.name == "posix":
            core.extend(["pexpect"])

        # Optional packages
        optional = ["matplotlib"]
        if sys.version_info[1] < 9:
            optional.append("ansys_corba")

        # PyAnsys packages + additional ones
        if additional:
            additional.extend(__PYANSYS_LIBS__)
        else:
            additional = __PYANSYS_LIBS__

        # Information about the GPU - bare except in case there is a rendering
        # bug that the user is trying to report.
        if gpu:
            try:
                try:
                    from pyvista.report import GPUInfo
                except ImportError:
                    from pyvista.utilities.errors import GPUInfo  # deprecated in PyVista 0.40

                extra_meta = [(t[0], t[1]) for t in GPUInfo().get_info()]
            except Exception:
                extra_meta = ("GPU Details", "error")
        else:
            extra_meta = ("GPU Details", "None")

        # Store the ANSYS vars and libs
        self._ansys_vars = ansys_vars
        self._ansys_libs = ansys_libs

        scooby.Report.__init__(
            self,
            additional=additional,
            core=core,
            optional=optional,
            ncol=ncol,
            text_width=text_width,
            sort=sort,
            extra_meta=extra_meta,
        )

    def project_info(self):
        """Return information regarding the Ansys environment and installation.

        Returns
        -------
        str
            The project information (env variables and installation)
        """
        # List installed Ansys
        lines = ["", "Ansys Environment Report", "-" * 79, "\n"]
        lines.append("\n".join(["Ansys Installation", "******************"]))
        if not self._ansys_libs:
            lines.append("No Ansys installations provided")
        else:
            lines.append("Version   Location")
            lines.append("------------------")
            for key in sorted(self._ansys_libs.keys()):
                lines.append(f"{key}       {self._ansys_libs[key]}")
        install_info = "\n".join(lines)

        env_info_lines = [
            "\n\n\nAnsys Environment Variables",
            "***************************",
        ]
        n_var = 0
        if self._ansys_vars is not None:
            for key, value in os.environ.items():
                if key in self._ansys_vars:
                    env_info_lines.append(f"{key:<30} {value}")
                    n_var += 1

        # Loop over all environment variables
        for key, value in os.environ.items():
            # Now, check if it is an Ansys default variable
            if self._is_ansys_var(key):
                # If found, check if it is already available or not
                if (self._ansys_vars is None) or (key not in self._ansys_vars):
                    env_info_lines.append(f"{key:<30} {value}")
                    n_var += 1

        # Finally, if no env vars were found, just append None
        if not n_var:
            env_info_lines.append("None")
        env_info = "\n".join(env_info_lines)

        return install_info + env_info

    def _is_ansys_var(self, env_var):
        """
        Determine if an env. variable belongs to the set of ANSYS default env. variables.

        Parameters
        ----------
        env_var : str
            The environment variable to be evaluated.

        Returns
        -------
        bool
            ``True`` when successful, ``False`` when failed.
        """
        # Loop over the Ansys default variables prefixes
        for prefix in __ANSYS_VARS_PREFIX__:
            # Check if the "prefix" substring is found
            if env_var.startswith(prefix):
                return True

    def __repr__(self):
        """Print out the report.

        Returns
        -------
        str
            Report statement.
        """
        add_text = "-" * 79 + "\nPyAnsys Software and Environment Report"

        report = add_text + super().__repr__() + self.project_info()
        return report.replace("-" * 80, "-" * 79)  # hotfix for scooby
