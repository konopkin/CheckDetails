# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CheckDet.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5.QtWidgets import QPushButton, QWidget, QLineEdit, QSpinBox, QLabel, QTextEdit, QMenuBar, QMenu, QStatusBar, QAction
from PyQt5.QtCore import QRect, QMetaObject, QCoreApplication, Qt
from PyQt5.QtGui import QCursor

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(497, 600)
        MainWindow.setContextMenuPolicy(Qt.NoContextMenu)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_start = QPushButton(self.centralwidget)
        self.pushButton_start.setGeometry(QRect(10, 120, 131, 23))
        self.pushButton_start.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_start.setContextMenuPolicy(Qt.NoContextMenu)
        self.pushButton_start.setObjectName("pushButton_start")

        self.pushButton_SaveDB = QPushButton(self.centralwidget)
        self.pushButton_SaveDB.setGeometry(QRect(10, 430, 131, 23))
        self.pushButton_SaveDB.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_SaveDB.setContextMenuPolicy(Qt.NoContextMenu)
        self.pushButton_SaveDB.setObjectName("pushButton_SaveDB")
        self.pushButton_FindDB = QPushButton(self.centralwidget)
        self.pushButton_FindDB.setGeometry(QRect(10, 500, 131, 23))
        self.pushButton_FindDB.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_FindDB.setContextMenuPolicy(Qt.NoContextMenu)
        self.pushButton_FindDB.setObjectName("pushButton_FindDB")

        self.pushButton_SubtractDB = QPushButton(self.centralwidget)
        self.pushButton_SubtractDB.setGeometry(QRect(10, 470, 131, 23))
        self.pushButton_SubtractDB.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_SubtractDB.setContextMenuPolicy(Qt.NoContextMenu)
        self.pushButton_SubtractDB.setObjectName("pushButton_FindDB")

        self.lineEdit_price = QLineEdit(self.centralwidget)
        self.lineEdit_price.setGeometry(QRect(10, 330, 131, 20))
        self.lineEdit_price.setAutoFillBackground(False)
        self.lineEdit_price.setText("")
        self.lineEdit_price.setClearButtonEnabled(False)
        self.lineEdit_price.setObjectName("lineEdit_price")

        self.spin_count = QSpinBox(self.centralwidget)
        self.spin_count.setGeometry(QRect(10, 390, 71, 22))


        self.lineEdit_partNumber = QLineEdit(self.centralwidget)
        self.lineEdit_partNumber.setGeometry(QRect(10, 70, 131, 20))
        self.lineEdit_partNumber.setAutoFillBackground(False)
        self.lineEdit_partNumber.setText("")
        self.lineEdit_partNumber.setClearButtonEnabled(False)
        self.lineEdit_partNumber.setObjectName("lineEdit_partNumber")
        self.label_count = QLabel(self.centralwidget)
        self.label_count.setGeometry(QRect(10, 370, 71, 16))
        self.label_count.setObjectName("label_count")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QRect(150, 0, 311, 541))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.pushButton_openInBrowser = QPushButton(self.centralwidget)
        self.pushButton_openInBrowser.setGeometry(QRect(10, 180, 131, 23))
        self.pushButton_openInBrowser.setObjectName("pushButton_openInBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 497, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QAction(MainWindow)
        self.action.setObjectName("action")
        self.menu.addAction(self.action)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Check Details"))
        self.pushButton_start.setText(_translate("MainWindow", "Поиск"))
        self.pushButton_SaveDB.setText(_translate("MainWindow", "Добавить в базу"))
        self.pushButton_FindDB.setText(_translate("MainWindow", "Найти в базе"))
        self.pushButton_SubtractDB.setText(_translate("MainWindow", "Вычесть из базы"))
        self.lineEdit_price.setPlaceholderText(_translate("MainWindow","Цена"))
        self.lineEdit_partNumber.setPlaceholderText(_translate("MainWindow", "Part Number"))
        self.label_count.setText(_translate("MainWindow", "Количество"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "Information about detail"))
        self.pushButton_openInBrowser.setText(_translate("MainWindow", "Open link"))
        self.menu.setTitle(_translate("MainWindow", "Меню"))
        self.action.setText(_translate("MainWindow", "О программе"))
