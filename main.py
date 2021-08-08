import sys
from PyQt5.QtWidgets import QApplication
from frontend.ventana_inicio import VentanaInicio
from frontend.ventana_periodo import VentanaPeriodo
from frontend.ventana_indicador import VentanaIndicador
from frontend.ventana_agregar_region import VentanaAgregarRegion
from backend.logica import Logica

def hook(type_error, traceback):
    print(type_error)
    print(traceback)

if __name__ == '__main__':

    sys.__excepthook__ = hook
    app = QApplication(sys.argv)
    
    ventana_inicio = VentanaInicio()
    ventana_periodo = VentanaPeriodo()
    ventana_indicador = VentanaIndicador()
    ventana_agregar_region = VentanaAgregarRegion()
    logica = Logica()
    
    ventana_inicio.show()

    logica.senal_carga_lista.connect(ventana_agregar_region.activar_boton)
    logica.senal_terminar.connect(ventana_agregar_region.cerrar_ventana)

    ventana_inicio.senal_avanzar.connect(ventana_periodo.mostrar_ventana)
    ventana_inicio.senal_labels.connect(ventana_periodo.reiniciar_labels)
    ventana_inicio.senal_labels.connect(ventana_indicador.reiniciar_labels)
    
    ventana_periodo.senal_volver.connect(ventana_inicio.mostrar_ventana)
    ventana_periodo.senal_avanzar.connect(ventana_indicador.mostrar_ventana)
    ventana_periodo.senal_avanzar.connect(logica.guardar_periodo)

    ventana_indicador.senal_volver.connect(ventana_periodo.mostrar_ventana)
    ventana_indicador.senal_avanzar.connect(logica.guardar_indicador)
    ventana_indicador.senal_grilla.connect(ventana_agregar_region.mostrar_ventana)

    ventana_agregar_region.senal_volver.connect(ventana_indicador.mostrar_ventana)
    ventana_agregar_region.senal_avanzar.connect(logica.generar_grafico)
    ventana_agregar_region.senal_nombre.connect(logica.guardar_archivo)

    sys.exit(app.exec_())