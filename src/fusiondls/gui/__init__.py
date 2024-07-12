import pickle
import sys
from typing import Optional

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtCore import QDir
from matplotlib.lines import Line2D

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic fusiondls_gui.ui -o ui_fusiondls.py
from .ui_fusiondls import Ui_FusiondlsGUI
from .plot_widget import MatplotlibWidget

from ..geometry import MagneticGeometry, _drop_properties


class FusiondlsGUI(QMainWindow, Ui_FusiondlsGUI):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.ui = Ui_FusiondlsGUI()
        self.ui.setupUi(self)

        self.ui.file_read_button.clicked.connect(self.read_balance_file)
        self.ui.file_input.returnPressed.connect(self.load_balance_file)

        self.ui.designComboBox.currentTextChanged.connect(self.update_side_box)

        self._balance_file: Optional[dict] = None
        self._geometry: Optional[MagneticGeometry] = None

        self.plot_widget = MatplotlibWidget(self.ui.field_plot)

        self.ui.sideComboBox.currentTextChanged.connect(self.load_geometry)
        self.ui.sideComboBox.currentTextChanged.connect(self.field_plot)

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
            self.ui.statusBar.showMessage(f"Unknown design {design_key!r}")
            return

        side = design.get(side_key, None)
        if side is None:
            self.ui.statusBar.showMessage(f"Unknown side {side_key!r}")
            return

        self._geometry = MagneticGeometry(**_drop_properties(side))
        self.ui.statusBar.showMessage(
            f"Loaded {design_key}:{side_key} from {self.ui.file_input.text()}"
        )

    def field_plot(self):
        if self._geometry is None:
            return

        self.plot_widget._clean_axes()
        ax = self.plot_widget.figure.subplots()
        s = self._geometry.S
        btot = self._geometry.Btot
        size = 100

        ax.plot(s, btot, color="C1")
        ax.scatter(
            self._geometry.Sx,
            self._geometry.Bx,
            color="C1",
            marker="x",
            s=size,
            label="X-point",
        )
        ax.scatter(s[0], btot[0], color="C1", marker="o", s=size, label="Target")
        ax.scatter(s[-1], btot[-1], color="C1", marker="d", s=size, label="Midplane")
        ax.set_xlabel(r"$S_{\parallel}$ (m from target)")
        ax.set_ylabel(r"$B_{tot}$ (T)")
        ax.legend()
        self.plot_widget.figure.tight_layout()
        self.plot_widget.canvas.draw()


def run_gui():
    app = QApplication(sys.argv)
    widget = FusiondlsGUI()
    widget.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    run_gui()
