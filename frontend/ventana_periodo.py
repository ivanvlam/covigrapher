from PyQt5.QtWidgets import QLabel, QWidget, QPushButton, QComboBox, QSlider, QCalendarWidget
from PyQt5.QtCore import pyqtSignal, Qt, QDate
from PyQt5.QtGui import QPixmap, QFont, QIcon, QMovie
import parametros as p


class VentanaPeriodo(QWidget):

    senal_volver = pyqtSignal()
    senal_avanzar = pyqtSignal(dict)

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

        self.main_label = QLabel(self)
        self.main_label.setFixedWidth(p.VENTANA_ANCHO * 94 / 100)
        self.main_label.setFixedHeight(p.VENTANA_ALTO * 81 / 100)
        self.main_label.setStyleSheet(p.ESTILO_LABEL_SELECCION)
        self.main_label.move(p.VENTANA_ANCHO * 3 / 100, p.VENTANA_ALTO * 4 / 100)

        self.label_periodo_text = QLabel(self)
        self.label_periodo_text.resize(p.VENTANA_ANCHO * 96 / 100, p.VENTANA_ALTO / 8)
        self.label_periodo_text.setPixmap(QPixmap(p.PATH_PERIODO_TITLE))
        self.label_periodo_text.move(
            self.main_label.x(), 
            self.main_label.y()
        )
        self.label_periodo_text.setAlignment(Qt.AlignCenter)

        self.label_incio_text = QLabel(self)
        self.label_incio_text.resize(p.VENTANA_ANCHO * 30 / 100, p.VENTANA_ALTO / 8)
        self.label_incio_text.setPixmap(QPixmap(p.PATH_INICIO_TITLE))
        self.label_incio_text.move(
            self.main_label.x() + p.VENTANA_ANCHO * 9 / 100, 
            self.main_label.y() + p.VENTANA_ALTO * 23 /  100
        )
        self.fecha_inicio = QDate(2020, 3, 3)
        self.hoy = QDate.currentDate()
        self.dias_totales = self.fecha_inicio.daysTo(self.hoy)
        
        self.calendario = QCalendarWidget(self)
        self.calendario.setGridVisible(True)
        self.calendario.move(p.VENTANA_ANCHO * 33 / 100, p.VENTANA_ALTO * 15 / 100)
        self.calendario.setMinimumDate(self.fecha_inicio)
        self.calendario.setMaximumDate(self.hoy.addDays(-7))
        self.calendario.setStyleSheet(p.ESTILO_CALENDARIO)
        self.calendario.setFont(QFont('Courier', 9, QFont.Bold))
        self.calendario.setSelectedDate(self.fecha_inicio)
        self.calendario.clicked.connect(self.cambiar_dias)
        self.calendario.clicked.connect(self.cambiar_a_personalizado)

        self.label_duracion_text = QLabel(self)
        self.label_duracion_text.resize(p.VENTANA_ANCHO * 30 / 100, p.VENTANA_ALTO / 8)
        self.label_duracion_text.setPixmap(QPixmap(p.PATH_DURACION_TITLE))
        self.label_duracion_text.move(
            self.main_label.x() + p.VENTANA_ANCHO * 2 / 100, 
            self.main_label.y() + p.VENTANA_ALTO * 45 / 100
        )

        self.slider_duracion = QSlider(Qt.Horizontal, self)
        self.slider_duracion.setMinimum(7)
        self.slider_duracion.setMaximum(self.dias_totales)
        self.slider_duracion.setValue(7)
        self.slider_duracion.setTickPosition(QSlider.TicksBelow)
        self.slider_duracion.setTickInterval(14)
        self.slider_duracion.setStyleSheet(p.ESTILO_SLIDER)
        self.slider_duracion.resize(p.VENTANA_ANCHO * 58 / 100, 50)
        self.slider_duracion.move(
            self.main_label.x() + p.VENTANA_ANCHO * 32 / 100, 
            self.main_label.y() + p.VENTANA_ALTO * 47 / 100
        )
        self.slider_duracion.valueChanged.connect(self.cambiar_dias)
        self.slider_duracion.sliderMoved.connect(self.cambiar_a_personalizado)

        self.label_7_dias = self.label_promedio_movil_text = QLabel(self)
        self.label_7_dias.resize(50, 25)
        self.label_7_dias.setPixmap(QPixmap(p.PATH_7_DIAS_TITLE))
        self.label_7_dias.move(
            self.main_label.x() + p.VENTANA_ANCHO * 29.5 / 100, 
            self.main_label.y() + p.VENTANA_ALTO * 53.5 / 100
        )

        self.label_hoy = self.label_promedio_movil_text = QLabel(self)
        self.label_hoy.resize(30, 25)
        self.label_hoy.setPixmap(QPixmap(p.PATH_HOY_TITLE))
        self.label_hoy.move(
            self.main_label.x() + p.VENTANA_ANCHO * 86.75 / 100, 
            self.main_label.y() + p.VENTANA_ALTO * 53.5 / 100
        )

        self.label_dias = QLabel('Seleccionar fecha y duración', self)
        self.label_dias.resize(p.VENTANA_ANCHO * 86 / 100, 35)
        self.label_dias.setFont(QFont('Courier', 13, QFont.Bold))
        self.label_dias.move(
            self.main_label.x() + p.VENTANA_ANCHO * 4 / 100, 
            self.main_label.y() + p.VENTANA_ALTO * 56.5 / 100
        )
        self.label_dias.setAlignment(Qt.AlignCenter)

        self.linea = QLabel(self)
        self.linea.resize(p.VENTANA_ANCHO * 90 / 100, 2)
        self.linea.move(p.VENTANA_ANCHO * 5 / 100, p.VENTANA_ALTO * 66 / 100)
        self.linea.setStyleSheet("background: 2px solid black;")

        self.label_periodo_text = QLabel(self)
        self.label_periodo_text.resize(p.VENTANA_ANCHO * 96 / 100, p.VENTANA_ALTO / 8)
        self.label_periodo_text.setPixmap(QPixmap(p.PATH_PREDEFINIDO_TITLE))
        self.label_periodo_text.move(
            self.main_label.x() - 4, 
            self.main_label.y() + p.VENTANA_ANCHO * 70 / 100
        )
        self.label_periodo_text.setAlignment(Qt.AlignCenter)

        self.seleccion_predefinido = QComboBox(self)
        self.seleccion_predefinido.resize(p.VENTANA_ANCHO * 80 / 100, 35)
        self.seleccion_predefinido.addItem('Personalizado')
        self.seleccion_predefinido.addItem('Última semana')
        self.seleccion_predefinido.addItem('Último mes')
        self.seleccion_predefinido.addItem('Último año')
        self.seleccion_predefinido.addItem('Peak Junio 2020')
        self.seleccion_predefinido.addItem('Peak Abril 2021')
        self.seleccion_predefinido.addItem('Peak Junio 2021')

        self.seleccion_predefinido.setEditable(True)
        line_edit = self.seleccion_predefinido.lineEdit()
        line_edit.setAlignment(Qt.AlignCenter)
        line_edit.setReadOnly(True)
        
        self.seleccion_predefinido.setFont(QFont('Courier', 11, QFont.Light))
        self.seleccion_predefinido.move(p.VENTANA_ANCHO * 10 / 100, p.VENTANA_ALTO * 76.5 / 100)

        self.seleccion_predefinido.currentIndexChanged.connect(self.cambiar_datos)

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

    def cambiar_dias(self):
        self.duracion_seleccionada = self.slider_duracion.value()

        self.fecha_cal = self.calendario.selectedDate()
        fecha_str = self.fecha_cal.toString(Qt.ISODate).split('-')
        agno_inicial, mes_inicial, dia_inicial = fecha_str[0], fecha_str[1], fecha_str[2]
        
        fecha_final = self.fecha_cal.addDays(self.duracion_seleccionada)

        if self.duracion_seleccionada == self.dias_totales or self.hoy.daysTo(fecha_final) >= 0:
            self.label_dias.setText(f'Desde el {dia_inicial}/{mes_inicial}/{agno_inicial} hasta hoy')
        else:
            fecha_final_str = fecha_final.toString(Qt.ISODate).split('-')
            agno_final, mes_final, dia_final = fecha_final_str[0], fecha_final_str[1], fecha_final_str[2]
            self.label_dias.setText(f'Desde el {dia_inicial}/{mes_inicial}/{agno_inicial} ' \
                f'hasta el {dia_final}/{mes_final}/{agno_final}')
        
        self.slider_duracion.setMaximum(self.fecha_cal.daysTo(self.hoy))
        self.slider_duracion.setValue(min(self.fecha_cal.daysTo(self.hoy), self.duracion_seleccionada))

    def cambiar_datos(self):
        opcion = self.seleccion_predefinido.currentText()

        if opcion == 'Personalizado':
            self.calendario.setSelectedDate(self.fecha_cal)
            self.slider_duracion.setValue(self.duracion_seleccionada)
        
        elif opcion == 'Última semana':
            self.calendario.setSelectedDate(self.hoy.addDays(-7))
            self.slider_duracion.setMaximum(self.calendario.selectedDate().daysTo(self.hoy))
            self.slider_duracion.setValue(7)
        
        elif opcion == 'Último mes':
            mes_pasado = self.hoy.addMonths(-1)
            self.calendario.setSelectedDate(mes_pasado)
            self.slider_duracion.setMaximum(self.calendario.selectedDate().daysTo(self.hoy))
            self.slider_duracion.setValue(mes_pasado.daysTo(self.hoy))
        
        elif opcion == 'Último año':
            agno_pasado = self.hoy.addYears(-1)
            self.calendario.setSelectedDate(agno_pasado)
            self.slider_duracion.setMaximum(self.calendario.selectedDate().daysTo(self.hoy))
            self.slider_duracion.setValue(agno_pasado.daysTo(self.hoy))

        elif opcion == 'Peak Junio 2020':
            inicio = QDate(2020, 5, 16)
            self.calendario.setSelectedDate(inicio)
            self.slider_duracion.setMaximum(self.calendario.selectedDate().daysTo(self.hoy))
            self.slider_duracion.setValue(inicio.daysTo(QDate(2020, 7, 1)))

        elif opcion == 'Peak Abril 2021':
            inicio = QDate(2021, 3, 15)
            self.calendario.setSelectedDate(inicio)
            self.slider_duracion.setMaximum(self.calendario.selectedDate().daysTo(self.hoy))
            self.slider_duracion.setValue(inicio.daysTo(QDate(2021, 5, 8)))
            
        elif opcion == 'Peak Junio 2021':
            inicio = QDate(2021, 5, 16)
            self.calendario.setSelectedDate(inicio)
            self.slider_duracion.setMaximum(self.fecha_cal.daysTo(self.hoy))
            self.slider_duracion.setValue(inicio.daysTo(QDate(2021, 7, 1)))
        
        self.cambiar_dias()

    def cambiar_a_personalizado(self):
        self.seleccion_predefinido.setCurrentIndex(0)

    def avanzar(self):
        self.fecha_cal = self.calendario.selectedDate()
        indice_inicial = self.fecha_inicio.daysTo(self.fecha_cal)
        indice_final = indice_inicial + self.slider_duracion.value()

        self.senal_avanzar.emit({
            'indice_inicial': indice_inicial,
            'indice_final': indice_final
        })
        self.close()
    
    def reiniciar_labels(self):
        self.seleccion_predefinido.setCurrentIndex(0)
        self.calendario.setSelectedDate(self.fecha_inicio)
        self.slider_duracion.setValue(7)

    def volver(self):
        self.senal_volver.emit()
        self.close()

    def mostrar_ventana(self):
        self.show()