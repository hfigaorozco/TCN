# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'actualizarCorrEstadoDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 150)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 360, 30))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.pushButton_cerrar = QPushButton(Dialog)
        self.pushButton_cerrar.setObjectName(u"pushButton_cerrar")
        self.pushButton_cerrar.setGeometry(QRect(150, 90, 100, 30))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Actualizar Estado Corrida", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Este es el di\u00e1logo para actualizar el estado.", None))
        self.pushButton_cerrar.setText(QCoreApplication.translate("Dialog", u"Cerrar", None))
    # retranslateUi

