import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
QInputDialog, QLineEdit, QVBoxLayout, QListView, QAbstractItemView, QMessageBox)
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import (QStandardItemModel, QStandardItem, QIcon)
#To allow only int
#self.onlyInt = QIntValidator()
#self.LineEdit.setValidator(self.onlyInt)

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "Calculator"
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)

        self.list_view = QListView()
        self.list_model = QStandardItemModel(self.list_view)
        self.list_view.setModel(self.list_model)

        self.textbox = QLineEdit(self)
        self.textbox.move(20,20)
        self.textbox.resize(280,40)

        self.textbox2 = QLineEdit(self)
        self.textbox2.move(20,20)
        self.textbox2.resize(280,40)

        self.buttonA = QPushButton('+')
        self.buttonA.setToolTip('Addition')
        self.buttonA.move(100,70)
        self.buttonA.setDisabled(True)

        self.buttonS = QPushButton('-')
        self.buttonS.setToolTip('Subtraction')
        self.buttonS.move(150,70)
        self.buttonS.setDisabled(True)

        self.buttonD = QPushButton('/')
        self.buttonD.setToolTip('Division')
        self.buttonD.move(200,70)
        self.buttonD.setDisabled(True)

        self.buttonM = QPushButton('*')
        self.buttonM.setToolTip('Multiplication')
        self.buttonM.move(250,70)
        self.buttonM.setDisabled(True)

        #organizes everything vertically
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.list_view)
        self.vbox.addWidget(self.textbox)
        self.vbox.addWidget(self.textbox2)
        self.vbox.addWidget(self.buttonA)
        self.vbox.addWidget(self.buttonS)
        self.vbox.addWidget(self.buttonD)
        self.vbox.addWidget(self.buttonM)
        self.setLayout(self.vbox)

        #connects to the actual math
        self.buttonA.clicked.connect(self.on_click_a)
        self.buttonS.clicked.connect(self.on_click_s)
        self.buttonD.clicked.connect(self.on_click_d)
        self.buttonM.clicked.connect(self.on_click_m)

        #clears the textboxes
        self.buttonA.clicked.connect(self.textbox.clear)
        self.buttonA.clicked.connect(self.textbox2.clear)
        self.buttonS.clicked.connect(self.textbox.clear)
        self.buttonS.clicked.connect(self.textbox2.clear)
        self.buttonD.clicked.connect(self.textbox.clear)
        self.buttonD.clicked.connect(self.textbox2.clear)
        self.buttonM.clicked.connect(self.textbox.clear)
        self.buttonM.clicked.connect(self.textbox2.clear)

        #connects to see if there is text in the box
        self.textbox.textChanged.connect(self.on_text_changed)
        self.textbox2.textChanged.connect(self.on_text_changed)
        self.show()

    @pyqtSlot()
    #check if something is in the box
    def on_text_changed(self):
        self.buttonA.setEnabled(bool(self.textbox.text()) and bool(self.textbox2.text()))
        self.buttonS.setEnabled(bool(self.textbox.text()) and bool(self.textbox2.text()))
        self.buttonD.setEnabled(bool(self.textbox.text()) and bool(self.textbox2.text()))
        self.buttonM.setEnabled(bool(self.textbox.text()) and bool(self.textbox2.text()))

    def on_click_a(self):
        textboxValue1 = float(self.textbox.text())
        textboxValue2 = float(self.textbox2.text())
        operationA = str(self.textbox.text()) +  " + " + str(self.textbox2.text()) + " ="
        answerA = round(textboxValue1 + textboxValue2,4)
        list_item = QStandardItem(operationA)
        self.list_model.appendRow(list_item)
        displayA = str(answerA)
        list_item2 = QStandardItem(displayA)
        self.list_model.appendRow(list_item2)

    def on_click_s(self):
        textboxValue1 = float(self.textbox.text())
        textboxValue2 = float(self.textbox2.text())
        operationS = str(self.textbox.text()) +  " - " + str(self.textbox2.text()) + " ="
        answerS = round(textboxValue1 - textboxValue2,4)
        list_item = QStandardItem(operationS)
        self.list_model.appendRow(list_item)
        displayS = str(answerS)
        list_item2 = QStandardItem(displayS)
        self.list_model.appendRow(list_item2)

    def on_click_d(self):
        textboxValue1 = float(self.textbox.text())
        textboxValue2 = float(self.textbox2.text())
        operationD = str(self.textbox.text()) +  " / " + str(self.textbox2.text()) + " ="
        if textboxValue2 == 0.0 or 0:
            QMessageBox.about(self, "Error!", "You can't divide by Zero!")
        else:
            answerD = round(textboxValue1 / textboxValue2,4)
            list_item = QStandardItem(operationD)
            self.list_model.appendRow(list_item)
            displayD = str(answerD)
            list_item2 = QStandardItem(displayD)
            self.list_model.appendRow(list_item2)

    def on_click_m(self):
        textboxValue1 = float(self.textbox.text())
        textboxValue2 = float(self.textbox2.text())
        operationM = str(self.textbox.text()) +  " * " + str(self.textbox2.text()) + " ="
        answerM = round(textboxValue1 * textboxValue2,4)
        list_item = QStandardItem(operationM)
        self.list_model.appendRow(list_item)
        displayM = str(answerM)
        list_item2 = QStandardItem(displayM)
        self.list_model.appendRow(list_item2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    return_code = app.exec_()
    sys.exit(return_code)
