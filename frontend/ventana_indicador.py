from PyQt5.QtWidgets import QLabel, QWidget, QPushButton, QComboBox, QSlider
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QPixmap, QFont, QIcon, QMovie
import parametros as p


class VentanaIndicador(QWidget):

    senal_volver = pyqtSignal()
    senal_avanzar = pyqtSignal(dict)
    senal_grilla = pyqtSignal(bool)

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

        self.top_label = QLabel(self)
        self.top_label.setFixedWidth(p.VENTANA_ANCHO * 94 / 100)
        self.top_label.setFixedHeight(p.VENTANA_ALTO * 25 / 100)
        self.top_label.setStyleSheet(p.ESTILO_LABEL_SELECCION)
        self.top_label.move(p.VENTANA_ANCHO * 3 / 100, p.VENTANA_ALTO * 4 / 100)

        self.label_indicador_text = QLabel(self)
        self.label_indicador_text.resize(p.VENTANA_ANCHO * 96 / 100, p.VENTANA_ALTO / 7)
        self.label_indicador_text.setPixmap(QPixmap(p.PATH_INDICADOR_TITLE))
        self.label_indicador_text.move(
            self.top_label.x(), 
            self.top_label.y()
        )
        self.label_indicador_text.setAlignment(Qt.AlignCenter)

        self.linea_1 = QLabel(self)
        self.linea_1.resize(2, 80)
        self.linea_1.move(p.VENTANA_ANCHO * 60 / 100, p.VENTANA_ALTO * 15 / 100)
        self.linea_1.setStyleSheet("background: 2px solid black;")

        self.label_por_hab_text = QLabel(self)
        self.label_por_hab_text.resize(p.VENTANA_ANCHO * 40 / 100, p.VENTANA_ALTO / 7)
        self.label_por_hab_text.setPixmap(QPixmap(p.PATH_POR_HAB_TITLE))
        self.label_por_hab_text.move(
            self.top_label.x() + p.VENTANA_ANCHO * 63 / 100, 
            self.top_label.y() + p.VENTANA_ALTO * 7 / 100
        )

        self.seleccion_por_hab = QComboBox(self)
        self.seleccion_por_hab.resize(p.VENTANA_ANCHO * 30 / 100, 35)
        self.seleccion_por_hab.addItem('Desactivado')
        self.seleccion_por_hab.addItem('Activado')

        self.seleccion_por_hab.setEditable(True)
        line_edit = self.seleccion_por_hab.lineEdit()
        line_edit.setAlignment(Qt.AlignCenter)
        line_edit.setReadOnly(True)
        
        self.seleccion_por_hab.setFont(QFont('Courier', 11, QFont.Light))
        self.seleccion_por_hab.move(p.VENTANA_ANCHO * 63 / 100, p.VENTANA_ALTO * 20 / 100)

        self.seleccion_indicador = QComboBox(self)
        self.seleccion_indicador.resize(p.VENTANA_ANCHO * 50 / 100, 45)
        self.seleccion_indicador.addItem('Casos acumulados')
        self.seleccion_indicador.addItem('Casos nuevos totales')
        self.seleccion_indicador.addItem('Casos nuevos con sintomas')
        self.seleccion_indicador.addItem('Casos nuevos sin sintomas')
        self.seleccion_indicador.addItem('Fallecidos totales')
        self.seleccion_indicador.addItem('Casos activos confirmados')

        self.seleccion_indicador.setEditable(True)
        line_edit = self.seleccion_indicador.lineEdit()
        line_edit.setAlignment(Qt.AlignCenter)
        line_edit.setReadOnly(True)
        
        self.seleccion_indicador.setFont(QFont('Courier', 12, QFont.Light))
        self.seleccion_indicador.move(p.VENTANA_ANCHO * 6 / 100, p.VENTANA_ALTO * 17.5 / 100)


        self.bottom_label = QLabel(self)
        self.bottom_label.setFixedWidth(p.VENTANA_ANCHO * 94 / 100)
        self.bottom_label.setFixedHeight(p.VENTANA_ALTO * 52 / 100)
        self.bottom_label.setStyleSheet(p.ESTILO_LABEL_SELECCION)
        self.bottom_label.move(p.VENTANA_ANCHO * 3 / 100, p.VENTANA_ALTO * 33 / 100)
        
        self.label_opciones_graficas_text = QLabel(self)
        self.label_opciones_graficas_text.resize(p.VENTANA_ANCHO * 96 / 100, p.VENTANA_ALTO / 8)
        self.label_opciones_graficas_text.setPixmap(QPixmap(p.PATH_OPCIONES_GRAFICAS_TITLE))
        self.label_opciones_graficas_text.move(
            self.bottom_label.x(), 
            self.bottom_label.y() + 5
        )
        self.label_opciones_graficas_text.setAlignment(Qt.AlignCenter)

        self.label_grilla_text = QLabel(self)
        self.label_grilla_text.resize(p.VENTANA_ANCHO * 32 / 100, p.VENTANA_ALTO / 7)
        self.label_grilla_text.setPixmap(QPixmap(p.PATH_GRILLA_TITLE))
        self.label_grilla_text.move(
            self.bottom_label.x() + p.VENTANA_ANCHO * 1.5 / 100,
            self.bottom_label.y() + p. VENTANA_ALTO * 9 / 100
        )
        self.label_grilla_text.setAlignment(Qt.AlignCenter)

        self.activacion_grilla = QComboBox(self)
        self.activacion_grilla.resize(p.VENTANA_ANCHO * 28 / 100, 35)
        self.activacion_grilla.addItem('Activada')
        self.activacion_grilla.addItem('Desactivada')

        self.activacion_grilla.setEditable(True)
        line_edit = self.activacion_grilla.lineEdit()
        line_edit.setAlignment(Qt.AlignCenter)
        line_edit.setReadOnly(True)
        
        self.activacion_grilla.setFont(QFont('Courier', 12, QFont.Light))
        self.activacion_grilla.move(p.VENTANA_ANCHO * 5 / 100, p.VENTANA_ALTO * 53 / 100)

        self.activacion_grilla.currentIndexChanged.connect(self.mostrar_grilla)

        self.imagen_grilla = QLabel(self)
        self.imagen_grilla.resize(p.VENTANA_ANCHO * 24 / 100, p.VENTANA_ANCHO * 24 / 100)
        self.imagen_grilla.setPixmap(QPixmap(p.PATH_GRID))
        self.imagen_grilla.move(p.VENTANA_ANCHO * 7.5 / 100, p.VENTANA_ALTO * 60.5 / 100)
        self.imagen_grilla.setScaledContents(True)

        self.linea_2 = QLabel(self)
        self.linea_2.resize(2, 260)
        self.linea_2.move(p.VENTANA_ANCHO * 36 / 100, p.VENTANA_ALTO * 46 / 100)
        self.linea_2.setStyleSheet("background: 2px solid black;")


        self.label_promedio_movil_text = QLabel(self)
        self.label_promedio_movil_text.resize(p.VENTANA_ANCHO * 62 / 100, p.VENTANA_ALTO / 8)
        self.label_promedio_movil_text.setPixmap(QPixmap(p.PATH_PROMEDIO_MOVIL_TITLE))
        self.label_promedio_movil_text.move(
            self.bottom_label.x() + p.VENTANA_ANCHO * 34 / 100,
            self.bottom_label.y() + p.VENTANA_ALTO * 10 / 100
        )
        self.label_promedio_movil_text.setAlignment(Qt.AlignCenter)

        self.activacion_promedio_movil = QComboBox(self)
        self.activacion_promedio_movil.resize(p.VENTANA_ANCHO * 34 / 100, 35)
        self.activacion_promedio_movil.addItem('Desactivado')
        self.activacion_promedio_movil.addItem('Activado')

        self.activacion_promedio_movil.setEditable(True)
        line_edit = self.activacion_promedio_movil.lineEdit()
        line_edit.setAlignment(Qt.AlignCenter)
        line_edit.setReadOnly(True)
        
        self.activacion_promedio_movil.setFont(QFont('Courier', 12, QFont.Light))
        self.activacion_promedio_movil.move(p.VENTANA_ANCHO * 50.5 / 100, p.VENTANA_ALTO * 52.5 / 100)

        self.activacion_promedio_movil.currentIndexChanged.connect(self.revisar_promedio)

        self.label_tamano_ventana_text = QLabel(self)
        self.label_tamano_ventana_text.resize(p.VENTANA_ANCHO * 40 / 100, p.VENTANA_ALTO / 8)
        self.label_tamano_ventana_text.setPixmap(QPixmap(p.PATH_TAMANO_VENTANA_TITLE))
        self.label_tamano_ventana_text.move(
            self.bottom_label.x() + p.VENTANA_ANCHO * 45 / 100,
            self.bottom_label.y() + p.VENTANA_ALTO * 24 / 100
        )
        self.label_tamano_ventana_text.setAlignment(Qt.AlignCenter)
        
        self.slider_ventana = QSlider(Qt.Horizontal, self)
        self.slider_ventana.setMinimum(0)
        self.slider_ventana.setMaximum(30)
        self.slider_ventana.setValue(0)
        self.slider_ventana.setTickPosition(QSlider.TicksBelow)
        self.slider_ventana.setTickInterval(5)
        self.slider_ventana.setStyleSheet(p.ESTILO_SLIDER)
        self.slider_ventana.resize(p.VENTANA_ANCHO * 50 / 100, 50)
        self.slider_ventana.move(
            self.bottom_label.x() + p.VENTANA_ANCHO * 38 / 100, 
            self.bottom_label.y() + p.VENTANA_ALTO * 32 / 100
        )
        self.slider_ventana.setDisabled(True)
        self.slider_ventana.valueChanged.connect(self.cambiar_dias)
        
        self.label_numero_1 = QLabel(self)
        self.label_numero_1.resize(25, 25)
        self.label_numero_1.setPixmap(QPixmap(p.PATH_NUMERO_1))
        self.label_numero_1.move(
            self.bottom_label.x() + p.VENTANA_ANCHO * 38.75 / 100, 
            self.bottom_label.y() + p.VENTANA_ALTO * 38 / 100
        )
        
        self.label_numero_5 = QLabel(self)
        self.label_numero_5.resize(25, 25)
        self.label_numero_5.setPixmap(QPixmap(p.PATH_NUMERO_5))
        self.label_numero_5.move(
            self.bottom_label.x() + p.VENTANA_ANCHO * 46.25 / 100, 
            self.bottom_label.y() + p.VENTANA_ALTO * 38 / 100
        )
        
        self.label_numero_10 = QLabel(self)
        self.label_numero_10.resize(25, 25)
        self.label_numero_10.setPixmap(QPixmap(p.PATH_NUMERO_10))
        self.label_numero_10.move(
            self.bottom_label.x() + p.VENTANA_ANCHO * 53.5 / 100, 
            self.bottom_label.y() + p.VENTANA_ALTO * 38 / 100
        )
        
        self.label_numero_15 = QLabel(self)
        self.label_numero_15.resize(25, 25)
        self.label_numero_15.setPixmap(QPixmap(p.PATH_NUMERO_15))
        self.label_numero_15.move(
            self.bottom_label.x() + p.VENTANA_ANCHO * 61.75 / 100, 
            self.bottom_label.y() + p.VENTANA_ALTO * 38 / 100
        )
        
        self.label_numero_20 = QLabel(self)
        self.label_numero_20.resize(25, 25)
        self.label_numero_20.setPixmap(QPixmap(p.PATH_NUMERO_20))
        self.label_numero_20.move(
            self.bottom_label.x() + p.VENTANA_ANCHO * 69.75 / 100, 
            self.bottom_label.y() + p.VENTANA_ALTO * 38 / 100
        )
        
        self.label_numero_25 = QLabel(self)
        self.label_numero_25.resize(25, 25)
        self.label_numero_25.setPixmap(QPixmap(p.PATH_NUMERO_25))
        self.label_numero_25.move(
            self.bottom_label.x() + p.VENTANA_ANCHO * 77.5 / 100, 
            self.bottom_label.y() + p.VENTANA_ALTO * 38 / 100
        )
        
        self.label_numero_30 = QLabel(self)
        self.label_numero_30.resize(25, 25)
        self.label_numero_30.setPixmap(QPixmap(p.PATH_NUMERO_30))
        self.label_numero_30.move(
            self.bottom_label.x() + p.VENTANA_ANCHO * 85.5 / 100, 
            self.bottom_label.y() + p.VENTANA_ALTO * 38 / 100
        )

        self.label_dias = QLabel('Promedio móvil desactivado', self)
        self.label_dias.resize(p.VENTANA_ANCHO * 60 / 100, 35)
        self.label_dias.setFont(QFont('Courier', 13, QFont.Bold))
        self.label_dias.move(
            self.bottom_label.x() + p.VENTANA_ANCHO * 33.5 / 100,
            self.bottom_label.y() + p.VENTANA_ALTO * 43 / 100
        )
        self.label_dias.setAlignment(Qt.AlignCenter)
        

        self.boton_volver = QPushButton('&Volver', self)
        self.boton_volver.resize(p.VENTANA_ANCHO * 30 / 100, p.VENTANA_ALTO * 7 / 100)
        self.boton_volver.clicked.connect(self.volver)
        self.boton_volver.setFont(QFont('Courier', 22, QFont.Bold))
        self.boton_volver.move(p.VENTANA_ANCHO * 3 / 100, p.VENTANA_ALTO * 89 / 100)
        self.boton_volver.setStyleSheet(p.ESTILO_BOTON)

        self.boton_continuar = QPushButton('&Continuar', self)
        self.boton_continuar.resize(p.VENTANA_ANCHO * 60 / 100, p.VENTANA_ALTO * 7 / 100)
        self.boton_continuar.clicked.connect(self.avanzar)
        self.boton_continuar.setFont(QFont('Courier', 22, QFont.Bold))
        self.boton_continuar.move(p.VENTANA_ANCHO * 37 / 100, p.VENTANA_ALTO * 89 / 100)
        self.boton_continuar.setStyleSheet(p.ESTILO_BOTON)
    
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
            self.label_dias.setText('Promedio móvil desactivado')
        else:
            self.slider_ventana.setEnabled(True)
            self.cambiar_dias()
    
    def cambiar_dias(self):
        valor = self.slider_ventana.value()
        if valor in [0, 1]:
            self.label_dias.setText('Ventana de 1 día')
        else:
            self.label_dias.setText(f'Ventana de {valor} días')
    
    def avanzar(self):
        indicador = self.seleccion_indicador.currentText()
        grilla = self.activacion_grilla.currentIndex()
        promedio_movil = self.activacion_promedio_movil.currentIndex()
        por_hab = self.seleccion_por_hab.currentIndex()
        tamano_ventana = self.slider_ventana.value()

        self.senal_avanzar.emit({
            'indicador': indicador,
            'grilla': grilla,
            'promedio_movil': promedio_movil,
            'tamano_ventana': max(1, tamano_ventana),
            'por_hab': por_hab
        })
        self.senal_grilla.emit(not bool(grilla))
        self.close()
    
    def reiniciar_labels(self):
        self.seleccion_indicador.setCurrentIndex(0)
        self.activacion_grilla.setCurrentIndex(0)
        self.activacion_promedio_movil.setCurrentIndex(0)
        self.slider_ventana.setValue(0)

    def volver(self):
        self.senal_volver.emit()
        self.close()

    def mostrar_ventana(self):
        self.show()