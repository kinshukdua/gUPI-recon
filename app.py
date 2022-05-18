import sys
import pyperclip 
from PyQt5.QtCore import QRegExp, QObject, QThread, pyqtSignal
from PyQt5.QtGui import QRegExpValidator, QIcon
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox, QDialogButtonBox, QLineEdit, QTableWidgetItem, QRadioButton, QFileDialog
)
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from main_ui import Ui_MainWindow

import requests
import concurrent.futures

from time import sleep
from sys import exit
from random import uniform as rand
from datetime import datetime


API_URL = 'https://upibankvalidator.com/api/upiValidation?upi='

phone_regex = QRegExp("[0-9]{10}")
email_regex = QRegExp("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,4}$")

#  opting to load lists from a file instead of hardcoding them
#  as this would be more flexible, allow for easier updates,
#  and allow others to make use of the lists provided
with open("data/general_suffixes.txt", "r") as suffix_file:
    upi_suffix_dict = suffix_file.read().splitlines() #  read all suffixes into a list

with open("data/mobile_suffixes.txt", "r") as mobile_suffix_file:
    mobile_suffix_dict = mobile_suffix_file.read().splitlines()

with open("data/fastag_suffixes.txt", "r") as fastag_suffix_file:
    fastag_suffix_dict = fastag_suffix_file.read().splitlines()

with open("data/gpay_suffixes.txt", "r") as gpay_suffix_file:
    gpay_suffix_dict = gpay_suffix_file.read().splitlines()



class Scraper(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    found = 0
    count = 0
    def searchvpa(self, searchtext, vpa_dict, threadcount):
        if(threadcount == 0):
            for suffix in vpa_dict:
                try:
                    self.address_discovery(searchtext + '@' + suffix, API_URL)
                except KeyboardInterrupt:
                    exit(0)
        else:
            threadcount = 10 if threadcount > 10 else threadcount
            with concurrent.futures.ThreadPoolExecutor(max_workers=threadcount) as executor:
                try:
                    for suffix in vpa_dict:
                        executor.submit(self.address_discovery, searchtext + '@' + suffix, API_URL)
                        sleep(rand(.1, .2))
                except KeyboardInterrupt:
                    #  quit ungracefully on keyboard interrupt:
                    #  considering the bandwidth consumed for requests,
                    #  there is no reason to wait for the threads to finish
                    #  sorry for the inconvenience
                    executor._threads.clear()
                    concurrent.futures.thread._threads_queues.clear()
        if self.found > 0:
            win.set_footer("Found: "+ str(self.found+1), "green")
        else:
            win.set_footer("No VPA found for: "+searchtext, "red")
        
    def address_discovery(self, vpa, api_url):
        r = requests.post(api_url+vpa)

        print(r.status_code)
        if r.status_code == 200 and r.json()['isUpiRegistered'] is True:
            rowPosition = win.Result.rowCount()
            win.Result.insertRow(rowPosition)
            win.Result.setItem(rowPosition , 0, QTableWidgetItem(r.json()['name']))
            win.Result.setItem(rowPosition , 1, QTableWidgetItem(vpa))
            win.nameEdit.setText(r.json()['name'])    
            self.found += 1
        if r.status_code == 400:
            win.set_footer("Bad Request", "red")
        if r.status_code == 429:
            win.set_footer("Too Many Requests", "red")
        self.progress.emit(self.count)
        self.count += 1
    def run(self):
        self.searchvpa(win.phoneEdit.text(), win.suffix, 2)
        self.finished.emit()

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()
        self.phoneEdit.setValidator(QRegExpValidator(phone_regex, self.phoneEdit))
        self.emailEdit.setValidator(QRegExpValidator(email_regex, self.emailEdit))
        self.nameEdit.setReadOnly(True)
        self.progressBar.setVisible(False)
        self.allUPI.setChecked(True)
        self.upibankAPI.setChecked(True)
        self.Result.setColumnCount(2)  
        self.Result.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.Result.setHorizontalHeaderLabels(["Name", "VPA"])
        self.setWindowIcon(QIcon('logo.png'))
        self.setWindowTitle("gUPI recon")

    def connectSignalsSlots(self):
        self.action_Manually.triggered.connect(self.add_api)
        self.pastePhone.clicked.connect(self.paste_phone)
        self.pasteEmail.clicked.connect(self.paste_email)
        self.Query.clicked.connect(self.query)
        self.saveButton.clicked.connect(self.saveQuery)
        self.action_Add_API_URL.triggered.connect(self.add_api)
        #self.action_Find_Replace.triggered.connect(self.findAndReplace)
        #self.action_About.triggered.connect(self.about)

    def add_api(self):
        pass

    def set_footer(self, text, color = "black"):
        self.footer.setStyleSheet("color: " + color)
        self.footer.setText(text)

    def add_api(self):
        dialog = add_API(self)
        dialog.exec()

    def paste_phone(self):
        if (QRegExp.exactMatch(phone_regex, pyperclip.paste())):
            self.phoneEdit.setText(pyperclip.paste())
        else:
            self.set_footer("Invalid phone number", "red")
    
    def paste_email(self):
        if (QRegExp.exactMatch(email_regex, pyperclip.paste())):
            self.emailEdit.setText(pyperclip.paste())
        else:
            self.set_footer("Invalid email", "red")

    def reportProgress(self, value):
        self.progressBar.setValue(round(((value+1)/len(self.suffix))*100))
        

    def saveQuery(self):
        if self.Result.rowCount() > 0:
            name, _ = QFileDialog.getSaveFileName(self, 'Save Query', self.phoneEdit.text(), 'CSV(*.csv)')
            if not name:
                return
            with open(name,'w') as file:
                for i in range(self.Result.rowCount()):
                    file.write(self.Result.item(i, 0).text())
                    file.write(", ")
                    file.write(self.Result.item(i, 1).text())
                    file.write("\n")
            footer_text = "Saved to " + name
            if len(footer_text) > 27:
                self.set_footer(footer_text[25:]+"...", "green")
            self.set_footer(footer_text, "green")
        else:
            self.set_footer("No results to save", "red")

    def query(self):
        # set footer
        self.set_footer("Querying...")
        self.thread = QThread()
        self.worker = Scraper()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.reportProgress)
        self.progressBar.setValue(0)
        self.progressBar.setVisible(True)
        self.thread.finished.connect(
            lambda: self.progressBar.setVisible(False)
        )
        self.suffix = upi_suffix_dict
        if (win.gpayUPI.isChecked()):
            self.suffix = gpay_suffix_dict
        elif (win.fastagUPI.isChecked()):
            self.suffix = fastag_suffix_dict
        elif (win.mobileUPI.isChecked()):
            self.suffix = mobile_suffix_dict
        self.thread.start()

class add_API(QDialog):
    def ok_clicked(self):
        print(self.api_input.text())
        self.close()
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("UI/api_input.ui", self)
        self.api_input = self.findChild(QLineEdit, "lineEdit")
        self.button_box = self.findChild(QDialogButtonBox, "buttonBox")
        self.ok = self.button_box.buttons()[0]
        self.ok.clicked.connect(self.ok_clicked)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())