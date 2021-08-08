from PyQt5.QtWidgets import QLabel, QWidget, QFileDialog, QPushButton, QColorDialog, QComboBox
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QPen, QPixmap, QFont, QIcon, QMovie, QPainter
from random import randint
import parametros as p


class VentanaAgregarRegion(QWidget):

    senal_volver = pyqtSignal()
    senal_avanzar = pyqtSignal(list)
    senal_nombre = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setFixedHeight(p.VENTANA_ALTO)
        self.setFixedWidth(p.VENTANA_ANCHO)
        
        self.setWindowIcon(QIcon(p.PATH_LOGO))

        self.setWindowTitle("COVIGRAPHER")

        self.regiones_seleccionadas = []
        self.regiones = p.REGIONES
        self.color_seleccionado = Qt.red
        self.carga_lista = False

        self.init_gui()
        self.recibir_grilla(True)

    def init_gui(self):

        self.gif_background = QMovie(p.PATH_GRADIENTE)
        self.label_background = QLabel(self)
        self.label_background.setFixedWidth(p.VENTANA_ANCHO)
        self.label_background.setFixedHeight(p.VENTANA_ALTO)
        self.label_background.setMovie(self.gif_background)
        self.label_background.setScaledContents(True)
        self.gif_background.start()

        self.top_label = QLabel(self)
        self.top_label.setFixedWidth(p.VENTANA_ANCHO * 94 / 100)
        self.top_label.setFixedHeight(p.VENTANA_ALTO * 35 / 100)
        self.top_label.setStyleSheet(p.ESTILO_LABEL_SELECCION)
        self.top_label.move(p.VENTANA_ANCHO * 3 / 100, p.VENTANA_ALTO * 4 / 100)

        self.label_region_text = QLabel(self)
        self.label_region_text.resize(p.VENTANA_ANCHO * 96 / 100, p.VENTANA_ALTO / 6)
        self.label_region_text.setPixmap(QPixmap(p.PATH_REGION_TITLE))
        self.label_region_text.move(
            self.top_label.x(), 
            self.top_label.y()
        )
        self.label_region_text.setAlignment(Qt.AlignCenter)

        
        self.seleccion_region = QComboBox(self)
        self.seleccion_region.resize(p.VENTANA_ANCHO * 80 / 100, 45)
        self.seleccion_region.addItem('Total')
        
        for region in self.regiones:
            self.seleccion_region.addItem(region)

        self.seleccion_region.setEditable(True)
        line_edit = self.seleccion_region.lineEdit()
        line_edit.setAlignment(Qt.AlignCenter)
        line_edit.setReadOnly(True)
        
        self.seleccion_region.setFont(QFont('Courier', 14, QFont.Light))
        self.seleccion_region.move(p.VENTANA_ANCHO * 10 / 100, p.VENTANA_ALTO * 17.5 / 100)
        
        self.boton_color = QPushButton('&Seleccionar color', self)
        self.boton_color.resize(p.VENTANA_ANCHO * 42.5 / 100, p.VENTANA_ALTO * 7 / 100)
        self.boton_color.clicked.connect(self.seleccionar_color)
        self.boton_color.setFont(QFont('Courier', 16, QFont.Bold))
        self.boton_color.move(p.VENTANA_ANCHO * 6 / 100, p.VENTANA_ALTO * 28 / 100)
        self.boton_color.setStyleSheet(p.ESTILO_BOTON_REGION)

        self.boton_agregar_region = QPushButton('&Agregar región', self)
        self.boton_agregar_region.resize(p.VENTANA_ANCHO * 42.5 / 100, p.VENTANA_ALTO * 7 / 100)
        self.boton_agregar_region.clicked.connect(self.agregar_region)
        self.boton_agregar_region.setFont(QFont('Courier', 16, QFont.Bold))
        self.boton_agregar_region.move(p.VENTANA_ANCHO * 51.5 / 100, p.VENTANA_ALTO * 28 / 100)
        self.boton_agregar_region.setStyleSheet(p.ESTILO_BOTON_REGION)


        self.bottom_label = QLabel(self)
        self.bottom_label.setFixedWidth(p.VENTANA_ANCHO * 94 / 100)
        self.bottom_label.setFixedHeight(p.VENTANA_ALTO * 42 / 100)
        self.bottom_label.setStyleSheet(p.ESTILO_LABEL_SELECCION)
        self.bottom_label.move(p.VENTANA_ANCHO * 3 / 100, p.VENTANA_ALTO * 43 / 100)
        
        self.label_previsualizacion_text = QLabel(self)
        self.label_previsualizacion_text.resize(p.VENTANA_ANCHO * 96 / 100, p.VENTANA_ALTO / 8)
        self.label_previsualizacion_text.setPixmap(QPixmap(p.PATH_PREVISUALIZACION_TITLE))
        self.label_previsualizacion_text.move(
            self.bottom_label.x(), 
            self.bottom_label.y() + 5
        )
        self.label_previsualizacion_text.setAlignment(Qt.AlignCenter)

        self.label_blanco = QLabel(self)
        pixeles = QPixmap(p.PATH_WHITE)
        pixeles = pixeles.scaled(p.VENTANA_ANCHO * 64 / 100, p.VENTANA_ANCHO * 32 / 100, Qt.IgnoreAspectRatio)
        self.label_blanco.setPixmap(pixeles)
        self.label_blanco.move(
            p.VENTANA_ANCHO * 18 / 100, 
            self.bottom_label.y() + p.VENTANA_ALTO * 10.5 / 100
        )

        self.grilla = QLabel(self)
        pixeles = QPixmap(p.PATH_BIG_GRID)
        pixeles = pixeles.scaled(p.VENTANA_ANCHO * 64 / 100, p.VENTANA_ANCHO * 32 / 100, Qt.IgnoreAspectRatio)
        self.grilla.setPixmap(pixeles)
        self.grilla.move(
            p.VENTANA_ANCHO * 18 / 100, 
            self.bottom_label.y() + p.VENTANA_ALTO * 10.5 / 100
        )
        self.grilla.setScaledContents(True)
        self.grilla.hide()


        self.boton_volver = QPushButton('&Volver', self)
        self.boton_volver.resize(p.VENTANA_ANCHO * 18 / 100, p.VENTANA_ALTO * 7 / 100)
        self.boton_volver.clicked.connect(self.volver)
        self.boton_volver.setFont(QFont('Courier', 20, QFont.Bold))
        self.boton_volver.move(p.VENTANA_ANCHO * 3 / 100, p.VENTANA_ALTO * 89 / 100)
        self.boton_volver.setStyleSheet(p.ESTILO_BOTON)

        self.boton_reiniciar = QPushButton('&Reiniciar gráfico', self)
        self.boton_reiniciar.resize(p.VENTANA_ANCHO * 45 / 100, p.VENTANA_ALTO * 7 / 100)
        self.boton_reiniciar.clicked.connect(self.reiniciar_grafico)
        self.boton_reiniciar.setFont(QFont('Courier', 20, QFont.Bold))
        self.boton_reiniciar.move(p.VENTANA_ANCHO * 24 / 100, p.VENTANA_ALTO * 89 / 100)
        self.boton_reiniciar.setStyleSheet(p.ESTILO_BOTON_REINICIAR)

        self.boton_finalizar = QPushButton('&Finalizar', self)
        self.boton_finalizar.resize(p.VENTANA_ANCHO * 25 / 100, p.VENTANA_ALTO * 7 / 100)
        self.boton_finalizar.clicked.connect(self.avanzar)
        self.boton_finalizar.setFont(QFont('Courier', 20, QFont.Bold))
        self.boton_finalizar.move(p.VENTANA_ANCHO * 72 / 100, p.VENTANA_ALTO * 89 / 100)
        self.boton_finalizar.setStyleSheet(p.ESTILO_BOTON_FINALIZAR)
        self.boton_finalizar.setDisabled(True)
    
    def seleccionar_color(self):
        self.color_seleccionado = QColorDialog.getColor()
        estilo = p.ESTILO_BOTON_REGION.replace('black', self.color_seleccionado.name())
        self.boton_color.setStyleSheet(estilo)
    
    def agregar_region(self):
        lapiz = QPen()
        lapiz.setColor(self.color_seleccionado)
        lapiz.setWidth(6)

        if self.grid:
            pixeles = QPixmap(self.grilla.size())
            pixeles.fill(Qt.transparent)

            painter = QPainter(pixeles)
            painter.setPen(lapiz)
            painter.drawPixmap(0, 0, self.grilla.pixmap())
            x_1 = randint(10, 200)
            y_1 = randint(10, 200)
            painter.drawLine(10, 10, x_1, y_1)
            x_2 = randint(x_1, 300)
            y_2 = randint(10, 200)
            painter.drawLine(x_1, y_1, x_2, y_2)
            x_3 = randint(x_2, 350)
            y_3 = randint(10, 200)
            painter.drawLine(x_2, y_2, x_3, y_3)
            y_4 = randint(10, 200)
            painter.drawLine(x_3, y_3, 400, y_4)
            painter.end()

            self.grilla.setPixmap(pixeles)
            self.grilla.setScaledContents(True)
        
        else:
            pixeles = QPixmap(self.label_blanco.size())
            pixeles.fill(Qt.transparent)

            painter = QPainter(pixeles)
            painter.setPen(lapiz)
            painter.drawPixmap(0, 0, self.label_blanco.pixmap())
            x_1 = randint(10, 200)
            y_1 = randint(10, 200)
            painter.drawLine(10, 10, x_1, y_1)
            x_2 = randint(x_1, 300)
            y_2 = randint(10, 200)
            painter.drawLine(x_1, y_1, x_2, y_2)
            x_3 = randint(x_2, 350)
            y_3 = randint(10, 200)
            painter.drawLine(x_2, y_2, x_3, y_3)
            y_4 = randint(10, 200)
            painter.drawLine(x_3, y_3, 400, y_4)
            painter.end()

            self.label_blanco.setPixmap(pixeles)
            self.label_blanco.setScaledContents(True)

        region = self.seleccion_region.currentText()
        try:
            color = self.color_seleccionado.name()
        except AttributeError:
            color = '#ff0000'

        self.regiones_seleccionadas.append((region, color))
        self.seleccion_region.removeItem(self.seleccion_region.currentIndex())
        
        if self.carga_lista:
            self.boton_finalizar.setEnabled(True)
    
    def recibir_grilla(self, grid):
        if grid:
            self.grilla.show()
        else:
            self.grilla.hide()

    def avanzar(self):
        self.senal_avanzar.emit(self.regiones_seleccionadas)
        filename = QFileDialog.getSaveFileName(self, 'Save file', 
            '',"Image files (*.jpg *.png)")

        self.senal_nombre.emit(filename[0])
    
    def cerrar_ventana(self):
        self.close()
    
    def reiniciar_grafico(self):
        self.regiones_seleccionadas = []
        self.boton_finalizar.setDisabled(True)
        self.seleccion_region.clear()
        
        self.seleccion_region.addItem('Total')
        for region in self.regiones:
            self.seleccion_region.addItem(region)

        pixeles = QPixmap(p.PATH_WHITE)
        pixeles = pixeles.scaled(p.VENTANA_ANCHO * 64 / 100, p.VENTANA_ANCHO * 32 / 100, Qt.IgnoreAspectRatio)
        self.label_blanco.setPixmap(pixeles)

        pixeles = QPixmap(p.PATH_BIG_GRID)
        pixeles = pixeles.scaled(p.VENTANA_ANCHO * 64 / 100, p.VENTANA_ANCHO * 32 / 100, Qt.IgnoreAspectRatio)
        self.grilla.setPixmap(pixeles)
        self.boton_color.setStyleSheet(p.ESTILO_BOTON_REGION)
        
    def volver(self):
        self.senal_volver.emit()
        self.grilla.hide()
        self.close()

    def activar_boton(self):
        self.carga_lista = True
        if len(self.regiones_seleccionadas) > 0:
            self.boton_finalizar.setEnabled(True)

    def mostrar_ventana(self, grid):
        self.grid = grid
        self.regiones_seleccionadas = []
        self.init_gui()
        self.recibir_grilla(grid)
        self.show()