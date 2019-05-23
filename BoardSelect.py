# Board selection window interface

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)



class Ui_Dialog(object):
    def setupUi(self, Dialog):

        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(420, 274)
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(70, 50, 281, 41))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.number_1 = QtGui.QPushButton(Dialog)
        self.number_1.setGeometry(QtCore.QRect(30, 140, 112, 34))
        self.number_1.setObjectName(_fromUtf8("pushButton"))
        self.number_2 = QtGui.QPushButton(Dialog)
        self.number_2.setGeometry(QtCore.QRect(160, 140, 112, 34))
        self.number_2.setObjectName(_fromUtf8("pushButton_2"))
        self.number_3 = QtGui.QPushButton(Dialog)
        self.number_3.setGeometry(QtCore.QRect(290, 140, 112, 34))
        self.number_3.setObjectName(_fromUtf8("pushButton_3"))
        self.library = QtGui.QPushButton(Dialog)
        self.library.setGeometry(QtCore.QRect(160, 190, 112, 34))
        self.library.setObjectName(_fromUtf8("libbutton"))



        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # return number_1,number_2,number_3

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.lineEdit.setText(_translate("Dialog", "Which board do you want to load ? ", None))
        self.number_1.setText(_translate("Dialog", "Number 1", None))
        self.number_2.setText(_translate("Dialog", "Number 2", None))
        self.number_3.setText(_translate("Dialog", "Number 3", None))
        self.library.setText(_translate("Dialog","Library",None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

