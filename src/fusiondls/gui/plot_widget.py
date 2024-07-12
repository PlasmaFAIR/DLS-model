from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.qt_compat import QtWidgets
from matplotlib.figure import Figure


class MatplotlibWidget:
    def __init__(self, parent):
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setParent(parent)
        self.mpl_toolbar = NavigationToolbar(self.canvas, parent)
        self.axes = self.figure.add_subplot(111)

        self.grid_layout = QtWidgets.QVBoxLayout()
        self.grid_layout.addWidget(self.canvas)
        self.grid_layout.addWidget(self.mpl_toolbar)
        parent.setLayout(self.grid_layout)

        self.callback_id = None

    def _clean_axes(self):
        """
        Make sure the figure is in a nice state
        """
        # Get rid of any extra axes
        if isinstance(self.axes, list):
            for axes in self.axes:
                del axes
            self.axes = self.figure.add_subplot(111)
        else:
            self.axes.clear()

        self.figure.clear()
        self.axes.grid(True)
        # Reset to some hardcoded default values
        self.figure.subplots_adjust(
            left=0.125, right=0.9, top=0.9, bottom=0.1, wspace=0.2, hspace=0.2
        )
        # Remove any event callbacks
        if self.callback_id:
            try:
                self.figure.canvas.mpl_disconnect(self.callback_id)
            except TypeError:
                for callback_id in self.callback_id:
                    self.figure.canvas.mpl_disconnect(callback_id)
                self.callback_id = None
