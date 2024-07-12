import pickle
import sys
from typing import Optional

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from PySide6.QtCore import QDir
from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow

from ..AnalyticCoolingCurves import LfuncN
from ..geometry import MagneticGeometry, _drop_properties
from ..plot import colored_line
from ..solver import SimulationOutput, run_dls
from .plot_widget import MatplotlibWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic fusiondls_gui.ui -o ui_fusiondls.py
from .ui_fusiondls import Ui_FusiondlsGUI


class FusiondlsGUI(QMainWindow, Ui_FusiondlsGUI):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.ui = Ui_FusiondlsGUI()
        self.ui.setupUi(self)

        self._timeout = 3000

        self.ui.file_read_button.clicked.connect(self.read_balance_file)
        self.ui.file_input.returnPressed.connect(self.load_balance_file)

        self.ui.designComboBox.currentTextChanged.connect(self.update_side_box)

        self._balance_file: Optional[dict] = None
        self._geometry: Optional[MagneticGeometry] = None
        self.result: Optional[SimulationOutput] = None

        self.field_plot_widget = MatplotlibWidget(self.ui.field_plot)
        self.main_plot_widget = MatplotlibWidget(self.ui.main_plot)

        self.ui.sideComboBox.currentTextChanged.connect(self.load_geometry)
        self.ui.sideComboBox.currentTextChanged.connect(self.field_plot)

        self.ui.runButton.clicked.connect(self.run_dls)
        self.ui.spar_front_input.textChanged.connect(self.run_dls)

        self.ui.gamma_sheath_input.returnPressed.connect(self.run_dls)
        self.ui.Tt_input.returnPressed.connect(self.run_dls)
        self.ui.qpllu0_input.returnPressed.connect(self.run_dls)
        self.ui.nu_input.returnPressed.connect(self.run_dls)
        self.ui.nu0_input.returnPressed.connect(self.run_dls)
        self.ui.cz0_input.returnPressed.connect(self.run_dls)
        self.ui.alpha_input.returnPressed.connect(self.run_dls)

    def read_balance_file(self):
        filename, _ = QFileDialog.getOpenFileName(
            self, "Open balance file", QDir.currentPath(), filter="Pickle files (*.pkl)"
        )
        self.ui.file_input.setText(str(filename))
        self.load_balance_file()

    def load_balance_file(self):
        filename = str(self.ui.file_input.text())

        with open(filename, "rb") as f:
            self._balance_file = pickle.load(f)

        self.ui.designComboBox.clear()
        for design in self._balance_file:
            self.ui.designComboBox.addItem(design)

    def update_side_box(self):
        self.ui.sideComboBox.clear()
        design = self.ui.designComboBox.currentText()
        for side in self._balance_file[design]:
            self.ui.sideComboBox.addItem(side)

    def load_geometry(self):
        design_key = self.ui.designComboBox.currentText()
        side_key = self.ui.sideComboBox.currentText()

        design = self._balance_file.get(design_key, None)
        if design is None:
            self.ui.statusBar.showMessage(
                f"Unknown design {design_key!r}", self._timeout
            )
            return

        side = design.get(side_key, None)
        if side is None:
            self.ui.statusBar.showMessage(f"Unknown side {side_key!r}", self._timeout)
            return

        self._geometry = MagneticGeometry(**_drop_properties(side))
        self.ui.statusBar.showMessage(
            f"Loaded {design_key}:{side_key} from {self.ui.file_input.text()}",
            self._timeout,
        )
        self.ui.spar_front_input.setMinimum(0.0)
        self.ui.spar_front_input.setMaximum(self._geometry.S[self._geometry.Xpoint - 1])

    def run_dls(self):
        inputs = {
            "gamma_sheath": float(self.ui.gamma_sheath_input.text()),
            "Tt": float(self.ui.Tt_input.text()),
            "qpllu0": float(self.ui.qpllu0_input.text()),
            "nu": float(self.ui.nu_input.text()),
            "nu0": float(self.ui.nu0_input.text()),
            "cz0": float(self.ui.cz0_input.text()),
            "Lfunc": LfuncN,
            "alpha": float(self.ui.alpha_input.text()),
        }
        s_parallel = [self.ui.spar_front_input.value()]

        self.results = run_dls(
            inputs,
            self._geometry,
            s_parallel,
            control_variable=self.ui.controlVariableComboBox.currentText(),
        )
        self.main_plot()

    def field_plot(self):
        if self._geometry is None:
            return

        self.field_plot_widget._clean_axes()
        ax = self.field_plot_widget.figure.subplots(ncols=2)
        s = self._geometry.S
        btot = self._geometry.Btot
        size = 100

        ax[0].plot(s, btot, color="C1")
        ax[0].scatter(
            self._geometry.Sx,
            self._geometry.Bx,
            color="C1",
            marker="x",
            s=size,
            label="X-point",
        )
        ax[0].scatter(s[0], btot[0], color="C1", marker="o", s=size, label="Target")
        ax[0].scatter(s[-1], btot[-1], color="C1", marker="d", s=size, label="Midplane")
        ax[0].set_xlabel(r"$S_{\parallel}$ [m]")
        ax[0].set_ylabel(r"$B_{tot}$ (T)")
        ax[0].legend()

        _scatter = colored_line(
            self._geometry.R, self._geometry.Z, self._geometry.S, ax[1]
        )
        ax[1].set_xlabel(r"$R$ [m]")
        ax[1].set_ylabel(r"$Z$ [m]")
        ax[1].axis("equal")
        self.field_plot_widget.figure.colorbar(
            _scatter, ax=ax[1], label=r"$S_\parallel$ [m]"
        )

        self.field_plot_widget.figure.tight_layout()
        self.field_plot_widget.canvas.draw()

    def main_plot(self):
        if self.results is None:
            return

        self.main_plot_widget._clean_axes()

        if len(self.results.Splot) == 0:
            return

        def plot_xpoint(ax):
            ymin, ymax = ax.get_ylim()
            ax.vlines(
                self._geometry.Sx,
                ymin,
                ymax,
                label="Xpoint",
                color="black",
                linestyle="dashed",
            )

        ax = self.main_plot_widget.figure.subplots(2, 2)
        s_parallel = self.results.Sprofiles[0]
        ax[0, 0].plot(s_parallel, self.results.Qprofiles[0])
        ax[0, 0].set_ylabel(r"Parallel heat flux, $q_\parallel$ [$\mathrm{Wm}^{-2}$]")

        ax[0, 1].plot(s_parallel, self.results.Tprofiles[0])
        ax[0, 1].set_ylabel("Temperature [eV]")

        self.main_plot_widget.canvas.draw()

        cmap = plt.get_cmap("plasma")

        ax[1, 0].plot(s_parallel, self.results.Tprofiles[0])
        ax[1, 0].set_ylabel("Temperature [eV]")
        rad_norm = mpl.colors.LogNorm(
            max(1e-9, self.results.Tprofiles[0].min()),
            max(1e-9, self.results.Tprofiles[0].max()),
        )
        rad = colored_line(
            s_parallel,
            self.results.Tprofiles[0],
            self.results.Rprofiles[0],
            ax[1, 0],
            linewidth=5,
            cmap=cmap,
            norm=rad_norm,
        )
        self.main_plot_widget.figure.colorbar(
            rad, ax=ax[1, 0], label=r"Radiated power [$\mathrm{Wm}^{-2}$]"
        )

        ax[1, 1].plot(s_parallel, self.results.Tprofiles[0])
        ax[1, 1].set_ylabel("Temperature [eV]")
        rad_percent = colored_line(
            s_parallel,
            self.results.Tprofiles[0],
            self.results.Rprofiles[0] / np.nanmax(self.results.Rprofiles[0]),
            ax[1, 1],
            linewidth=5,
            cmap=cmap,
            norm=mpl.colors.LogNorm(1e-3, 1),
        )
        self.main_plot_widget.figure.colorbar(
            rad_percent, ax=ax[1, 1], label=r"Radiated power [% of peak]"
        )

        for ax_ in ax.flat:
            ax_.set_xlabel(r"$S_\parallel$ [m]")
            plot_xpoint(ax_)

        self.main_plot_widget.figure.tight_layout()
        self.main_plot_widget.canvas.draw()


def run_gui():
    app = QApplication(sys.argv)
    widget = FusiondlsGUI()
    widget.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    run_gui()
