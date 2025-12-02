# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_actualizarPasaj.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(446, 329)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 110, 361, 112))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)

        self.verticalLayout_2.addWidget(self.label_4)

        self.lineEdit_nombrePasajero = QLineEdit(self.layoutWidget)
        self.lineEdit_nombrePasajero.setObjectName(u"lineEdit_nombrePasajero")
        self.lineEdit_nombrePasajero.setMaxLength(30)

        self.verticalLayout_2.addWidget(self.lineEdit_nombrePasajero)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.verticalLayout_24.addWidget(self.label_8)

        self.lineEdit_correoPasajero = QLineEdit(self.layoutWidget)
        self.lineEdit_correoPasajero.setObjectName(u"lineEdit_correoPasajero")
        self.lineEdit_correoPasajero.setMaxLength(40)

        self.verticalLayout_24.addWidget(self.lineEdit_correoPasajero)


        self.horizontalLayout_3.addLayout(self.verticalLayout_24)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.verticalLayout_25.addWidget(self.label_9)

        self.lineEdit_telefonoPasajero = QLineEdit(self.layoutWidget)
        self.lineEdit_telefonoPasajero.setObjectName(u"lineEdit_telefonoPasajero")
        self.lineEdit_telefonoPasajero.setMaxLength(10)

        self.verticalLayout_25.addWidget(self.lineEdit_telefonoPasajero)


        self.horizontalLayout_3.addLayout(self.verticalLayout_25)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 0, 511, 81))
        font1 = QFont()
        font1.setPointSize(27)
        font1.setBold(True)
        self.label_3.setFont(font1)
        self.boton_actualizar = QPushButton(Form)
        self.boton_actualizar.setObjectName(u"boton_actualizar")
        self.boton_actualizar.setGeometry(QRect(240, 290, 91, 31))
        font2 = QFont()
        font2.setBold(True)
        self.boton_actualizar.setFont(font2)
        self.boton_actualizar.setStyleSheet(u"QPushButton{\n"
"	background: #1061C4;\n"
"	color:WHITE;\n"
"	border:none;\n"
"	border-radius: 6px;\n"
"	font-weight: bold;\n"
"	font-size:15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0D4FAB;    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0A3F8A;     \n"
"}")
        self.boton_cancelar = QPushButton(Form)
        self.boton_cancelar.setObjectName(u"boton_cancelar")
        self.boton_cancelar.setGeometry(QRect(340, 290, 91, 31))
        self.boton_cancelar.setFont(font2)
        self.boton_cancelar.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(237, 51, 59);\n"
"	color:WHITE;\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(191, 41, 49);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background-color: rgb(141, 30, 36);\n"
"}")
        self.line_2 = QFrame(Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(-20, 80, 741, 20))
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Nombre (s)", None))
        self.lineEdit_nombrePasajero.setText(QCoreApplication.translate("Form", u"Leonardo Ivan", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Correo electr\u00f3nico", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"N\u00famero telef\u00f3nico", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Actualizar pasajero", None))
        self.boton_actualizar.setText(QCoreApplication.translate("Form", u"Actualizar", None))
        self.boton_cancelar.setText(QCoreApplication.translate("Form", u"Cancelar", None))
    # retranslateUi

