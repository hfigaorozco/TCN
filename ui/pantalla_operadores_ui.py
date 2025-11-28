# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pantalla_operadores.ui'
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
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1916, 1084)
        Form.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.header_widget = QWidget(Form)
        self.header_widget.setObjectName(u"header_widget")
        self.header_widget.setGeometry(QRect(-10, 0, 1951, 111))
        self.header_widget.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border-bottom: 1px solid #E3E3E3;")
        self.boton_rutas = QPushButton(self.header_widget)
        self.boton_rutas.setObjectName(u"boton_rutas")
        self.boton_rutas.setGeometry(QRect(1140, 20, 221, 71))
        font = QFont()
        font.setBold(True)
        self.boton_rutas.setFont(font)
        self.boton_rutas.setStyleSheet(u"QPushButton{\n"
"	background: #1061C4;\n"
"	color:WHITE;\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size:25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0D4FAB;    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0A3F8A;     \n"
"}")
        icon = QIcon()
        icon.addFile(u":/recursos/iconsEmpresa/entrega.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_rutas.setIcon(icon)
        self.boton_rutas.setIconSize(QSize(30, 30))
        self.boton_corridas = QPushButton(self.header_widget)
        self.boton_corridas.setObjectName(u"boton_corridas")
        self.boton_corridas.setGeometry(QRect(640, 20, 221, 71))
        self.boton_corridas.setFont(font)
        self.boton_corridas.setStyleSheet(u"QPushButton{\n"
"	background: #1061C4;\n"
"	color:WHITE;\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0D4FAB;    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0A3F8A;     \n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/recursos/iconsCliente/calendario.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_corridas.setIcon(icon1)
        self.boton_corridas.setIconSize(QSize(30, 30))
        self.boton_operadores = QPushButton(self.header_widget)
        self.boton_operadores.setObjectName(u"boton_operadores")
        self.boton_operadores.setGeometry(QRect(1390, 20, 221, 71))
        self.boton_operadores.setFont(font)
        self.boton_operadores.setStyleSheet(u"QPushButton{\n"
"	background: #1061C4;\n"
"	color:WHITE;\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0D4FAB;    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0A3F8A;     \n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/recursos/iconsEmpresa/conductor.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_operadores.setIcon(icon2)
        self.boton_operadores.setIconSize(QSize(30, 30))
        self.boton_autobuses = QPushButton(self.header_widget)
        self.boton_autobuses.setObjectName(u"boton_autobuses")
        self.boton_autobuses.setGeometry(QRect(890, 20, 221, 71))
        self.boton_autobuses.setFont(font)
        self.boton_autobuses.setStyleSheet(u"QPushButton{\n"
"	background: #1061C4;\n"
"	color:WHITE;\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0D4FAB;    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0A3F8A;     \n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/recursos/iconsCliente/autobus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_autobuses.setIcon(icon3)
        self.boton_autobuses.setIconSize(QSize(30, 30))
        self.boton_inicio = QPushButton(self.header_widget)
        self.boton_inicio.setObjectName(u"boton_inicio")
        self.boton_inicio.setGeometry(QRect(270, 20, 91, 71))
        self.boton_inicio.setFont(font)
        self.boton_inicio.setStyleSheet(u"QPushButton{\n"
"	background: #1061C4;\n"
"	color:WHITE;\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0D4FAB;    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0A3F8A;     \n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/recursos/iconsEmpresa/casa-silueta-negra-sin-puerta.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_inicio.setIcon(icon4)
        self.boton_inicio.setIconSize(QSize(30, 30))
        self.boton_reservaciones = QPushButton(self.header_widget)
        self.boton_reservaciones.setObjectName(u"boton_reservaciones")
        self.boton_reservaciones.setGeometry(QRect(390, 20, 221, 71))
        self.boton_reservaciones.setFont(font)
        self.boton_reservaciones.setStyleSheet(u"QPushButton{\n"
"	background: #1061C4;\n"
"	color:WHITE;\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0D4FAB;    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0A3F8A;     \n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/recursos/iconsEmpresa/boleto.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_reservaciones.setIcon(icon5)
        self.boton_reservaciones.setIconSize(QSize(30, 30))
        self.boton_salir = QPushButton(self.header_widget)
        self.boton_salir.setObjectName(u"boton_salir")
        self.boton_salir.setGeometry(QRect(1640, 20, 91, 71))
        self.boton_salir.setFont(font)
        self.boton_salir.setStyleSheet(u"QPushButton{\n"
"	background: #1061C4;\n"
"	color:WHITE;\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0D4FAB;    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0A3F8A;     \n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/recursos/iconsEmpresa/cerrar-sesion.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_salir.setIcon(icon6)
        self.boton_salir.setIconSize(QSize(30, 30))
        self.widget_opbotones_6 = QWidget(Form)
        self.widget_opbotones_6.setObjectName(u"widget_opbotones_6")
        self.widget_opbotones_6.setGeometry(QRect(20, 140, 221, 881))
        self.widget_opbotones_6.setStyleSheet(u"\n"
"\n"
"background-color: #1061C4;\n"
"border: 1px solid #dcdfe6;\n"
"border-radius: 15px;\n"
"gridline-color: #e0e0e0;\n"
"outline: none;\n"
"color: #606266;\n"
"\n"
"")
        self.boton_editaroperadores = QPushButton(self.widget_opbotones_6)
        self.boton_editaroperadores.setObjectName(u"boton_editaroperadores")
        self.boton_editaroperadores.setGeometry(QRect(10, 90, 201, 71))
        self.boton_editaroperadores.setFont(font)
        self.boton_editaroperadores.setStyleSheet(u"QPushButton{\n"
"	background: #1061C4;\n"
"	color:WHITE;\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0D4FAB;    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0A3F8A;     \n"
"}")
        self.boton_editaroperadores.setIconSize(QSize(30, 30))
        self.boton_agregaroperadores = QPushButton(self.widget_opbotones_6)
        self.boton_agregaroperadores.setObjectName(u"boton_agregaroperadores")
        self.boton_agregaroperadores.setGeometry(QRect(10, 10, 201, 71))
        self.boton_agregaroperadores.setFont(font)
        self.boton_agregaroperadores.setStyleSheet(u"QPushButton{\n"
"	background: #1061C4;\n"
"	color:WHITE;\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0D4FAB;    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0A3F8A;     \n"
"}")
        self.boton_agregaroperadores.setIconSize(QSize(30, 30))
        self.widget_titulo = QWidget(Form)
        self.widget_titulo.setObjectName(u"widget_titulo")
        self.widget_titulo.setGeometry(QRect(270, 140, 1621, 101))
        self.widget_titulo.setStyleSheet(u"background-color: #ffffff;\n"
"border: 2px solid #dcdfe6;\n"
"border-radius: 15px;\n"
"gridline-color: #e0e0e0;\n"
"outline: none;\n"
"color: #606266;\n"
"border-radius: 15px;\n"
"border-bottom: 1px solid #E3E3E3;\n"
"\n"
"")
        self.label_estatico_operadores = QLabel(self.widget_titulo)
        self.label_estatico_operadores.setObjectName(u"label_estatico_operadores")
        self.label_estatico_operadores.setGeometry(QRect(30, 10, 461, 71))
        font1 = QFont()
        font1.setPointSize(59)
        font1.setBold(True)
        font1.setItalic(True)
        self.label_estatico_operadores.setFont(font1)
        self.label_estatico_operadores.setStyleSheet(u"border:none\n"
"\n"
"")
        self.label_estatico_fitrorigen = QLabel(self.widget_titulo)
        self.label_estatico_fitrorigen.setObjectName(u"label_estatico_fitrorigen")
        self.label_estatico_fitrorigen.setGeometry(QRect(1220, 10, 179, 40))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.label_estatico_fitrorigen.setFont(font2)
        self.label_estatico_fitrorigen.setStyleSheet(u"border:none;\n"
"\n"
"\n"
"")
        self.label_estatico_fitrorigen.setAlignment(Qt.AlignCenter)
        self.ComboBox_filtrorigen = QComboBox(self.widget_titulo)
        self.ComboBox_filtrorigen.addItem("")
        self.ComboBox_filtrorigen.addItem("")
        self.ComboBox_filtrorigen.addItem("")
        self.ComboBox_filtrorigen.addItem("")
        self.ComboBox_filtrorigen.addItem("")
        self.ComboBox_filtrorigen.addItem("")
        self.ComboBox_filtrorigen.addItem("")
        self.ComboBox_filtrorigen.setObjectName(u"ComboBox_filtrorigen")
        self.ComboBox_filtrorigen.setGeometry(QRect(1220, 50, 179, 33))
        self.ComboBox_filtrorigen.setStyleSheet(u"\n"
"QComboBox {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #dcdfe6;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-size: 13px;\n"
"    color: #606266;\n"
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
"}\n"
"")
        self.label_estatico_filtrodestino = QLabel(self.widget_titulo)
        self.label_estatico_filtrodestino.setObjectName(u"label_estatico_filtrodestino")
        self.label_estatico_filtrodestino.setGeometry(QRect(1430, 10, 179, 40))
        self.label_estatico_filtrodestino.setFont(font2)
        self.label_estatico_filtrodestino.setStyleSheet(u"border:none;\n"
"\n"
"\n"
"")
        self.label_estatico_filtrodestino.setAlignment(Qt.AlignCenter)
        self.ComboBox_filtrodestino = QComboBox(self.widget_titulo)
        self.ComboBox_filtrodestino.addItem("")
        self.ComboBox_filtrodestino.addItem("")
        self.ComboBox_filtrodestino.addItem("")
        self.ComboBox_filtrodestino.addItem("")
        self.ComboBox_filtrodestino.addItem("")
        self.ComboBox_filtrodestino.addItem("")
        self.ComboBox_filtrodestino.addItem("")
        self.ComboBox_filtrodestino.setObjectName(u"ComboBox_filtrodestino")
        self.ComboBox_filtrodestino.setGeometry(QRect(1430, 50, 179, 33))
        self.ComboBox_filtrodestino.setStyleSheet(u"\n"
"QComboBox {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #dcdfe6;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font-size: 13px;\n"
"    color: #606266;\n"
"    min-height: 10px;\n"
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
"}\n"
"")
        self.o_tableWidget = QTableWidget(Form)
        if (self.o_tableWidget.columnCount() < 5):
            self.o_tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.o_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.o_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.o_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        self.o_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font);
        self.o_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.o_tableWidget.setObjectName(u"o_tableWidget")
        self.o_tableWidget.setGeometry(QRect(360, 280, 1421, 661))
        self.o_tableWidget.setLayoutDirection(Qt.LeftToRight)
        self.o_tableWidget.setStyleSheet(u"QTableView {\n"
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
        self.o_tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.o_tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.o_tableWidget.horizontalHeader().setDefaultSectionSize(284)
        self.o_tableWidget.verticalHeader().setVisible(False)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.boton_rutas.setText(QCoreApplication.translate("Form", u"Rutas", None))
        self.boton_corridas.setText(QCoreApplication.translate("Form", u"Corridas", None))
        self.boton_operadores.setText(QCoreApplication.translate("Form", u"Operadores", None))
        self.boton_autobuses.setText(QCoreApplication.translate("Form", u"Autobuses", None))
        self.boton_inicio.setText("")
        self.boton_reservaciones.setText(QCoreApplication.translate("Form", u"Reservaciones", None))
        self.boton_salir.setText("")
        self.boton_editaroperadores.setText(QCoreApplication.translate("Form", u"editar", None))
        self.boton_agregaroperadores.setText(QCoreApplication.translate("Form", u"A\u00f1adir", None))
        self.label_estatico_operadores.setText(QCoreApplication.translate("Form", u"Operadores", None))
        self.label_estatico_fitrorigen.setText(QCoreApplication.translate("Form", u"Filtrar por origen", None))
        self.ComboBox_filtrorigen.setItemText(0, QCoreApplication.translate("Form", u"Todos", None))
        self.ComboBox_filtrorigen.setItemText(1, QCoreApplication.translate("Form", u"Tijuana", None))
        self.ComboBox_filtrorigen.setItemText(2, QCoreApplication.translate("Form", u"Mexicali", None))
        self.ComboBox_filtrorigen.setItemText(3, QCoreApplication.translate("Form", u"Ensenada", None))
        self.ComboBox_filtrorigen.setItemText(4, QCoreApplication.translate("Form", u"San Felipe", None))
        self.ComboBox_filtrorigen.setItemText(5, QCoreApplication.translate("Form", u"Tecate", None))
        self.ComboBox_filtrorigen.setItemText(6, QCoreApplication.translate("Form", u"San Quintin", None))

        self.label_estatico_filtrodestino.setText(QCoreApplication.translate("Form", u"Filtrar por destino", None))
        self.ComboBox_filtrodestino.setItemText(0, QCoreApplication.translate("Form", u"Todos", None))
        self.ComboBox_filtrodestino.setItemText(1, QCoreApplication.translate("Form", u"Tijuana", None))
        self.ComboBox_filtrodestino.setItemText(2, QCoreApplication.translate("Form", u"Mexicali", None))
        self.ComboBox_filtrodestino.setItemText(3, QCoreApplication.translate("Form", u"Ensenada", None))
        self.ComboBox_filtrodestino.setItemText(4, QCoreApplication.translate("Form", u"San Felipe", None))
        self.ComboBox_filtrodestino.setItemText(5, QCoreApplication.translate("Form", u"Tecate", None))
        self.ComboBox_filtrodestino.setItemText(6, QCoreApplication.translate("Form", u"San Quintin", None))

        ___qtablewidgetitem = self.o_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Num", None));
        ___qtablewidgetitem1 = self.o_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Nombre", None));
        ___qtablewidgetitem2 = self.o_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Fecha de nacimiento", None));
        ___qtablewidgetitem3 = self.o_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Tel\u00e9fono", None));
        ___qtablewidgetitem4 = self.o_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Fecha de contrato", None));
    # retranslateUi

