# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fusiondls_gui.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QAction,
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QFormLayout,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMenu,
    QMenuBar,
    QPlainTextEdit,
    QPushButton,
    QSizePolicy,
    QStatusBar,
    QWidget,
)


class Ui_FusiondlsGUI(object):
    def setupUi(self, FusiondlsGUI):
        if not FusiondlsGUI.objectName():
            FusiondlsGUI.setObjectName("FusiondlsGUI")
        FusiondlsGUI.resize(1691, 935)
        self.centralwidget = QWidget(FusiondlsGUI)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.gamma_sheath_label = QLabel(self.centralwidget)
        self.gamma_sheath_label.setObjectName("gamma_sheath_label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.gamma_sheath_label)

        self.gamma_sheath_input = QLineEdit(self.centralwidget)
        self.gamma_sheath_input.setObjectName("gamma_sheath_input")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.gamma_sheath_input)

        self.Tt_label = QLabel(self.centralwidget)
        self.Tt_label.setObjectName("Tt_label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.Tt_label)

        self.qpllu0_label = QLabel(self.centralwidget)
        self.qpllu0_label.setObjectName("qpllu0_label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.qpllu0_label)

        self.nu_label = QLabel(self.centralwidget)
        self.nu_label.setObjectName("nu_label")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.nu_label)

        self.nu0_label = QLabel(self.centralwidget)
        self.nu0_label.setObjectName("nu0_label")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.nu0_label)

        self.cz0_label = QLabel(self.centralwidget)
        self.cz0_label.setObjectName("cz0_label")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.cz0_label)

        self.alpha_label = QLabel(self.centralwidget)
        self.alpha_label.setObjectName("alpha_label")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.alpha_label)

        self.controlVariableLabel = QLabel(self.centralwidget)
        self.controlVariableLabel.setObjectName("controlVariableLabel")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.controlVariableLabel)

        self.controlVariableComboBox = QComboBox(self.centralwidget)
        self.controlVariableComboBox.addItem("")
        self.controlVariableComboBox.addItem("")
        self.controlVariableComboBox.addItem("")
        self.controlVariableComboBox.setObjectName("controlVariableComboBox")

        self.formLayout.setWidget(
            7, QFormLayout.FieldRole, self.controlVariableComboBox
        )

        self.balanceFileLabel = QLabel(self.centralwidget)
        self.balanceFileLabel.setObjectName("balanceFileLabel")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.balanceFileLabel)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.file_input = QLineEdit(self.centralwidget)
        self.file_input.setObjectName("file_input")

        self.horizontalLayout_4.addWidget(self.file_input)

        self.file_read_button = QPushButton(self.centralwidget)
        self.file_read_button.setObjectName("file_read_button")

        self.horizontalLayout_4.addWidget(self.file_read_button)

        self.formLayout.setLayout(8, QFormLayout.FieldRole, self.horizontalLayout_4)

        self.designLabel = QLabel(self.centralwidget)
        self.designLabel.setObjectName("designLabel")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.designLabel)

        self.designComboBox = QComboBox(self.centralwidget)
        self.designComboBox.setObjectName("designComboBox")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.designComboBox)

        self.sideLabel = QLabel(self.centralwidget)
        self.sideLabel.setObjectName("sideLabel")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.sideLabel)

        self.sideComboBox = QComboBox(self.centralwidget)
        self.sideComboBox.setObjectName("sideComboBox")

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.sideComboBox)

        self.Tt_input = QLineEdit(self.centralwidget)
        self.Tt_input.setObjectName("Tt_input")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.Tt_input)

        self.qpllu0_input = QLineEdit(self.centralwidget)
        self.qpllu0_input.setObjectName("qpllu0_input")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.qpllu0_input)

        self.nu_input = QLineEdit(self.centralwidget)
        self.nu_input.setObjectName("nu_input")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.nu_input)

        self.nu0_input = QLineEdit(self.centralwidget)
        self.nu0_input.setObjectName("nu0_input")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.nu0_input)

        self.cz0_input = QLineEdit(self.centralwidget)
        self.cz0_input.setObjectName("cz0_input")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.cz0_input)

        self.alpha_input = QLineEdit(self.centralwidget)
        self.alpha_input.setObjectName("alpha_input")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.alpha_input)

        self.horizontalLayout.addLayout(self.formLayout)

        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.runButton = QPushButton(self.centralwidget)
        self.runButton.setObjectName("runButton")

        self.horizontalLayout_3.addWidget(self.runButton)

        self.textOutput = QPlainTextEdit(self.centralwidget)
        self.textOutput.setObjectName("textOutput")
        self.textOutput.setMaximumSize(QSize(16777215, 100))

        self.horizontalLayout_3.addWidget(self.textOutput)

        self.gridLayout_2.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)

        self.field_plot = QWidget(self.centralwidget)
        self.field_plot.setObjectName("field_plot")
        self.field_plot.setMinimumSize(QSize(0, 100))

        self.gridLayout_2.addWidget(self.field_plot, 1, 0, 1, 1)

        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.main_plot = QWidget(self.centralwidget)
        self.main_plot.setObjectName("main_plot")
        self.main_plot.setMinimumSize(QSize(800, 0))

        self.gridLayout_3.addWidget(self.main_plot, 0, 1, 1, 1)

        FusiondlsGUI.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(FusiondlsGUI)
        self.menuBar.setObjectName("menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1691, 23))
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        FusiondlsGUI.setMenuBar(self.menuBar)
        self.statusBar = QStatusBar(FusiondlsGUI)
        self.statusBar.setObjectName("statusBar")
        FusiondlsGUI.setStatusBar(self.statusBar)

        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(FusiondlsGUI)

        QMetaObject.connectSlotsByName(FusiondlsGUI)

    # setupUi

    def retranslateUi(self, FusiondlsGUI):
        FusiondlsGUI.setWindowTitle(
            QCoreApplication.translate("FusiondlsGUI", "FusiondlsGUI", None)
        )
        self.gamma_sheath_label.setText(
            QCoreApplication.translate("FusiondlsGUI", "gamma_sheath", None)
        )
        self.gamma_sheath_input.setText(
            QCoreApplication.translate("FusiondlsGUI", "7", None)
        )
        self.Tt_label.setText(QCoreApplication.translate("FusiondlsGUI", "Tt", None))
        self.qpllu0_label.setText(
            QCoreApplication.translate("FusiondlsGUI", "qpllu0", None)
        )
        self.nu_label.setText(QCoreApplication.translate("FusiondlsGUI", "nu", None))
        self.nu0_label.setText(QCoreApplication.translate("FusiondlsGUI", "nu0", None))
        self.cz0_label.setText(QCoreApplication.translate("FusiondlsGUI", "cz0", None))
        self.alpha_label.setText(
            QCoreApplication.translate("FusiondlsGUI", "alpha", None)
        )
        self.controlVariableLabel.setText(
            QCoreApplication.translate("FusiondlsGUI", "control variable", None)
        )
        self.controlVariableComboBox.setItemText(
            0, QCoreApplication.translate("FusiondlsGUI", "density", None)
        )
        self.controlVariableComboBox.setItemText(
            1, QCoreApplication.translate("FusiondlsGUI", "impurity_frac", None)
        )
        self.controlVariableComboBox.setItemText(
            2, QCoreApplication.translate("FusiondlsGUI", "power", None)
        )

        self.balanceFileLabel.setText(
            QCoreApplication.translate("FusiondlsGUI", "balance file", None)
        )
        self.file_read_button.setText(
            QCoreApplication.translate("FusiondlsGUI", "Read", None)
        )
        self.designLabel.setText(
            QCoreApplication.translate("FusiondlsGUI", "design", None)
        )
        self.sideLabel.setText(QCoreApplication.translate("FusiondlsGUI", "side", None))
        self.Tt_input.setText(QCoreApplication.translate("FusiondlsGUI", "0.5", None))
        self.qpllu0_input.setText(
            QCoreApplication.translate("FusiondlsGUI", "1e9", None)
        )
        self.nu_input.setText(QCoreApplication.translate("FusiondlsGUI", "1e20", None))
        self.nu0_input.setText(QCoreApplication.translate("FusiondlsGUI", "1e20", None))
        self.cz0_input.setText(QCoreApplication.translate("FusiondlsGUI", "0.02", None))
        self.alpha_input.setText(
            QCoreApplication.translate("FusiondlsGUI", "1000", None)
        )
        self.runButton.setText(QCoreApplication.translate("FusiondlsGUI", "&Run", None))
        self.menuFile.setTitle(
            QCoreApplication.translate("FusiondlsGUI", "&File", None)
        )

    # retranslateUi
