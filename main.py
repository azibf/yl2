from random import randint
import sys
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 500)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(170, 230, 112, 34))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Bam"))


class Main(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.z = 0
        self.x = 0
        self.y = 0
        self.color = QColor('yellow')
        self.show()
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.z = randint(10, 100)
        self.x = randint(0, 500)
        self.y = randint(0, 500)
        self.color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawc(qp)
        qp.end()

    def drawc(self, qp):
        qp.setBrush(self.color)
        qp.drawEllipse(self.x, self.y, self.z, self.z)
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())