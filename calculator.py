from PyQt5 import QtWidgets
from calculator_ui import Ui_Calculator

class CalculatorWindow(QtWidgets.QWidget,Ui_Calculator):

    firstNum = None
    userIsTypingSecondNumber = False

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        # Connect buttons
        self.num_0_btn.clicked.connect(self.digit_pressed)
        self.num_1_btn.clicked.connect(self.digit_pressed)
        self.num_2_btn.clicked.connect(self.digit_pressed)
        self.num_3_btn.clicked.connect(self.digit_pressed)
        self.num_4_btn.clicked.connect(self.digit_pressed)
        self.num_5_btn.clicked.connect(self.digit_pressed)
        self.num_6_btn.clicked.connect(self.digit_pressed)
        self.num_7_btn.clicked.connect(self.digit_pressed)
        self.num_8_btn.clicked.connect(self.digit_pressed)
        self.num_9_btn.clicked.connect(self.digit_pressed)

        self.point_btn.clicked.connect(self.decimal_pressed)

        self.percentage_btn.clicked.connect(self.unary_operation_pressed)
        self.p_n_btn.clicked.connect(self.unary_operation_pressed)

        self.clear_btn.clicked.connect(self.clear_operation_pressed)

        self.addition_btn.clicked.connect(self.binary_operation_pressed)
        self.subtration_btn.clicked.connect(self.binary_operation_pressed)
        self.multiplication_btn.clicked.connect(self.binary_operation_pressed)
        self.division_btn.clicked.connect(self.binary_operation_pressed)

        self.equal_btn.clicked.connect(self.equal_operation_pressed)

        self.addition_btn.setCheckable(True)
        self.subtration_btn.setCheckable(True)
        self.multiplication_btn.setCheckable(True)
        self.division_btn.setCheckable(True)



    def digit_pressed(self):

        button = self.sender()
        #self.sender is for multiple button
        if ((self.addition_btn.isChecked() or self.subtration_btn.isChecked() or
                self.multiplication_btn.isChecked() or self.division_btn.isChecked()) and
                (not self.userIsTypingSecondNumber)):
            newLabel = format(float(button.text()), ".8g")
            self.userIsTypingSecondNumber = True
        else:
            if (("." in self.Results.text()) and (button.text() == "0")):
                newLabel = format(self.Results.text() + button.text(), ".8")
            else:
                newLabel = format(float(self.Results.text() + button.text()), ".8g")

        self.Results.setText(newLabel)

    def decimal_pressed(self):
        if "." not in self.Results.text():
            # Prvent double decimal
            self.Results.setText(self.Results.text() + '.')

    def unary_operation_pressed(self):
        button = self.sender()
        labelNumber = float(self.Results.text())

        if button.text() == "±":
            labelNumber *= -1
        else:
            labelNumber *= 0.01

        newLabel = format(labelNumber, ".8g")
        self.Results.setText(newLabel)

    def binary_operation_pressed(self):
        button = self.sender()
        # if (button.text() == "+"):

        self.firstNum = float(self.Results.text())
        button.setChecked(True)

    def equal_operation_pressed(self):

        secondNum = float(self.Results.text())

        if self.addition_btn.isChecked():
            labelNumber = self.firstNum + secondNum
            newLabel = format(labelNumber, ".8g")
            self.Results.setText(newLabel)
            self.addition_btn.setChecked(False)
        elif self.subtration_btn.isChecked():
            labelNumber = self.firstNum - secondNum
            newLabel = format(labelNumber, ".8g")
            self.Results.setText(newLabel)
            self.subtration_btn.setChecked(False)
        elif self.multiplication_btn.isChecked():
            labelNumber = self.firstNum * secondNum
            newLabel = format(labelNumber, ".8g")
            self.Results.setText(newLabel)
            self.multiplication_btn.setChecked(False)
        elif self.division_btn.isChecked():
            labelNumber = self.firstNum / secondNum
            newLabel = format(labelNumber, ".8g")
            self.Results.setText(newLabel)
            self.division_btn.setChecked(False)

        self.userIsTypingSecondNumber = False

    def clear_operation_pressed(self):
        self.addition_btn.setChecked(False)
        self.subtration_btn.setChecked(False)
        self.multiplication_btn.setChecked(False)
        self.division_btn.setChecked(False)

        self.userIsTypingSecondNumber = False

        self.Results.setText("0")


