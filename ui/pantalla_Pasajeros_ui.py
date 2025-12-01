# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pantalla_Pasajeros.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1920, 1080)
        self.QtableWidget_pasajeros = QTableWidget(Form)
        if (self.QtableWidget_pasajeros.columnCount() < 6):
            self.QtableWidget_pasajeros.setColumnCount(6)
        font = QFont()
        font.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.QtableWidget_pasajeros.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.QtableWidget_pasajeros.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.QtableWidget_pasajeros.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        self.QtableWidget_pasajeros.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font);
        self.QtableWidget_pasajeros.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font);
        self.QtableWidget_pasajeros.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.QtableWidget_pasajeros.setObjectName(u"QtableWidget_pasajeros")
        self.QtableWidget_pasajeros.setGeometry(QRect(240, 240, 1641, 751))
        self.QtableWidget_pasajeros.setFont(font)
        self.QtableWidget_pasajeros.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.QtableWidget_pasajeros.setStyleSheet(u"QTableView {\n"
"    background: #ffffff;\n"
"    border: 1px solid #e6e8ec;\n"
"    border-radius: 8px;\n"
"    gridline-color: #f1f1f3;\n"
"    selection-background-color: #e8f0fe;\n"
"    selection-color: #1a1a1a;\n"
"    font-size: 14px;\n"
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
"    font-size: 17px;\n"
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
        self.QtableWidget_pasajeros.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.QtableWidget_pasajeros.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.QtableWidget_pasajeros.horizontalHeader().setVisible(True)
        self.QtableWidget_pasajeros.horizontalHeader().setCascadingSectionResizes(True)
        self.QtableWidget_pasajeros.horizontalHeader().setDefaultSectionSize(273)
        self.QtableWidget_pasajeros.horizontalHeader().setHighlightSections(False)
        self.QtableWidget_pasajeros.verticalHeader().setCascadingSectionResizes(True)
        self.header_pasajeros = QWidget(Form)
        self.header_pasajeros.setObjectName(u"header_pasajeros")
        self.header_pasajeros.setGeometry(QRect(0, 0, 1951, 111))
        self.header_pasajeros.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border-bottom: 1px solid #E3E3E3;")
        self.boton_rutas = QPushButton(self.header_pasajeros)
        self.boton_rutas.setObjectName(u"boton_rutas")
        self.boton_rutas.setGeometry(QRect(1140, 20, 221, 71))
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
        icon.addFile(u"../recursos/recursos empresa/entrega.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_rutas.setIcon(icon)
        self.boton_rutas.setIconSize(QSize(30, 30))
        self.boton_corridas = QPushButton(self.header_pasajeros)
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
        icon1.addFile(u"../recursos/recursos empresa/calendario.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_corridas.setIcon(icon1)
        self.boton_corridas.setIconSize(QSize(30, 30))
        self.boton_operadores = QPushButton(self.header_pasajeros)
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
        icon2.addFile(u"../recursos/recursos empresa/conductor.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_operadores.setIcon(icon2)
        self.boton_operadores.setIconSize(QSize(30, 30))
        self.boton_autobuses = QPushButton(self.header_pasajeros)
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
        icon3.addFile(u"../recursos/recursos empresa/autobus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_autobuses.setIcon(icon3)
        self.boton_autobuses.setIconSize(QSize(30, 30))
        self.boton_inicio = QPushButton(self.header_pasajeros)
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
        icon4.addFile(u"../recursos/recursos empresa/casa-silueta-negra-sin-puerta.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_inicio.setIcon(icon4)
        self.boton_inicio.setIconSize(QSize(30, 30))
        self.boton_reservaciones = QPushButton(self.header_pasajeros)
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
        icon5.addFile(u"../recursos/recursos empresa/boleto.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_reservaciones.setIcon(icon5)
        self.boton_reservaciones.setIconSize(QSize(30, 30))
        self.boton_salir = QPushButton(self.header_pasajeros)
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
        icon6.addFile(u"../recursos/recursos empresa/cerrar-sesion.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_salir.setIcon(icon6)
        self.boton_salir.setIconSize(QSize(30, 30))
        self.label_4 = QLabel(self.header_pasajeros)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(18, 15, 231, 81))
        self.label_4.setStyleSheet(u"border: none")
        self.label_4.setPixmap(QPixmap(u"../recursos/recursos empresa/logo.png"))
        self.label_6 = QLabel(self.header_pasajeros)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(1790, 10, 70, 70))
        self.label_6.setPixmap(QPixmap(u"../recursos/recursos empresa/usuario.png"))
        self.label_6.setScaledContents(True)
        self.widget_pasajBotones = QWidget(Form)
        self.widget_pasajBotones.setObjectName(u"widget_pasajBotones")
        self.widget_pasajBotones.setGeometry(QRect(0, 120, 221, 871))
        self.widget_pasajBotones.setStyleSheet(u"\n"
"\n"
"background-color: #1061C4;\n"
"border: 1px solid #dcdfe6;\n"
"border-radius: 15px;\n"
"gridline-color: #e0e0e0;\n"
"outline: none;\n"
"color: #606266;\n"
"\n"
"")
        self.boton_anadirPasaj = QPushButton(self.widget_pasajBotones)
        self.boton_anadirPasaj.setObjectName(u"boton_anadirPasaj")
        self.boton_anadirPasaj.setGeometry(QRect(10, 40, 201, 71))
        self.boton_anadirPasaj.setFont(font)
        self.boton_anadirPasaj.setStyleSheet(u"QPushButton{\n"
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
        icon7 = QIcon()
        icon7.addFile(u"../recursos/recursos empresa/a\u00f1adir.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_anadirPasaj.setIcon(icon7)
        self.boton_anadirPasaj.setIconSize(QSize(30, 30))
        self.boton_actualizarPasaj = QPushButton(self.widget_pasajBotones)
        self.boton_actualizarPasaj.setObjectName(u"boton_actualizarPasaj")
        self.boton_actualizarPasaj.setGeometry(QRect(10, 130, 201, 71))
        self.boton_actualizarPasaj.setFont(font)
        self.boton_actualizarPasaj.setStyleSheet(u"QPushButton{\n"
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
        icon8 = QIcon()
        icon8.addFile(u"../recursos/recursos empresa/editar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_actualizarPasaj.setIcon(icon8)
        self.boton_actualizarPasaj.setIconSize(QSize(30, 30))
        self.widget_pasajFiltro = QWidget(Form)
        self.widget_pasajFiltro.setObjectName(u"widget_pasajFiltro")
        self.widget_pasajFiltro.setGeometry(QRect(240, 120, 1641, 101))
        self.widget_pasajFiltro.setStyleSheet(u"background-color: #ffffff;\n"
"border: 1px solid #dcdfe6;\n"
"border-radius: 15px;\n"
"gridline-color: #e0e0e0;\n"
"outline: none;\n"
"color: #606266;\n"
"border-radius: 15px;\n"
"border-bottom: 1px solid #E3E3E3;\n"
"\n"
"")
        self.corridas_label = QLabel(self.widget_pasajFiltro)
        self.corridas_label.setObjectName(u"corridas_label")
        self.corridas_label.setGeometry(QRect(30, 10, 351, 81))
        font1 = QFont()
        font1.setPointSize(59)
        font1.setBold(True)
        font1.setItalic(True)
        self.corridas_label.setFont(font1)
        self.corridas_label.setStyleSheet(u"border:none\n"
"\n"
"")
        self.corridas_label.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing)
        self.label = QLabel(self.widget_pasajFiltro)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(1061, 21, 58, 27))
        font2 = QFont()
        font2.setPointSize(15)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color: black;\n"
"border:none;")
        self.lineEdit_buscarTelPasaj = QLineEdit(self.widget_pasajFiltro)
        self.lineEdit_buscarTelPasaj.setObjectName(u"lineEdit_buscarTelPasaj")
        self.lineEdit_buscarTelPasaj.setGeometry(QRect(1250, 56, 151, 25))
        font3 = QFont()
        font3.setPointSize(12)
        self.lineEdit_buscarTelPasaj.setFont(font3)
        self.lineEdit_buscarTelPasaj.setStyleSheet(u"border-radius: 6px;")
        self.label_2 = QLabel(self.widget_pasajFiltro)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(1250, 21, 58, 27))
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color: black;\n"
"border:none;")
        self.lineEdit_buscarNumPasaj = QLineEdit(self.widget_pasajFiltro)
        self.lineEdit_buscarNumPasaj.setObjectName(u"lineEdit_buscarNumPasaj")
        self.lineEdit_buscarNumPasaj.setGeometry(QRect(1060, 56, 151, 25))
        self.lineEdit_buscarNumPasaj.setFont(font3)
        self.lineEdit_buscarNumPasaj.setStyleSheet(u"border-radius: 6px;")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        ___qtablewidgetitem = self.QtableWidget_pasajeros.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Num", None));
        ___qtablewidgetitem1 = self.QtableWidget_pasajeros.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Nombre", None));
        ___qtablewidgetitem2 = self.QtableWidget_pasajeros.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Fecha de nacimiento", None));
        ___qtablewidgetitem3 = self.QtableWidget_pasajeros.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Edad", None));
        ___qtablewidgetitem4 = self.QtableWidget_pasajeros.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Correo electr\u00f3nico", None));
        ___qtablewidgetitem5 = self.QtableWidget_pasajeros.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Tel\u00e9fono", None));
        self.boton_rutas.setText(QCoreApplication.translate("Form", u"Rutas", None))
        self.boton_corridas.setText(QCoreApplication.translate("Form", u"Corridas", None))
        self.boton_operadores.setText(QCoreApplication.translate("Form", u"Operadores", None))
        self.boton_autobuses.setText(QCoreApplication.translate("Form", u"Autobuses", None))
        self.boton_inicio.setText("")
        self.boton_reservaciones.setText(QCoreApplication.translate("Form", u"Reservaciones", None))
        self.boton_salir.setText("")
        self.label_4.setText("")
        self.label_6.setText("")
        self.boton_anadirPasaj.setText(QCoreApplication.translate("Form", u"A\u00f1adir", None))
        self.boton_actualizarPasaj.setText(QCoreApplication.translate("Form", u"Actualizar", None))
        self.corridas_label.setText(QCoreApplication.translate("Form", u"Pasajeros", None))
        self.label.setText(QCoreApplication.translate("Form", u"Buscar", None))
        self.lineEdit_buscarTelPasaj.setText("")
        self.lineEdit_buscarTelPasaj.setPlaceholderText(QCoreApplication.translate("Form", u"N\u00famero telef\u00f3nico", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Buscar", None))
        self.lineEdit_buscarNumPasaj.setText("")
        self.lineEdit_buscarNumPasaj.setPlaceholderText(QCoreApplication.translate("Form", u"N\u00famero de pasajero", None))
    # retranslateUi

