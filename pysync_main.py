import sys
import os
from PyQt4 import QtCore, QtGui
from pysync import Ui_PySync
from PyQt4.QtGui import *


class MyDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_PySync()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.sync)
        self.ui.pushButton_2.clicked.connect(self.src)
        self.ui.pushButton_3.clicked.connect(self.dst)
        self.ui.progressbar = QtGui.QProgressBar()
        self.ui.progressBar.hide()

    def src(self):
        f = QFileDialog.getExistingDirectory() #Filedialog zeigt das aktuelle Verzeichnis an
        file = self.ui.lineEdit.setText(f)


    def dst(self):
        f = QFileDialog.getExistingDirectory() #Filedialog zeigt das aktuelle Verzeichnis an
        file = self.ui.lineEdit_2.setText(f)


    def sync(self):
        data1 = self.ui.lineEdit.text()
        data2 = self.ui.lineEdit_2.text()



        if data1 == "":
            result = QMessageBox.critical(self,"Fehler","Bitte geben Sie das Quellverzeichnis an!")

        if data2 == "":
            result = QMessageBox.critical(self,"Fehler","Bitte geben Sie das Zielverzeichnis an!")


        if os.path.exists(data1) and os.path.exists(data2):


            self.ui.progressBar.show() #Progressbar wird angezeigt
            self.ui.progressBar.setMinimum(1)
            self.ui.progressBar.setMaximum(100)
            self.ui.progressBar.setValue(20) #Werte der Progressbar werden angezeigt
            self.ui.progressBar.setValue(50)

            os.system("rsync -av --progress " + data1 + " " + data2) #Eigentlicher Sync

            self.ui.progressBar.setValue(100)

            result = QMessageBox.information(self,"Info", "Synchronisation abgeschlossen!")
            self.ui.progressBar.hide()

        else:
            error = QMessageBox.critical(self,"Fehler","Ein Fehler ist aufgetreten.Bitte erneut versuchen!")
            self.ui.progressBar.hide()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyDialog()
    myapp.show()
    sys.exit(app.exec_())