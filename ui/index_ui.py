# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'index.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.NonModal)
        MainWindow.resize(1920, 1080)
        MainWindow.setMinimumSize(QSize(1920, 1080))
        MainWindow.setMaximumSize(QSize(1920, 1080))
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget_opfiltro_2 = QWidget(self.centralwidget)
        self.widget_opfiltro_2.setObjectName(u"widget_opfiltro_2")
        self.widget_opfiltro_2.setGeometry(QRect(10, 130, 1881, 101))
        self.widget_opfiltro_2.setStyleSheet(u"background-color: #ffffff;\n"
"border: 2px solid #dcdfe6;\n"
"border-radius: 15px;\n"
"gridline-color: #e0e0e0;\n"
"outline: none;\n"
"color: #606266;\n"
"border-radius: 15px;\n"
"border-bottom: 1px solid #E3E3E3;\n"
"\n"
"")
        self.corridas_label = QLabel(self.widget_opfiltro_2)
        self.corridas_label.setObjectName(u"corridas_label")
        self.corridas_label.setGeometry(QRect(20, 10, 551, 71))
        font = QFont()
        font.setPointSize(59)
        font.setBold(True)
        font.setItalic(True)
        self.corridas_label.setFont(font)
        self.corridas_label.setStyleSheet(u"border:none")
        self.header_corridas = QWidget(self.centralwidget)
        self.header_corridas.setObjectName(u"header_corridas")
        self.header_corridas.setGeometry(QRect(10, 10, 1951, 111))
        self.header_corridas.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border-bottom: 1px solid #E3E3E3;")
        self.boton_rutas = QPushButton(self.header_corridas)
        self.boton_rutas.setObjectName(u"boton_rutas")
        self.boton_rutas.setGeometry(QRect(1140, 20, 221, 71))
        font1 = QFont()
        font1.setBold(True)
        self.boton_rutas.setFont(font1)
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
        self.boton_corridas = QPushButton(self.header_corridas)
        self.boton_corridas.setObjectName(u"boton_corridas")
        self.boton_corridas.setGeometry(QRect(640, 20, 221, 71))
        self.boton_corridas.setFont(font1)
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
        self.boton_operadores = QPushButton(self.header_corridas)
        self.boton_operadores.setObjectName(u"boton_operadores")
        self.boton_operadores.setGeometry(QRect(1390, 20, 221, 71))
        self.boton_operadores.setFont(font1)
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
        self.boton_autobuses = QPushButton(self.header_corridas)
        self.boton_autobuses.setObjectName(u"boton_autobuses")
        self.boton_autobuses.setGeometry(QRect(890, 20, 221, 71))
        self.boton_autobuses.setFont(font1)
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
        self.boton_inicio = QPushButton(self.header_corridas)
        self.boton_inicio.setObjectName(u"boton_inicio")
        self.boton_inicio.setGeometry(QRect(270, 20, 91, 71))
        self.boton_inicio.setFont(font1)
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
        self.boton_reservaciones = QPushButton(self.header_corridas)
        self.boton_reservaciones.setObjectName(u"boton_reservaciones")
        self.boton_reservaciones.setGeometry(QRect(390, 20, 221, 71))
        self.boton_reservaciones.setFont(font1)
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
        self.boton_salir = QPushButton(self.header_corridas)
        self.boton_salir.setObjectName(u"boton_salir")
        self.boton_salir.setGeometry(QRect(1640, 20, 91, 71))
        self.boton_salir.setFont(font1)
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
        self.label_5 = QLabel(self.header_corridas)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(18, 15, 231, 81))
        self.label_5.setStyleSheet(u"border: none")
        self.label_5.setPixmap(QPixmap(u"../recursos/recursos empresa/logo.png"))
        self.label_6 = QLabel(self.header_corridas)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(1790, 10, 70, 70))
        self.label_6.setPixmap(QPixmap(u"../recursos/recursos empresa/usuario.png"))
        self.label_6.setScaledContents(True)
        self.boton_autobuses_2 = QPushButton(self.centralwidget)
        self.boton_autobuses_2.setObjectName(u"boton_autobuses_2")
        self.boton_autobuses_2.setGeometry(QRect(1590, 960, 241, 71))
        self.boton_autobuses_2.setFont(font1)
        self.boton_autobuses_2.setStyleSheet(u"QPushButton{\n"
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
        self.boton_autobuses_2.setIcon(icon5)
        self.boton_autobuses_2.setIconSize(QSize(30, 30))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(880, 260, 951, 681))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setPointSize(41)
        font2.setBold(True)
        font2.setItalic(True)
        self.label_2.setFont(font2)

        self.verticalLayout_2.addWidget(self.label_2)

        self.pasajerosm_tableWidget = QTableWidget(self.layoutWidget)
        if (self.pasajerosm_tableWidget.columnCount() < 4):
            self.pasajerosm_tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.pasajerosm_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.pasajerosm_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.pasajerosm_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.pasajerosm_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.pasajerosm_tableWidget.setObjectName(u"pasajerosm_tableWidget")
        self.pasajerosm_tableWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.pasajerosm_tableWidget.setStyleSheet(u"\n"
"QTableWidget {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #dcdfe6;\n"
"    border-radius: 15px;\n"
"    gridline-color: #e0e0e0;\n"
"    outline: none;\n"
"    font-size: 13px;\n"
"    color: #606266;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    padding: 8px;\n"
"    border-bottom: 1px solid #f0f0f0;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #409eff;\n"
"    color: white;\n"
"}\n"
"\n"
"QTableWidget::item:hover {\n"
"    background-color: #f5f7fa;\n"
"}\n"
"\n"
"/* Header con bordes redondeados solo arriba */\n"
"QHeaderView::section:first {\n"
"    border-top-left-radius: 15px;\n"
"}\n"
"\n"
"QHeaderView::section:last {\n"
"    border-top-right-radius: 15px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #1061C4;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    font-size: 18px;\n"
"    padding: 8px 12px;\n"
"    border: none;\n"
"    border-right: 1px solid #0a4a9d;\n"
"}\n"
"\n"
"QHeaderView::section:hover {\n"
"    background-color:"
                        " #0a4a9d;\n"
"}\n"
"\n"
"QHeaderView::section:pressed {\n"
"    background-color: #083a7a;\n"
"}\n"
"")
        self.pasajerosm_tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.pasajerosm_tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.pasajerosm_tableWidget.horizontalHeader().setDefaultSectionSize(237)
        self.pasajerosm_tableWidget.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.pasajerosm_tableWidget)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(19, 260, 751, 681))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label = QLabel(self.layoutWidget1)
        self.label.setObjectName(u"label")
        self.label.setFont(font2)

        self.verticalLayout.addWidget(self.label)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.layoutWidget1)
        self.label_4.setObjectName(u"label_4")
        font3 = QFont()
        font3.setPointSize(12)
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"color: black;\n"
"border:none;")

        self.verticalLayout_3.addWidget(self.label_4)

        self.dateEdit_filtroFecha = QDateEdit(self.layoutWidget1)
        self.dateEdit_filtroFecha.setObjectName(u"dateEdit_filtroFecha")
        self.dateEdit_filtroFecha.setMaximumDateTime(QDateTime(QDate(2030, 1, 1), QTime(23, 59, 59)))
        self.dateEdit_filtroFecha.setMinimumDateTime(QDateTime(QDate(2025, 1, 1), QTime(8, 0, 0)))
        self.dateEdit_filtroFecha.setMaximumDate(QDate(2030, 1, 1))
        self.dateEdit_filtroFecha.setMinimumDate(QDate(2025, 1, 1))

        self.verticalLayout_3.addWidget(self.dateEdit_filtroFecha)


        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.corridasm_tableWidget = QTableWidget(self.layoutWidget1)
        if (self.corridasm_tableWidget.columnCount() < 4):
            self.corridasm_tableWidget.setColumnCount(4)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.corridasm_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.corridasm_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.corridasm_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.corridasm_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        self.corridasm_tableWidget.setObjectName(u"corridasm_tableWidget")
        self.corridasm_tableWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.corridasm_tableWidget.setStyleSheet(u"\n"
"QTableWidget {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #dcdfe6;\n"
"    border-radius: 15px;\n"
"    gridline-color: #e0e0e0;\n"
"    outline: none;\n"
"    font-size: 15px;\n"
"    color: #606266;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    padding: 8px;\n"
"    border-bottom: 1px solid #f0f0f0;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #409eff;\n"
"    color: white;\n"
"}\n"
"\n"
"QTableWidget::item:hover {\n"
"    background-color: #f5f7fa;\n"
"}\n"
"\n"
"/* Header con bordes redondeados solo arriba */\n"
"QHeaderView::section:first {\n"
"    border-top-left-radius: 15px;\n"
"}\n"
"\n"
"QHeaderView::section:last {\n"
"    border-top-right-radius: 15px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #1061C4;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    font-size: 18px;\n"
"    padding: 8px 12px;\n"
"    border: none;\n"
"    border-right: 1px solid #0a4a9d;\n"
"}\n"
"\n"
"QHeaderView::section:hover {\n"
"    background-color:"
                        " #0a4a9d;\n"
"}\n"
"\n"
"QHeaderView::section:pressed {\n"
"    background-color: #083a7a;\n"
"}\n"
"")
        self.corridasm_tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.corridasm_tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.corridasm_tableWidget.horizontalHeader().setDefaultSectionSize(187)
        self.corridasm_tableWidget.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.corridasm_tableWidget)

        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.verticalLayout.addWidget(self.label_3)

        self.autobusm_tableWidget = QTableWidget(self.layoutWidget1)
        if (self.autobusm_tableWidget.columnCount() < 4):
            self.autobusm_tableWidget.setColumnCount(4)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.autobusm_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.autobusm_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.autobusm_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.autobusm_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        self.autobusm_tableWidget.setObjectName(u"autobusm_tableWidget")
        self.autobusm_tableWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.autobusm_tableWidget.setStyleSheet(u"\n"
"QTableWidget {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #dcdfe6;\n"
"    border-radius: 15px;\n"
"    gridline-color: #e0e0e0;\n"
"    outline: none;\n"
"    font-size: 13px;\n"
"    color: #606266;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    padding: 8px;\n"
"    border-bottom: 1px solid #f0f0f0;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #409eff;\n"
"    color: white;\n"
"}\n"
"\n"
"QTableWidget::item:hover {\n"
"    background-color: #f5f7fa;\n"
"}\n"
"\n"
"/* Header con bordes redondeados solo arriba */\n"
"QHeaderView::section:first {\n"
"    border-top-left-radius: 15px;\n"
"}\n"
"\n"
"QHeaderView::section:last {\n"
"    border-top-right-radius: 15px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #1061C4;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    font-size: 18px;\n"
"    padding: 8px 12px;\n"
"    border: none;\n"
"    border-right: 1px solid #0a4a9d;\n"
"}\n"
"\n"
"QHeaderView::section:hover {\n"
"    background-color:"
                        " #0a4a9d;\n"
"}\n"
"\n"
"QHeaderView::section:pressed {\n"
"    background-color: #083a7a;\n"
"}\n"
"")
        self.autobusm_tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.autobusm_tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.autobusm_tableWidget.horizontalHeader().setDefaultSectionSize(187)
        self.autobusm_tableWidget.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.autobusm_tableWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.corridas_label.setText(QCoreApplication.translate("MainWindow", u"Inicio", None))
        self.boton_rutas.setText(QCoreApplication.translate("MainWindow", u"Rutas", None))
        self.boton_corridas.setText(QCoreApplication.translate("MainWindow", u"Corridas", None))
        self.boton_operadores.setText(QCoreApplication.translate("MainWindow", u"Operadores", None))
        self.boton_autobuses.setText(QCoreApplication.translate("MainWindow", u"Autobuses", None))
        self.boton_inicio.setText("")
        self.boton_reservaciones.setText(QCoreApplication.translate("MainWindow", u"Reservaciones", None))
        self.boton_salir.setText("")
        self.label_5.setText("")
        self.label_6.setText("")
        self.boton_autobuses_2.setText(QCoreApplication.translate("MainWindow", u"Comprar boleto", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Pasajeros", None))
        ___qtablewidgetitem = self.pasajerosm_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 Pasajero", None));
        ___qtablewidgetitem1 = self.pasajerosm_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nombre ", None));
        ___qtablewidgetitem2 = self.pasajerosm_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Edad", None));
        ___qtablewidgetitem3 = self.pasajerosm_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Telefono", None));
        self.label.setText(QCoreApplication.translate("MainWindow", u"Corridas activas", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Buscar por fecha", None))
        ___qtablewidgetitem4 = self.corridasm_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 Corrida", None));
        ___qtablewidgetitem5 = self.corridasm_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Fecha", None));
        ___qtablewidgetitem6 = self.corridasm_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Hora Salida", None));
        ___qtablewidgetitem7 = self.corridasm_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Ruta", None));
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Operadores", None))
        ___qtablewidgetitem8 = self.autobusm_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 Operador", None));
        ___qtablewidgetitem9 = self.autobusm_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem10 = self.autobusm_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Corrida asignada", None));
        ___qtablewidgetitem11 = self.autobusm_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Fecha de corrida", None));
    # retranslateUi

