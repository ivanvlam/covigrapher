from PyQt5.QtCore import pyqtSignal, QObject
import parametros as p
from threading import Thread
from matplotlib import pyplot as plt
import pandas as pd
from datetime import datetime
import os

class Logica(QObject):

    senal_carga_lista = pyqtSignal()
    senal_terminar = pyqtSignal()

    def __init__(self):
        super().__init__()
        
        thread = Thread(target = self.cargar_datos, daemon = True)
        thread.start()
    
    def guardar_periodo(self, diccionario):
        self.indice_inicial = diccionario['indice_inicial']
        self.indice_final = diccionario['indice_final']
    
    def guardar_indicador(self, diccionario):
        self.indicador = diccionario['indicador']
        self.grilla = True if diccionario['grilla'] == 0 else False
        self.promedio_movil = True if diccionario['promedio_movil'] == 1 else False
        self.tamano_ventana = diccionario['tamano_ventana']
        self.por_hab = True if diccionario['por_hab'] == 1 else False
    
    def cargar_datos(self):
        data_path ="https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/"

        csv_path = "producto3/TotalesPorRegion_std.csv"

        path = data_path + csv_path

        # Leemos el archivo csv y creamos el data frame con nuestros datos.
        self.data = pd.read_csv(path ,parse_dates=['Fecha'],
                        date_parser=lambda x: datetime.strptime(x, '%Y-%m-%d'))
        
        self.data['Categoria'].unique()
        self.data.set_index('Fecha', inplace = True)

        self.poblacion_dic = pd.Series(data = p.POBLACION)

        self.senal_carga_lista.emit()


    def generar_grafico(self, regiones):
        fig, ax = plt.subplots(1, 1, figsize=(16, 8))
        ax.set_xlabel('\nFecha\n', fontsize = 18)
        ax.set_ylabel('\n' + self.indicador + '\n', fontsize = 18)

        titulo = self.indicador
        if self.por_hab:
            titulo += ' por 100.000 habitantes'
        
        if self.promedio_movil:
            titulo += ' [Promedio móvil]'

        ax.set_title(titulo, fontsize = 24)

        if self.promedio_movil:
            for elemento in regiones:
                region, color = elemento[0], elemento[1]
                Indices = self.data['Region'] == region
                filtro_region = self.data[Indices] 
                filtro_datos = filtro_region[filtro_region['Categoria'] == self.indicador]
                datos = filtro_datos['Total']

                if self.por_hab:
                    datos *= (100_000 / self.poblacion_dic[region])

                datos_movil = datos.rolling(window = self.tamano_ventana, min_periods = 1).mean()
                
                if region == 'Total':
                    ax.plot(datos_movil[self.indice_inicial:self.indice_final], linewidth = 3.5, color = color, label = 'Total Nacional')
                else:
                    ax.plot(datos_movil[self.indice_inicial:self.indice_final], linewidth = 3.5, color = color, label = region)

        else:
            for elemento in regiones:
                region, color = elemento[0], elemento[1]
                Indices = self.data['Region'] == region
                filtro_region = self.data[Indices] 
                filtro_datos = filtro_region[filtro_region['Categoria'] == self.indicador]
                datos = filtro_datos['Total']

                if self.por_hab:
                    datos *= (100_000 / self.poblacion_dic[region])
                
                if region == 'Total':
                    ax.plot(datos[self.indice_inicial:self.indice_final], linewidth = 3.5, color = color, label = 'Total Nacional')
                else:
                    ax.plot(datos[self.indice_inicial:self.indice_final], linewidth = 3.5, color = color, label = region)
        
        plt.legend(fontsize = 14)
        plt.tight_layout()

        if self.grilla:
            plt.grid(True)
        
        plt.xticks(fontsize = 14)
        plt.yticks(fontsize = 14)

    def guardar_archivo(self, path):
        if path not in ['.png', 'jpg']:
            plt.savefig(path)

        if os.path.exists(".png"):
            os.remove(".png")

        self.senal_terminar.emit()

