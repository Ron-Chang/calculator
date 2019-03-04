# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Calculator(object):
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.resize(280, 430)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Calculator.sizePolicy().hasHeightForWidth())
        Calculator.setSizePolicy(sizePolicy)
        Calculator.setMinimumSize(QtCore.QSize(280, 430))
        Calculator.setMaximumSize(QtCore.QSize(280, 430))
        Calculator.setSizeIncrement(QtCore.QSize(0, 0))
        Calculator.setBaseSize(QtCore.QSize(0, 0))
        Calculator.setWindowOpacity(0.975)
        Calculator.setStyleSheet("")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(Calculator)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.Results = QtWidgets.QLabel(Calculator)
        self.Results.setMaximumSize(QtCore.QSize(280, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(45)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Results.setFont(font)
        self.Results.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.Results.setStyleSheet("QLabel {\n"
"    qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"    /*border: 2px solid #E8E8E8;*/\n"
"}\n"
"\n"
"background-color : white;")
        self.Results.setIndent(15)
        self.Results.setObjectName("Results")
        self.verticalLayout_7.addWidget(self.Results)
        self.Line_5 = QtWidgets.QHBoxLayout()
        self.Line_5.setSpacing(0)
        self.Line_5.setObjectName("Line_5")
        self.clear_btn = QtWidgets.QPushButton(Calculator)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear_btn.sizePolicy().hasHeightForWidth())
        self.clear_btn.setSizePolicy(sizePolicy)
        self.clear_btn.setMinimumSize(QtCore.QSize(70, 70))
        self.clear_btn.setMaximumSize(QtCore.QSize(70, 70))
        self.clear_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clear_btn.setAutoFillBackground(False)
        self.clear_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(155, 155, 155);\n"
"    border: 1px solid #AAAAAA;\n"
"    font: 24pt \"Inconsolata\";\n"
"    color:white;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"    font: 22pt \"Inconsolata\";\n"
"    color:gray;\n"
"}")
        self.clear_btn.setAutoDefault(False)
        self.clear_btn.setDefault(False)
        self.clear_btn.setFlat(False)
        self.clear_btn.setObjectName("clear_btn")
        self.Line_5.addWidget(self.clear_btn)
        self.p_n_btn = QtWidgets.QPushButton(Calculator)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p_n_btn.sizePolicy().hasHeightForWidth())
        self.p_n_btn.setSizePolicy(sizePolicy)
        self.p_n_btn.setMinimumSize(QtCore.QSize(70, 70))
        self.p_n_btn.setMaximumSize(QtCore.QSize(70, 70))
        self.p_n_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.p_n_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(155, 155, 155);\n"
"    border: 1px solid #AAAAAA;\n"
"    font: 24pt \"Inconsolata\";\n"
"    color:white;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"    font: 22pt \"Inconsolata\";\n"
"    color:gray;\n"
"}")
        self.p_n_btn.setAutoDefault(False)
        self.p_n_btn.setDefault(False)
        self.p_n_btn.setFlat(False)
        self.p_n_btn.setObjectName("p_n_btn")
        self.Line_5.addWidget(self.p_n_btn)
        self.percentage_btn = QtWidgets.QPushButton(Calculator)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.percentage_btn.sizePolicy().hasHeightForWidth())
        self.percentage_btn.setSizePolicy(sizePolicy)
        self.percentage_btn.setMinimumSize(QtCore.QSize(70, 70))
        self.percentage_btn.setMaximumSize(QtCore.QSize(70, 70))
        self.percentage_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.percentage_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(155, 155, 155);\n"
"    border: 1px solid #AAAAAA;\n"
"    font: 24pt \"Inconsolata\";\n"
"    color:white;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"    font: 22pt \"Inconsolata\";\n"
"    color:gray;\n"
"}")
        self.percentage_btn.setAutoDefault(False)
        self.percentage_btn.setDefault(False)
        self.percentage_btn.setFlat(False)
        self.percentage_btn.setObjectName("percentage_btn")
        self.Line_5.addWidget(self.percentage_btn)
        self.division_btn = QtWidgets.QPushButton(Calculator)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.division_btn.sizePolicy().hasHeightForWidth())
        self.division_btn.setSizePolicy(sizePolicy)
        self.division_btn.setMinimumSize(QtCore.QSize(70, 70))
        self.division_btn.setMaximumSize(QtCore.QSize(70, 70))
        self.division_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.division_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 151, 57);\n"
"    color: white;\n"
"    border: 1px solid #AAAAAA;\n"
"    font: 25pt \"Inconsolata\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #FF7832, stop: 1 #FF9739);\n"
"    font: 23pt \"Inconsolata\";\n"
"}")
        self.division_btn.setAutoDefault(False)
        self.division_btn.setDefault(False)
        self.division_btn.setFlat(False)
        self.division_btn.setObjectName("division_btn")
        self.Line_5.addWidget(self.division_btn)
        self.verticalLayout_7.addLayout(self.Line_5)
        self.Line_4 = QtWidgets.QHBoxLayout()
        self.Line_4.setSpacing(0)
        self.Line_4.setObjectName("Line_4")
        self.num_7_btn = QtWidgets.QPushButton(Calculator)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.num_7_btn.sizePolicy().hasHeightForWidth())
        self.num_7_btn.setSizePolicy(sizePolicy)
        self.num_7_btn.setMinimumSize(QtCore.QSize(70, 70))
        self.num_7_btn.setMaximumSize(QtCore.QSize(70, 70))
        self.num_7_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.num_7_btn.setAutoFillBackground(False)
        self.num_7_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(55, 55, 55);\n"
"    border: 1px solid #AAAAAA;\n"
"    font: 26pt \"Helvetica\";\n"
"    color:white;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"    font: 24pt \"Helvetica\";\n"
"    color:gray;\n"
"}")
        self.num_7_btn.setAutoDefault(False)
        self.num_7_btn.setDefault(False)
        self.num_7_btn.setFlat(False)
        self.num_7_btn.setObjectName("num_7_btn")
        self.Line_4.addWidget(self.num_7_btn)
        self.num_8_btn = QtWidgets.QPushButton(Calculator)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.num_8_btn.sizePolicy().hasHeightForWidth())
        self.num_8_btn.setSizePolicy(sizePolicy)
        self.num_8_btn.setMinimumSize(QtCore.QSize(70, 70))
        self.num_8_btn.setMaximumSize(QtCore.QSize(70, 70))
        self.num_8_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.num_8_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(55, 55, 55);\n"
"    border: 1px solid #AAAAAA;\n"
"    font: 26pt \"Helvetica\";\n"
"    color:white;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"    font: 24pt \"Helvetica\";\n"
"    color:gray;\n"
"}")
        self.num_8_btn.setAutoDefault(False)
        self.num_8_btn.setDefault(False)
        self.num_8_btn.setFlat(False)
        self.num_8_btn.setObjectName("num_8_btn")
        self.Line_4.addWidget(self.num_8_btn)
        self.num_9_btn = QtWidgets.QPushButton(Calculator)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.num_9_btn.sizePolicy().hasHeightForWidth())
        self.num_9_btn.setSizePolicy(sizePolicy)
        self.num_9_btn.setMinimumSize(QtCore.QSize(70, 70))
        self.num_9_btn.setMaximumSize(QtCore.QSize(70, 70))
        self.num_9_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.num_9_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(55, 55, 55);\n"
"    border: 1px solid #AAAAAA;\n"
"    font: 26pt \"Helvetica\";\n"
"    color:white;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"    font: 24pt \"Helvetica\";\n"
"    color:gray;\n"
"}")
        self.num_9_btn.setAutoDefault(False)
        self.num_9_btn.setDefault(False)
        self.num_9_btn.setFlat(False)
        self.num_9_btn.setObjectName("num_9_btn")
        self.Line_4.addWidget(self.num_9_btn)
        self.multiplication_btn = QtWidgets.QPushButton(Calculator)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.multiplication_btn.sizePolicy().hasHeightForWidth())
        self.multiplication_btn.setSizePolicy(sizePolicy)
        self.multiplication_btn.setMinimumSize(QtCore.QSize(70, 70))
        self.multiplication_btn.setMaximumSize(QtCore.QSize(70, 70))
        self.multiplication_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.multiplication_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 151, 57);\n"
"    color: white;\n"
"    border: 1px solid #AAAAAA;\n"
"    font: 25pt \"Inconsolata\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #FF7832, stop: 1 #FF9739);\n"
"    font: 23pt \"Inconsolata\";\n"
"}")
        self.multiplication_btn.setAutoDefault(False)
        self.multiplication_btn.setDefault(False)
        self.multiplication_btn.setFlat(False)
        self.multiplication_btn.setObjectName("multiplication_btn")
        self.Line_4.addWidget(self.multiplication_btn)
        self.verticalLayout_7.addLayout(self.Line_4)
        self.Line_3 = QtWidgets.QHBoxLayout()
        self.Line_3.setSpacing(0)
        self.Line_3.setObjectName("Line_3")
        self.num_4_btn = QtWidgets.QPushButton(Calculator)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.num_4_btn.sizePolicy().hasHeightForWidth())
        self.num_4_btn.setSizePolicy(sizePolicy)
        self.num_4_btn.setMinimumSize(QtCore.QSize(70, 70))
        self.num_4_btn.setMaximumSize(QtCore.QSize(70, 70))
        self.num_4_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.num_4_btn.setAutoFillBackground(False)
        self.num_4_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(55, 55, 55);\n"
"    border: 1px solid #AAAAAA;\n"
"    font: 26pt \"Helvetica\";\n"
"    color:white;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"    font: 24pt \"Helvetica\";\n"
"    color:gray;\n"
"}")
        self.num_4_btn.setAutoDefault(False)
        self.num_4_btn.setDefault(False)
        self.num_4_btn.setFlat(False)
        self.num_4_btn.setObjectName("num_4_btn")
        self.Line_3.addWidget(self.num_4_btn)
        self.num_5_btn = QtWidgets.QPushButton(Calculator)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.num_5_btn.sizePolicy().hasHeightForWidth())
        self.num_5_btn.setSizePolicy(sizePolicy)
        self.num_5_btn.setMinimumSize(QtCore.QSize(70, 70))
        self.num_5_btn.setMaximumSize(QtCore.QSize(70, 70))
        self.num_5_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.num_5_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(55, 55, 55);\n"
"    border: 1px solid #AAAAAA;\n"
"    font: 26pt \"Helvetica\";\n"
"    color:white;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"    font: 24pt \"Helvetica\";\n"
"    color:gray;\n"
"}")
        self.num_5_btn.setAutoDefault(False)
        self.num_5_btn.setDefault(False)
        self.num_5_btn.setFlat(False)
        self.num_5_btn.setObjectName("num_5_btn")
        self.Line_3.addWidget(self.num_5_btn)
        self.num_6_btn = QtWidgets.QPushButton(Calculator)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.num_6_btn.sizePolicy().hasHeightForWidth())
        self.num_6_btn.setSizePolicy(sizePolicy)
        self.num_6_btn.setMinimumSize(QtCore.QSize(70, 70))
        self.num_6_btn.setMaximumSize(QtCore.QSize(70, 70))
        self.num_6_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.num_6_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(55, 55, 55);\n"
"    border: 1px solid #AAAAAA;\n"
"    font: 26pt \"Helvetica\";\n"
"    color:white;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"    font: 24pt \"Helvetica\";\n"
"    color:gray;\n"
"}")
        self.num_6_btn.setAutoDefault(False)
        self.num_6_btn.setDefault(False)
        self.num_6_btn.setFlat(False)
        self.num_6_btn.setObjectName("num_6_btn")
        self.Line_3.addWidget(self.num_6_btn)
        self.subtration_btn = QtWidgets.QPushButton(Calculator)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subtration_btn.sizePolicy().hasHeightForWidth())
        self.subtration_btn.setSizePolicy(sizePolicy)
        self.subtration_btn.setMinimumSize(QtCore.QSize(70, 70))
        self.subtration_btn.setMaximumSize(QtCore.QSize(70, 70))
        self.subtration_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.subtration_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 151, 57);\n"
"    color: white;\n"
"    border: 1px solid #AAAAAA;\n"
"    font: 25pt \"Inconsolata\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #FF7832, stop: 1 #FF9739);\n"
"    font: 23pt \"Inconsolata\";\n"
"}")
        self.subtration_btn.setAutoDefault(False)
        self.subtration_btn.setDefault(False)
        self.subtration_btn.setFlat(False)
        self.subtration_btn.setObjectName("subtration_btn")
        self.Line_3.addWidget(self.subtration_btn)
        self.verticalLayout_7.addLayout(self.Line_3)
        self.Line_2 = QtWidgets.QHBoxLayout()
        self.Line_2.setSpacing(0)
        self.Line_2.setObjectName("Line_2")
        self.num_1_btn = QtWidgets.QPushButton(Calculator)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.num_1_btn.sizePolicy().hasHeightForWidth())
        self.num_1_btn.setSizePolicy(sizePolicy)
        self.num_1_btn.setMinimumSize(QtCore.QSize(70, 70))
        self.num_1_btn.setMaximumSize(QtCore.QSize(70, 70))
        self.num_1_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.num_1_btn.setAutoFillBackground(False)
        self.num_1_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(55, 55, 55);\n"
"    border: 1px solid #AAAAAA;\n"
"    font: 26pt \"Helvetica\";\n"
"    color:white;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"    font: 24pt \"Helvetica\";\n"
"    color:gray;\n"
"}")
        self.num_1_btn.setAutoDefault(False)
        self.num_1_btn.setDefault(False)
        self.num_1_btn.setFlat(False)
        self.num_1_btn.setObjectName("num_1_btn")
        self.Line_2.addWidget(self.num_1_btn)
        self.num_2_btn = QtWidgets.QPushButton(Calculator)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.num_2_btn.sizePolicy().hasHeightForWidth())
        self.num_2_btn.setSizePolicy(sizePolicy)
        self.num_2_btn.setMinimumSize(QtCore.QSize(70, 70))
        self.num_2_btn.setMaximumSize(QtCore.QSize(70, 70))
        self.num_2_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.num_2_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(55, 55, 55);\n"
"    border: 1px solid #AAAAAA;\n"
"    font: 26pt \"Helvetica\";\n"
"    color:white;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"    font: 24pt \"Helvetica\";\n"
"    color:gray;\n"
"}")
        self.num_2_btn.setAutoDefault(False)
        self.num_2_btn.setDefault(False)
        self.num_2_btn.setFlat(False)
        self.num_2_btn.setObjectName("num_2_btn")
        self.Line_2.addWidget(self.num_2_btn)
        self.num_3_btn = QtWidgets.QPushButton(Calculator)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.num_3_btn.sizePolicy().hasHeightForWidth())
        self.num_3_btn.setSizePolicy(sizePolicy)
        self.num_3_btn.setMinimumSize(QtCore.QSize(70, 70))
        self.num_3_btn.setMaximumSize(QtCore.QSize(70, 70))
        self.num_3_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.num_3_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(55, 55, 55);\n"
"    border: 1px solid #AAAAAA;\n"
"    font: 26pt \"Helvetica\";\n"
"    color:white;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"    font: 24pt \"Helvetica\";\n"
"    color:gray;\n"
"}")
        self.num_3_btn.setAutoDefault(False)
        self.num_3_btn.setDefault(False)
        self.num_3_btn.setFlat(False)
        self.num_3_btn.setObjectName("num_3_btn")
        self.Line_2.addWidget(self.num_3_btn)
        self.equal_btn = QtWidgets.QPushButton(Calculator)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.equal_btn.sizePolicy().hasHeightForWidth())
        self.equal_btn.setSizePolicy(sizePolicy)
        self.equal_btn.setMinimumSize(QtCore.QSize(70, 70))
        self.equal_btn.setMaximumSize(QtCore.QSize(70, 70))
        self.equal_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.equal_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 151, 57);\n"
"    color: white;\n"
"    border: 1px solid #AAAAAA;\n"
"    font: 25pt \"Inconsolata\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #FF7832, stop: 1 #FF9739);\n"
"    font: 23pt \"Inconsolata\";\n"
"}")
        self.equal_btn.setAutoDefault(False)
        self.equal_btn.setDefault(False)
        self.equal_btn.setFlat(False)
        self.equal_btn.setObjectName("equal_btn")
        self.Line_2.addWidget(self.equal_btn)
        self.verticalLayout_7.addLayout(self.Line_2)
        self.Line_1 = QtWidgets.QHBoxLayout()
        self.Line_1.setSpacing(0)
        self.Line_1.setObjectName("Line_1")
        self.num_0_btn = QtWidgets.QPushButton(Calculator)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.num_0_btn.sizePolicy().hasHeightForWidth())
        self.num_0_btn.setSizePolicy(sizePolicy)
        self.num_0_btn.setMinimumSize(QtCore.QSize(140, 70))
        self.num_0_btn.setMaximumSize(QtCore.QSize(140, 70))
        self.num_0_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.num_0_btn.setAutoFillBackground(False)
        self.num_0_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(55, 55, 55);\n"
"    border: 1px solid #AAAAAA;\n"
"    font: 26pt \"Helvetica\";\n"
"    color:white;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"    font: 24pt \"Helvetica\";\n"
"    color:gray;\n"
"}")
        self.num_0_btn.setAutoDefault(False)
        self.num_0_btn.setDefault(False)
        self.num_0_btn.setFlat(False)
        self.num_0_btn.setObjectName("num_0_btn")
        self.Line_1.addWidget(self.num_0_btn)
        self.point_btn = QtWidgets.QPushButton(Calculator)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.point_btn.sizePolicy().hasHeightForWidth())
        self.point_btn.setSizePolicy(sizePolicy)
        self.point_btn.setMinimumSize(QtCore.QSize(70, 70))
        self.point_btn.setMaximumSize(QtCore.QSize(70, 70))
        self.point_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.point_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(155, 155, 155);\n"
"    border: 1px solid #AAAAAA;\n"
"    font: 24pt \"Inconsolata\";\n"
"    color:white;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"    font: 22pt \"Inconsolata\";\n"
"    color:gray;\n"
"}")
        self.point_btn.setAutoDefault(False)
        self.point_btn.setDefault(False)
        self.point_btn.setFlat(False)
        self.point_btn.setObjectName("point_btn")
        self.Line_1.addWidget(self.point_btn)
        self.addition_btn = QtWidgets.QPushButton(Calculator)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addition_btn.sizePolicy().hasHeightForWidth())
        self.addition_btn.setSizePolicy(sizePolicy)
        self.addition_btn.setMinimumSize(QtCore.QSize(70, 70))
        self.addition_btn.setMaximumSize(QtCore.QSize(70, 70))
        self.addition_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addition_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 151, 57);\n"
"    color: white;\n"
"    border: 1px solid #AAAAAA;\n"
"    font: 25pt \"Inconsolata\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #FF7832, stop: 1 #FF9739);\n"
"    font: 23pt \"Inconsolata\";\n"
"}")
        self.addition_btn.setAutoDefault(False)
        self.addition_btn.setDefault(False)
        self.addition_btn.setFlat(False)
        self.addition_btn.setObjectName("addition_btn")
        self.Line_1.addWidget(self.addition_btn)
        self.verticalLayout_7.addLayout(self.Line_1)
        self.Results.raise_()

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "Calculator by Ron"))
        self.Results.setText(_translate("Calculator", "0"))
        self.clear_btn.setText(_translate("Calculator", "C"))
        self.p_n_btn.setText(_translate("Calculator", "±"))
        self.percentage_btn.setText(_translate("Calculator", "%"))
        self.division_btn.setText(_translate("Calculator", "÷"))
        self.num_7_btn.setText(_translate("Calculator", "7"))
        self.num_8_btn.setText(_translate("Calculator", "8"))
        self.num_9_btn.setText(_translate("Calculator", "9"))
        self.multiplication_btn.setText(_translate("Calculator", "×"))
        self.num_4_btn.setText(_translate("Calculator", "4"))
        self.num_5_btn.setText(_translate("Calculator", "5"))
        self.num_6_btn.setText(_translate("Calculator", "6"))
        self.subtration_btn.setText(_translate("Calculator", "-"))
        self.num_1_btn.setText(_translate("Calculator", "1"))
        self.num_2_btn.setText(_translate("Calculator", "2"))
        self.num_3_btn.setText(_translate("Calculator", "3"))
        self.equal_btn.setText(_translate("Calculator", "="))
        self.num_0_btn.setText(_translate("Calculator", "0"))
        self.point_btn.setText(_translate("Calculator", "."))
        self.addition_btn.setText(_translate("Calculator", "+"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calculator = QtWidgets.QWidget()
    ui = Ui_Calculator()
    ui.setupUi(Calculator)
    Calculator.show()
    sys.exit(app.exec_())

