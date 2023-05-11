import math
import sys
from functools import partial
from PyQt6 import QtCore, QtGui
from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

ERROR_MSG = "ERROR"
WINDOW_SIZE_X = 520
WINDOW_SIZE_Y = 280
DISPLAY_HEIGHT = 55
BUTTON_SIZE = 50


class PyCalcWindow(QMainWindow):
    """main window GUI view"""
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setFixedSize(WINDOW_SIZE_X, WINDOW_SIZE_Y)
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)
        self._createDisplay()
        self._createButtons()

    def _createDisplay(self) -> None:
        """
        creates display or layout
        :return: None
        """
        self.display = QLineEdit()
        self.display.setFixedHeight(DISPLAY_HEIGHT)
        self.display.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.display.setFont(font)
        self.generalLayout.addWidget(self.display)

    def _createButtons(self) -> None:
        """
        adds buttons as keyboard
        :return: None
        """
        self.buttonMap = {}
        buttonsLayout = QGridLayout()
        keyBoard = [
            ["pi", "sin", "cos", "tan", "7", "8", "9", "/", "C"],
            ["2pi", "sinh", "cosh", "tanh", "4", "5", "6", "*", "("],
            ["log", "exp", "Mod", "e", "1", "2", "3", "-", ")"],
            ["log10", "log2", "expm1", "deg", "0", "00", ".", "+", "="],
        ]

        for row, keys in enumerate(keyBoard):
            for col, key in enumerate(keys):
                self.buttonMap[key] = QPushButton(key)
                self.buttonMap[key].setFixedSize(BUTTON_SIZE, BUTTON_SIZE)
                buttonsLayout.addWidget(self.buttonMap[key], row, col)

        self.generalLayout.addLayout(buttonsLayout)

    def setDisplayText(self, text):
        """Set the display text"""
        self.display.setText(text)
        self.display.setFocus()

    def displayText(self):
        """Get the display text"""
        return self.display.text()

    def clearDisplay(self):
        """Clear the display"""
        self.setDisplayText("")


def evaluateExpression(expression):
    """Evaluate an expression (Model)."""
    try:
        result = str(eval(expression, {}, {}))
    except Exception:
        result = ERROR_MSG
    return result


class PyCalc:
    """controller class."""
    def __init__(self, model, view):
        self._evaluate = model
        self._view = view
        self._connectSignalsAndSlots()

    def _calculateResult(self):
        result = self._evaluate(expression=self._view.displayText())
        self._view.setDisplayText(result)

    def _buildExpression(self, subExpression):
        if self._view.displayText() == ERROR_MSG:
            self._view.clearDisplay()
        expression = self._view.displayText() + subExpression
        self._view.setDisplayText(expression)

    def _signs(self):
        try:
            if self._view.displayText() == ERROR_MSG:
                self._view.clearDisplay()
            expression = str(math.sin(math.radians(float(self._view.displayText()))))
            self._view.setDisplayText(expression)
        except ValueError:
            self._view.clearDisplay

    def _cosign(self):
        try:
            if self._view.displayText() == ERROR_MSG:
                self._view.clearDisplay()
            expression = str(math.cos(math.radians(float(self._view.displayText()))))
            self._view.setDisplayText(expression)
        except ValueError:
            self._view.clearDisplay

    def _tan(self):
        try:
            if self._view.displayText() == ERROR_MSG:
                self._view.clearDisplay()
            expression = str(math.tan(math.radians(float(self._view.displayText()))))
            self._view.setDisplayText(expression)
        except ValueError:
            self._view.clearDisplay

    def _signsh(self):
        try:
            if self._view.displayText() == ERROR_MSG:
                self._view.clearDisplay()
            expression = str(math.sinh(math.radians(float(self._view.displayText()))))
            self._view.setDisplayText(expression)
        except ValueError:
            self._view.clearDisplay

    def _cosh(self):
        try:
            if self._view.displayText() == ERROR_MSG:
                self._view.clearDisplay()
            expression = str(math.cosh(math.radians(float(self._view.displayText()))))
            self._view.setDisplayText(expression)
        except ValueError:
            self._view.clearDisplay

    def _tanh(self):
        try:
            if self._view.displayText() == ERROR_MSG:
                self._view.clearDisplay()
            expression = str(math.tanh(math.radians(float(self._view.displayText()))))
            self._view.setDisplayText(expression)
        except ValueError:
            self._view.clearDisplay

    def _log(self):
        try:
            if self._view.displayText() == ERROR_MSG:
                self._view.clearDisplay()
            expression = str(math.log(float(self._view.displayText())))
            self._view.setDisplayText(expression)
        except ValueError:
            self._view.clearDisplay

    def _exp(self):
        try:
            if self._view.displayText() == ERROR_MSG:
                self._view.clearDisplay()
            expression = str(math.exp(float(self._view.displayText())))
            self._view.setDisplayText(expression)
        except ValueError:
            self._view.clearDisplay

    def _Mod(self):
        try:
            if self._view.displayText() == ERROR_MSG:
                self._view.clearDisplay()
            expression = str(math.tan(math.radians(float(self._view.displayText()))))
            self._view.setDisplayText(expression)
        except ValueError:
            self._view.clearDisplay

    def _log10(self):
        try:
            if self._view.displayText() == ERROR_MSG:
                self._view.clearDisplay()
            expression = str(math.log10(float(self._view.displayText())))
            self._view.setDisplayText(expression)
        except ValueError:
            self._view.clearDisplay

    def _log2(self):
        try:
            if self._view.displayText() == ERROR_MSG:
                self._view.clearDisplay()
            expression = str(math.log2(float(self._view.displayText())))
            self._view.setDisplayText(expression)
        except ValueError:
            self._view.clearDisplay

    def _expm1(self):
        try:
            if self._view.displayText() == ERROR_MSG:
                self._view.clearDisplay()
            expression = str(math.expm1(float(self._view.displayText())))
            self._view.setDisplayText(expression)
        except ValueError:
            self._view.clearDisplay

    def _deg(self):
        try:
            if self._view.displayText() == ERROR_MSG:
                self._view.clearDisplay()
            expression = str(math.degrees(float(self._view.displayText())))
            self._view.setDisplayText(expression)
        except ValueError:
            self._view.clearDisplay

    def _connectSignalsAndSlots(self):
        sciSlots = {"pi", "sin", "cos", "tan",
                    "2pi", "sinh", "cosh", "tanh",
                    "log", "exp", "Mod", "e",
                    "log10", "log2", "expm1", "deg"}
        for keySymbol, button in self._view.buttonMap.items():
            if keySymbol not in {"=", "C",
                                 "pi", "sin", "cos", "tan",
                                 "2pi", "sinh", "cosh", "tanh",
                                 "log", "exp", "Mod", "e",
                                 "log10", "log2", "expm1", "deg"
                                 }:
                button.clicked.connect(
                    partial(self._buildExpression, keySymbol)
                )
            elif keySymbol in sciSlots:
                if keySymbol in {"pi"}:
                    button.clicked.connect(partial(self._buildExpression, str(math.pi)))
                elif keySymbol in {"sin"}:
                    button.clicked.connect(self._signs)
                elif keySymbol in {"cos"}:
                    button.clicked.connect(self._cosign)
                elif keySymbol in {"tan"}:
                    button.clicked.connect(self._tan)
                elif keySymbol in {"2pi"}:
                    button.clicked.connect(partial(self._buildExpression, str(math.pi*2)))
                elif keySymbol in {"sinh"}:
                    button.clicked.connect(self._signsh)
                elif keySymbol in {"cosh"}:
                    button.clicked.connect(self._cosh)
                elif keySymbol in {"tanh"}:
                    button.clicked.connect(self._tanh)
                elif keySymbol in {"log"}:
                    button.clicked.connect(self._log)
                elif keySymbol in {"exp"}:
                    button.clicked.connect(self._exp)
                elif keySymbol in {"Mod"}:
                    button.clicked.connect(self._Mod)
                elif keySymbol in {"e"}:
                    button.clicked.connect(partial(self._buildExpression, str(math.e)))
                elif keySymbol in {"log10"}:
                    button.clicked.connect(self._log10)
                elif keySymbol in {"log2"}:
                    button.clicked.connect(self._log2)
                elif keySymbol in {"expm1"}:
                    button.clicked.connect(self._expm1)
                elif keySymbol in {"deg"}:
                    button.clicked.connect(self._deg)

        self._view.buttonMap["="].clicked.connect(self._calculateResult)
        self._view.display.returnPressed.connect(self._calculateResult)
        self._view.buttonMap["C"].clicked.connect(self._view.clearDisplay)


def main():
    pycalcApp = QApplication([])
    pycalcWindow = PyCalcWindow()
    pycalcWindow.show()
    PyCalc(model=evaluateExpression, view=pycalcWindow)
    sys.exit(pycalcApp.exec())


if __name__ == "__main__":
    main()
