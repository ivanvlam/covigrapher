from PyQt5.QtWidgets import QLabel, QWidget, QPushButton
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap, QFont, QIcon, QMovie
import parametros as p


class VentanaInicio(QWidget):

    senal_avanzar = pyqtSignal()
    senal_predeterminados = pyqtSignal()
    senal_labels = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setFixedHeight(p.VENTANA_ALTO)
        self.setFixedWidth(p.VENTANA_ANCHO)
        
        self.setWindowIcon(QIcon(p.PATH_LOGO))

        self.setWindowTitle("COVIGRAPHER")

        self.init_gui()
        

    def init_gui(self):

        self.gif_background = QMovie(p.PATH_GRADIENTE)
        self.label_background = QLabel(self)
        self.label_background.setFixedWidth(p.VENTANA_ANCHO)
        self.label_background.setFixedHeight(p.VENTANA_ALTO)
        self.label_background.setMovie(self.gif_background)
        self.label_background.setScaledContents(True)
        self.gif_background.start()

        self.logo_completo = QLabel(self)
        self.logo_completo.resize(p.VENTANA_ANCHO * 80 / 100, p.VENTANA_ANCHO * 80 / 100)
        self.logo_completo.setPixmap(QPixmap(p.PATH_LOGO_COMPLETO))
        self.logo_completo.move(p.VENTANA_ANCHO * 10 / 100, -10)
        self.logo_completo.setScaledContents(True)
        

        self.boton_iniciar = QPushButton('&Iniciar', self)
        self.boton_iniciar.resize(p.VENTANA_ANCHO * 60 / 100, p.VENTANA_ALTO * 8 / 100)
        self.boton_iniciar.clicked.connect(self.avanzar)
        self.boton_iniciar.setFont(QFont('Courier', 20, QFont.Bold))
        self.boton_iniciar.move(p.VENTANA_ANCHO * 20 / 100, p.VENTANA_ALTO * 75 / 100)
        self.boton_iniciar.setStyleSheet(p.ESTILO_BOTON)

        '''
        self.boton_predeterminados = QPushButton('&Gráficos predeterminados', self)
        self.boton_predeterminados.resize(p.VENTANA_ANCHO * 60 / 100, p.VENTANA_ALTO * 8 / 100)
        self.boton_predeterminados.clicked.connect(self.mostrar_predeterminados)
        self.boton_predeterminados.setFont(QFont('Courier', 22, QFont.Bold))
        self.boton_predeterminados.move(p.VENTANA_ANCHO * 20 / 100, p.VENTANA_ALTO * 87 / 100)
        self.boton_predeterminados.setStyleSheet(p.ESTILO_BOTON)
        '''

        self.boton_salir = QPushButton('&Salir', self)
        self.boton_salir.resize(p.VENTANA_ANCHO * 60 / 100, p.VENTANA_ALTO * 8 / 100)
        self.boton_salir.clicked.connect(self.salir)
        self.boton_salir.setFont(QFont('Courier', 22, QFont.Bold))
        self.boton_salir.move(p.VENTANA_ANCHO * 20 / 100, p.VENTANA_ALTO * 87 / 100)
        self.boton_salir.setStyleSheet(p.ESTILO_BOTON)
    
    def mostrar_grilla(self):
        texto = self.activacion_grilla.currentText()
        if texto[0] == 'D':
            self.imagen_grilla.hide()
        else:
            self.imagen_grilla.show()

    def revisar_promedio(self):
        texto = self.activacion_promedio_movil.currentText()
        if texto[0] == 'D':
            self.slider_ventana.setDisabled(True)
        else:
            self.slider_ventana.setEnabled(True)
        
    def mostrar_predeterminados(self):
        self.senal_predeterminados.emit()

    def avanzar(self):
        self.senal_avanzar.emit()
        self.close()
    
    def mostrar_ventana(self):
        self.senal_labels.emit()
        self.show()
    
    def salir(self):
        self.close()