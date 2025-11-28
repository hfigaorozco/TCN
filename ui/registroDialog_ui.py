# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registroDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)
import resources_rc
import resources_rc
import resources_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(900, 700)
        Dialog.setMaximumSize(QSize(900, 700))
        Dialog.setSizeIncrement(QSize(900, 700))
        Dialog.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_estatico_yatienescuenta = QLabel(Dialog)
        self.label_estatico_yatienescuenta.setObjectName(u"label_estatico_yatienescuenta")
        self.label_estatico_yatienescuenta.setGeometry(QRect(480, 630, 171, 21))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(False)
        self.label_estatico_yatienescuenta.setFont(font)
        self.lineEdit_contrasena = QLineEdit(Dialog)
        self.lineEdit_contrasena.setObjectName(u"lineEdit_contrasena")
        self.lineEdit_contrasena.setGeometry(QRect(480, 400, 391, 32))
        self.lineEdit_contrasena.setMinimumSize(QSize(0, 32))
        self.lineEdit_contrasena.setMaximumSize(QSize(16777215, 24))
        font1 = QFont()
        self.lineEdit_contrasena.setFont(font1)
        self.lineEdit_contrasena.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(246, 245, 244);\n"
"    border: 1px solid #dcdfe6;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-size: 20px;\n"
"    color: #606266;\n"
"    min-height: 18px;\n"
"}\n"
"")
        self.lineEdit_contrasena.setEchoMode(QLineEdit.Password)
        self.boton_continuar = QPushButton(Dialog)
        self.boton_continuar.setObjectName(u"boton_continuar")
        self.boton_continuar.setGeometry(QRect(550, 487, 261, 51))
        font2 = QFont()
        font2.setBold(True)
        self.boton_continuar.setFont(font2)
        self.boton_continuar.setStyleSheet(u"QPushButton{\n"
"	background: #1061C4;\n"
"	color:WHITE;\n"
"	border:none;\n"
"	border-radius: 15px;\n"
"	font-weight: bold;\n"
"	font-size: 22px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #0D4FAB;    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0A3F8A;     \n"
"}")
        self.lineEdit_telefono = QLineEdit(Dialog)
        self.lineEdit_telefono.setObjectName(u"lineEdit_telefono")
        self.lineEdit_telefono.setGeometry(QRect(480, 310, 391, 32))
        self.lineEdit_telefono.setMinimumSize(QSize(0, 32))
        self.lineEdit_telefono.setMaximumSize(QSize(16777215, 24))
        self.lineEdit_telefono.setFont(font1)
        self.lineEdit_telefono.setStyleSheet(u"QLineEdit {\n"
"    \n"
"	background-color: rgb(246, 245, 244);\n"
"    border: 1px solid #dcdfe6;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-size: 20px;\n"
"    color: #606266;\n"
"    min-height: 18px;\n"
"}\n"
"\n"
"")
        self.label_estatico_registrotxt = QLabel(Dialog)
        self.label_estatico_registrotxt.setObjectName(u"label_estatico_registrotxt")
        self.label_estatico_registrotxt.setGeometry(QRect(480, 160, 401, 81))
        font3 = QFont()
        font3.setPointSize(13)
        self.label_estatico_registrotxt.setFont(font3)
        self.label_estatico_registrotxt.setWordWrap(True)
        self.pushButton_estatico_identificate = QPushButton(Dialog)
        self.pushButton_estatico_identificate.setObjectName(u"pushButton_estatico_identificate")
        self.pushButton_estatico_identificate.setGeometry(QRect(660, 620, 111, 31))
        self.pushButton_estatico_identificate.setFont(font2)
        self.pushButton_estatico_identificate.setStyleSheet(u"QPushButton{\n"
"	background: white;\n"
"	color:#1061C4;\n"
"	border: 2px solid #1061C4;\n"
"	border-radius: 15px;\n"
"	font-weight: bold;\n"
"	font-size: 15px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #0D4FAB;    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0A3F8A;     \n"
"}")
        self.label_imagen_registro = QLabel(Dialog)
        self.label_imagen_registro.setObjectName(u"label_imagen_registro")
        self.label_imagen_registro.setGeometry(QRect(0, -10, 451, 721))
        self.label_imagen_registro.setPixmap(QPixmap(u":/recursos/iconsEmpresa/image(4).png"))
        self.label_estatico_registro = QLabel(Dialog)
        self.label_estatico_registro.setObjectName(u"label_estatico_registro")
        self.label_estatico_registro.setGeometry(QRect(480, 110, 401, 51))
        font4 = QFont()
        font4.setPointSize(25)
        font4.setBold(True)
        self.label_estatico_registro.setFont(font4)
        self.label_estatico_registro.setAlignment(Qt.AlignCenter)
        self.label_estatico_telefono = QLabel(Dialog)
        self.label_estatico_telefono.setObjectName(u"label_estatico_telefono")
        self.label_estatico_telefono.setGeometry(QRect(480, 271, 111, 31))
        font5 = QFont()
        font5.setPointSize(18)
        self.label_estatico_telefono.setFont(font5)
        self.label_estatico_contrasena = QLabel(Dialog)
        self.label_estatico_contrasena.setObjectName(u"label_estatico_contrasena")
        self.label_estatico_contrasena.setGeometry(QRect(480, 360, 141, 31))
        self.label_estatico_contrasena.setFont(font5)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_estatico_yatienescuenta.setText(QCoreApplication.translate("Dialog", u"\u00bfYa tienes una cuenta?", None))
        self.lineEdit_contrasena.setInputMask("")
        self.boton_continuar.setText(QCoreApplication.translate("Dialog", u"Continuar", None))
        self.lineEdit_telefono.setInputMask(QCoreApplication.translate("Dialog", u"9999999999", None))
        self.lineEdit_telefono.setText("")
        self.label_estatico_registrotxt.setText(QCoreApplication.translate("Dialog", u"Registrate para comprar tus boletos y gestionar tus reservaciones de forma rapida rapida", None))
        self.pushButton_estatico_identificate.setText(QCoreApplication.translate("Dialog", u"Identificate", None))
        self.label_imagen_registro.setText("")
        self.label_estatico_registro.setText(QCoreApplication.translate("Dialog", u"Registro", None))
        self.label_estatico_telefono.setText(QCoreApplication.translate("Dialog", u"Tel\u00e9fono:", None))
        self.label_estatico_contrasena.setText(QCoreApplication.translate("Dialog", u"Contrase\u00f1a:", None))
    # retranslateUi

