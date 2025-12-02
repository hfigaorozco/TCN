# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pantalla_viajar.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1920, 1080)
        Form.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_estatico_logo = QLabel(Form)
        self.label_estatico_logo.setObjectName(u"label_estatico_logo")
        self.label_estatico_logo.setGeometry(QRect(1560, 20, 331, 91))
        self.label_estatico_logo.setPixmap(QPixmap(u"../../recursos/recursos_empresa/Screenshot from 2025-11-22 14-58-14.png"))
        self.label_estatico_logo.setScaledContents(True)
        self.label_estatico_titulo = QLabel(Form)
        self.label_estatico_titulo.setObjectName(u"label_estatico_titulo")
        self.label_estatico_titulo.setGeometry(QRect(750, 40, 381, 71))
        self.boton_regresar = QPushButton(Form)
        self.boton_regresar.setObjectName(u"boton_regresar")
        self.boton_regresar.setGeometry(QRect(110, 40, 201, 71))
        self.boton_regresar.setStyleSheet(u"QPushButton {\n"
"    /* Sin color de fondo */\n"
"    background-color: transparent;\n"
"    \n"
"    /* Borde naranja */\n"
"    border: 2px solid #FFA500;\n"
"    \n"
"    /* Bordes redondos */\n"
"    border-radius: 15px;\n"
"    \n"
"    /* Texto naranja y en negrita */\n"
"    color: #FFA500;\n"
"    font-weight: bold;\n"
"	font-size: 24px;\n"
"    \n"
"    /* Padding interno */\n"
"    padding: 8px 16px;\n"
"    \n"
"    /* Eliminar outline por defecto */\n"
"    outline: none;\n"
"}\n"
"\n"
"/* Efecto hover */\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 165, 0, 0.1);\n"
"}\n"
"\n"
"/* Efecto pressed */\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 165, 0, 0.2);\n"
"    border: 2px solid #FF8C00;\n"
"    color: #FF8C00;\n"
"}\n"
"\n"
"/* Efecto disabled */\n"
"QPushButton:disabled {\n"
"    border: 2px solid #CCCCCC;\n"
"    color: #CCCCCC;\n"
"    background-color: transparent;\n"
"}")
        self.tableWidget = QTableWidget(Form)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(160, 300, 1561, 681))
        self.tableWidget.setStyleSheet(u"QTableView {\n"
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
"    \n"
"    /* Centrar todo el contenido de las celdas */\n"
"    qproperty-alignment: 'AlignCenter';\n"
"}\n"
"\n"
"QTableView::item {\n"
"    padding: 8px 12px;\n"
"    border: 0px;\n"
"    \n"
"    /* Centrar contenido de cada item */\n"
"    text-align: center;\n"
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
"    \n"
"    /* Cent"
                        "rar texto del encabezado */\n"
"    text-align: center;\n"
"    \n"
"    /* Asegurar que todas las columnas tengan el mismo ancho */\n"
"    qproperty-minimumSectionSize: 150; /* Ancho m\u00ednimo igual para todas */\n"
"    qproperty-defaultAlignment: 'AlignCenter'; /* Centrar texto del header */\n"
"}\n"
"\n"
"QHeaderView::section:hover {\n"
"    background: #f7f9fc;\n"
"}\n"
"\n"
"QHeaderView {\n"
"    background: #ffffff;\n"
"    border: 0;\n"
"    \n"
"    /* IMPORTANTE: Forzar que las secciones se estiren para llenar el espacio */\n"
"    qproperty-stretchLastSection: false;\n"
"    qproperty-resizeMode: 'Stretch'; /* Esto hace que las columnas se ajusten autom\u00e1ticamente */\n"
"}\n"
"\n"
"/* Configuraci\u00f3n adicional para el modelo de datos en Python */\n"
"QTableView QAbstractItemView {\n"
"    /* Asegurar que las columnas se ajusten al contenido */\n"
"    qproperty-horizontalScrollMode: 'ScrollPerPixel';\n"
"    qproperty-verticalScrollMode: 'ScrollPerPixel';\n"
"}\n"
"\n"
"QTableView::indicat"
                        "or {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"    /* Centrar el checkbox si hay */\n"
"    margin-left: auto;\n"
"    margin-right: auto;\n"
"}\n"
"\n"
"QHeaderView::section:first {\n"
"    border-top-left-radius: 8px;\n"
"}\n"
"\n"
"QHeaderView::section:last {\n"
"    border-top-right-radius: 8px;\n"
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
"}")
        self.tableWidget.horizontalHeader().setDefaultSectionSize(223)
        self.label_estatico_subtitulo = QLabel(Form)
        self.label_estatico_subtitulo.setObjectName(u"label_estatico_subtitulo")
        self.label_estatico_subtitulo.setGeometry(QRect(90, 200, 141, 61))
        self.label_ciudadOrigen = QLabel(Form)
        self.label_ciudadOrigen.setObjectName(u"label_ciudadOrigen")
        self.label_ciudadOrigen.setGeometry(QRect(230, 210, 431, 51))
        self.label_ciudadOrigen.setStyleSheet(u"QLabel {\n"
"    font-size: 24px;\n"
"}")
        self.label_estatico_subtitulo_2 = QLabel(Form)
        self.label_estatico_subtitulo_2.setObjectName(u"label_estatico_subtitulo_2")
        self.label_estatico_subtitulo_2.setGeometry(QRect(690, 210, 141, 51))
        self.label_ciudadDestino = QLabel(Form)
        self.label_ciudadDestino.setObjectName(u"label_ciudadDestino")
        self.label_ciudadDestino.setGeometry(QRect(850, 210, 461, 61))
        self.label_ciudadDestino.setStyleSheet(u"QLabel {\n"
"    font-size: 24px;\n"
"}")
        self.label_estatico_subtitulo_3 = QLabel(Form)
        self.label_estatico_subtitulo_3.setObjectName(u"label_estatico_subtitulo_3")
        self.label_estatico_subtitulo_3.setGeometry(QRect(1350, 210, 121, 51))
        self.label_fechaCorrida = QLabel(Form)
        self.label_fechaCorrida.setObjectName(u"label_fechaCorrida")
        self.label_fechaCorrida.setGeometry(QRect(1490, 200, 401, 61))
        self.label_fechaCorrida.setStyleSheet(u"QLabel {\n"
"    font-size: 20px;\n"
"}")
        self.boton_continuar = QPushButton(Form)
        self.boton_continuar.setObjectName(u"boton_continuar")
        self.boton_continuar.setGeometry(QRect(1110, 1000, 191, 61))
        self.boton_continuar.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: 4px solid #1877F2;\n"
"    border-radius: 15px;\n"
"    color: #1877F2;\n"
"    font-weight: bold;\n"
"    font-size: 24px;\n"
"    padding: 12px 24px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(24, 119, 242, 0.1);\n"
"    border: 4px solid #166FE5;\n"
"    color: #166FE5;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(24, 119, 242, 0.2);\n"
"    border: 4px solid #1460C4;\n"
"    color: #1460C4;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    border: 4px solid #CCCCCC;\n"
"    color: #CCCCCC;\n"
"    background-color: transparent;\n"
"}")
        self.label_estatico_subtitulo_4 = QLabel(Form)
        self.label_estatico_subtitulo_4.setObjectName(u"label_estatico_subtitulo_4")
        self.label_estatico_subtitulo_4.setGeometry(QRect(450, 1010, 651, 41))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_estatico_logo.setText("")
        self.label_estatico_titulo.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:700; font-style:italic;\">VIAJAR</span></p></body></html>", None))
        self.boton_regresar.setText(QCoreApplication.translate("Form", u"Regresar", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"No. Corrida", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Autob\u00fas", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Servicio", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Hora de llegada", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Hora de salida", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Lugares disponibles", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"Precio", None));
        self.label_estatico_subtitulo.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:28pt; font-weight:700;\">Origen:</span></p></body></html>", None))
        self.label_ciudadOrigen.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_estatico_subtitulo_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:28pt; font-weight:700;\">Destino:</span></p><p><br/></p></body></html>", None))
        self.label_ciudadDestino.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_estatico_subtitulo_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:28pt; font-weight:700;\">Fecha:</span></p><p><br/></p></body></html>", None))
        self.label_fechaCorrida.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><br/></p></body></html>", None))
        self.boton_continuar.setText(QCoreApplication.translate("Form", u"Continuar", None))
        self.label_estatico_subtitulo_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:700;\">Selecciona una corrida para continuar</span></p></body></html>", None))
    # retranslateUi

