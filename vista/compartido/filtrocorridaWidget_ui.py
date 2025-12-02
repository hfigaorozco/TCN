# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'filtrocorridaWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_pagina_compraboleto(object):
    def setupUi(self, pagina_compraboleto):
        if not pagina_compraboleto.objectName():
            pagina_compraboleto.setObjectName(u"pagina_compraboleto")
        pagina_compraboleto.resize(1280, 670)
        pagina_compraboleto.setMinimumSize(QSize(1280, 670))
        pagina_compraboleto.setMaximumSize(QSize(1280, 670))
        pagina_compraboleto.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_imagen_logo = QLabel(pagina_compraboleto)
        self.label_imagen_logo.setObjectName(u"label_imagen_logo")
        self.label_imagen_logo.setGeometry(QRect(460, 20, 351, 111))
        self.label_imagen_logo.setMinimumSize(QSize(261, 71))
        font = QFont()
        font.setPointSize(25)
        self.label_imagen_logo.setFont(font)
        self.label_imagen_logo.setStyleSheet(u"")
        self.label_imagen_logo.setPixmap(QPixmap(u"../../../x/recursos/recursos_empresa/logo.png"))
        self.label_imagen_logo.setScaledContents(True)
        self.comboBox_origen = QComboBox(pagina_compraboleto)
        self.comboBox_origen.setObjectName(u"comboBox_origen")
        self.comboBox_origen.setGeometry(QRect(120, 160, 231, 61))
        self.comboBox_origen.setStyleSheet(u"QComboBox {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #dcdfe6;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-size: 35px;\n"
"    color: #1061C4;\n"
"    min-height: 18px;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border-color: #c0c4cc;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border-color: #409eff;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"    width: 25px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: none;\n"
"    border-left: 4px solid transparent;\n"
"    border-right: 4px solid transparent;\n"
"    border-top: 4px solid #909399;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #dcdfe6;\n"
"    border-radius: 6px;\n"
"    background-color: white;\n"
"    outline: none;\n"
"    selection-background-color: #409eff;\n"
"    selection-color: white;\n"
"    /* ELIMINA CUALQUIER cursor: ...; DE AQU\u00cd */\n"
"}")
        self.comboBox_destino = QComboBox(pagina_compraboleto)
        self.comboBox_destino.setObjectName(u"comboBox_destino")
        self.comboBox_destino.setGeometry(QRect(400, 160, 231, 61))
        self.comboBox_destino.setStyleSheet(u"QComboBox {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #dcdfe6;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-size: 35px;\n"
"    color: #1061C4;\n"
"    min-height: 18px;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border-color: #c0c4cc;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border-color: #409eff;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"    width: 25px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: none;\n"
"    border-left: 4px solid transparent;\n"
"    border-right: 4px solid transparent;\n"
"    border-top: 4px solid #909399;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #dcdfe6;\n"
"    border-radius: 6px;\n"
"    background-color: white;\n"
"    outline: none;\n"
"    selection-background-color: #409eff;\n"
"    selection-color: white;\n"
"    /* ELIMINA CUALQUIER cursor: ...; DE AQU\u00cd */\n"
"}")
        self.comboBox_fecha = QComboBox(pagina_compraboleto)
        self.comboBox_fecha.setObjectName(u"comboBox_fecha")
        self.comboBox_fecha.setGeometry(QRect(680, 160, 231, 61))
        self.comboBox_fecha.setStyleSheet(u"QComboBox {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #dcdfe6;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-size: 35px;\n"
"    color: #1061C4;\n"
"    min-height: 18px;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border-color: #c0c4cc;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border-color: #409eff;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"    width: 25px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: none;\n"
"    border-left: 4px solid transparent;\n"
"    border-right: 4px solid transparent;\n"
"    border-top: 4px solid #909399;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #dcdfe6;\n"
"    border-radius: 6px;\n"
"    background-color: white;\n"
"    outline: none;\n"
"    selection-background-color: #409eff;\n"
"    selection-color: white;\n"
"    /* ELIMINA CUALQUIER cursor: ...; DE AQU\u00cd */\n"
"}")
        self.tableWidget_corridas = QTableWidget(pagina_compraboleto)
        if (self.tableWidget_corridas.columnCount() < 5):
            self.tableWidget_corridas.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_corridas.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_corridas.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_corridas.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_corridas.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_corridas.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget_corridas.setObjectName(u"tableWidget_corridas")
        self.tableWidget_corridas.setGeometry(QRect(190, 250, 901, 321))
        self.tableWidget_corridas.setStyleSheet(u"QTableView {\n"
"    background: #ffffff;\n"
"    border: 2px solid #e6e8ec;\n"
"    border-radius: 8px;\n"
"    gridline-color: #f1f1f3;\n"
"    selection-background-color: #e8f0fe;\n"
"    selection-color: #1a1a1a;\n"
"    font-size: 18px;\n"
"    color: #333;\n"
"    alternate-background-color: #fafbff;\n"
"    show-grid: false;\n"
"}\n"
"\n"
"QTableView::item {\n"
"    padding: 8px 12px;\n"
"    border: 0px;\n"
"}\n"
"\n"
"QTableView::item:hover {\n"
"    background: #f5f8ff;\n"
"}\n"
"\n"
"QTableView::item:selected {\n"
"    background: #e2edff;\n"
"    color: #1a1a1a;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background: #ffffff;\n"
"    color: #6b7280;\n"
"    padding: 10px 12px;\n"
"    border: 0;\n"
"    border-bottom: 2px solid #e6e8ec;\n"
"    font-size: 20px;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QHeaderView::section:hover {\n"
"    background: #f7f9fc;\n"
"}\n"
"\n"
"QHeaderView {\n"
"    background: #ffffff;\n"
"    border: 0;\n"
"}\n"
"\n"
"QTableView::indicator {\n"
"    width: 18px;\n"
""
                        "    height: 18px;\n"
"}\n"
"\n"
"QHeaderView::section:first {\n"
"    border-top-left-radius: 15px;\n"
"}\n"
"\n"
"QHeaderView::section:last {\n"
"    border-top-right-radius: 15px;\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical {\n"
"    background: transparent;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #cfd3da;\n"
"    min-height: 25px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #b5bac4;\n"
"}\n"
"\n"
"QScrollBar::add-line,\n"
"QScrollBar::sub-line {\n"
"    background: none;\n"
"    height: 0px;\n"
"}\n"
"")
        self.tableWidget_corridas.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_corridas.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_corridas.horizontalHeader().setDefaultSectionSize(180)
        self.tableWidget_corridas.verticalHeader().setHighlightSections(True)
        self.LineEdit_pasajeros = QLineEdit(pagina_compraboleto)
        self.LineEdit_pasajeros.setObjectName(u"LineEdit_pasajeros")
        self.LineEdit_pasajeros.setGeometry(QRect(960, 160, 231, 61))
        self.LineEdit_pasajeros.setStyleSheet(u"QLineEdit {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #dcdfe6;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-size: 35px;\n"
"    color: #1061C4;\n"
"    min-height: 18px;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border-color: #c0c4cc;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: #409eff;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #f5f7fa;\n"
"    color: #c0c4cc;\n"
"    border-color: #e4e7ed;\n"
"}\n"
"\n"
"QLineEdit:read-only {\n"
"    background-color: #f5f7fa;\n"
"    color: #909399;\n"
"}")
        self.boton_cancelar = QPushButton(pagina_compraboleto)
        self.boton_cancelar.setObjectName(u"boton_cancelar")
        self.boton_cancelar.setGeometry(QRect(880, 600, 171, 41))
        font1 = QFont()
        font1.setBold(True)
        self.boton_cancelar.setFont(font1)
        self.boton_cancelar.setStyleSheet(u"QPushButton{\n"
"	background: #FF6A36;\n"
"	color:WHITE;\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 20px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #E85F30;   /* Naranja m\u00e1s oscuro */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #CC532A;   /* M\u00e1s oscuro para click */\n"
"}")
        self.boton_agregar = QPushButton(pagina_compraboleto)
        self.boton_agregar.setObjectName(u"boton_agregar")
        self.boton_agregar.setGeometry(QRect(1070, 600, 171, 41))
        self.boton_agregar.setFont(font1)
        self.boton_agregar.setStyleSheet(u"QPushButton{\n"
"	background: #1061C4;\n"
"	color:WHITE;\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 20px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #0D4FAB;    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0A3F8A;     \n"
"}")

        self.retranslateUi(pagina_compraboleto)

        QMetaObject.connectSlotsByName(pagina_compraboleto)
    # setupUi

    def retranslateUi(self, pagina_compraboleto):
        pagina_compraboleto.setWindowTitle("")
        self.label_imagen_logo.setText("")
        self.comboBox_origen.setPlaceholderText(QCoreApplication.translate("pagina_compraboleto", u"Origen", None))
        self.comboBox_destino.setPlaceholderText(QCoreApplication.translate("pagina_compraboleto", u"Destino", None))
        self.comboBox_fecha.setPlaceholderText(QCoreApplication.translate("pagina_compraboleto", u"Fecha", None))
        ___qtablewidgetitem = self.tableWidget_corridas.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("pagina_compraboleto", u"Servicio", None));
        ___qtablewidgetitem1 = self.tableWidget_corridas.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("pagina_compraboleto", u"Hora", None));
        ___qtablewidgetitem2 = self.tableWidget_corridas.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("pagina_compraboleto", u"Origen", None));
        ___qtablewidgetitem3 = self.tableWidget_corridas.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("pagina_compraboleto", u"Destino", None));
        ___qtablewidgetitem4 = self.tableWidget_corridas.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("pagina_compraboleto", u"Precio", None));
        self.LineEdit_pasajeros.setText("")
        self.LineEdit_pasajeros.setPlaceholderText(QCoreApplication.translate("pagina_compraboleto", u"Pasajeros", None))
        self.boton_cancelar.setText(QCoreApplication.translate("pagina_compraboleto", u"Cancelar", None))
        self.boton_agregar.setText(QCoreApplication.translate("pagina_compraboleto", u"Aceptar", None))
    # retranslateUi

