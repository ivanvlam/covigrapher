from os.path import join

# Archivos
PATH_LOGO = join("frontend", "assets", "logo.png")
PATH_GRADIENTE = join("frontend", "assets", "gradiente.gif")
PATH_GRID = join("frontend", "assets", "grid.png")
PATH_BIG_GRID = join("frontend", "assets", "Big_grid.png")
PATH_LOGO_COMPLETO = join("frontend", "assets", "logo_completo.png")
PATH_WHITE = join("frontend", "assets", "white.png")

# Títulos
PATH_PERIODO_TITLE = join('frontend', 'assets', 'titles', 'Seleccionar_periodo.png')
PATH_INDICADOR_TITLE = join('frontend', 'assets', 'titles', 'Seleccionar_indicador.png')
PATH_PREDEFINIDO_TITLE = join('frontend', 'assets', 'titles', 'Seleccionar_predefinido.png')
PATH_GRILLA_TITLE = join('frontend', 'assets', 'titles', 'Grilla.png')
PATH_PROMEDIO_MOVIL_TITLE = join('frontend', 'assets', 'titles', 'Promedio_movil.png')
PATH_TAMANO_VENTANA_TITLE = join('frontend', 'assets', 'titles', 'Tamano_ventana.png')
PATH_INICIO_TITLE = join('frontend', 'assets', 'titles', 'Inicio.png')
PATH_DURACION_TITLE = join('frontend', 'assets', 'titles', 'Duracion.png')
PATH_DIAS_TITLE = join('frontend', 'assets', 'titles', 'Dias.png')
PATH_OPCIONES_GRAFICAS_TITLE = join('frontend', 'assets', 'titles', 'Opciones_graficas.png')
PATH_7_DIAS_TITLE = join('frontend', 'assets', 'titles', '7_dias.png')
PATH_HOY_TITLE = join('frontend', 'assets', 'titles', 'Hoy.png')
PATH_REGION_TITLE = join('frontend', 'assets', 'titles', 'Agregar_region.png')
PATH_PREVISUALIZACION_TITLE = join('frontend', 'assets', 'titles', 'Previsualizacion.png')
PATH_POR_HAB_TITLE = join('frontend', 'assets', 'titles', 'Por_100_hab.png')

# Números
PATH_NUMERO_1 = join('frontend', 'assets', 'titles', 'Numero_1.png')
PATH_NUMERO_5 = join('frontend', 'assets', 'titles', 'Numero_5.png')
PATH_NUMERO_10 = join('frontend', 'assets', 'titles', 'Numero_10.png')
PATH_NUMERO_15 = join('frontend', 'assets', 'titles', 'Numero_15.png')
PATH_NUMERO_20 = join('frontend', 'assets', 'titles', 'Numero_20.png')
PATH_NUMERO_25 = join('frontend', 'assets', 'titles', 'Numero_25.png')
PATH_NUMERO_30 = join('frontend', 'assets', 'titles', 'Numero_30.png')

# Ventana
VENTANA_ANCHO = 640
VENTANA_ALTO = 720

# Datos
REGIONES = [
    'Arica y Parinacota',
    'Tarapacá',
    'Antofagasta',
    'Atacama',
    'Coquimbo',
    'Valparaíso',
    'Metropolitana',
    'O’Higgins',
    'Maule',
    'Ñuble',
    'Biobío',
    'Araucanía',
    'Los Ríos',
    'Los Lagos',
    'Aysén',
    'Magallanes'
]

POBLACION = {
    'Arica y Parinacota':255_068,
    'Tarapacá': 391_558,
    'Antofagasta':703_534,
    'Atacama':316_168,
    'Coquimbo':848_079,
    'Valparaíso':1_979_373,
    'Metropolitana':8_242_459,
    'O’Higgins':1_000_959,
    'Maule':1_143_012,
    'Ñuble':514_609,
    'Biobío':1_670_590,
    'Araucanía':1_019_548,
    'Los Ríos':407_837,
    'Los Lagos':897_708,
    'Aysén':107_158,
    'Magallanes':179_533
}

POBLACION['Total'] = sum(POBLACION.values())
# Fuente: Wikipedia


# Estilos
ESTILO_BOTON = '''
    background-color: rgb(213, 225, 232);
    border-style: outset;
    border-width: 3px;
    border-radius: 15px;
    border-color: black;
    padding: 6px;
'''

ESTILO_BOTON_REINICIAR = '''
    background-color: rgb(247, 143, 145);
    border-style: outset;
    border-width: 3px;
    border-radius: 15px;
    border-color: black;
    padding: 6px;
    color: black;
'''

ESTILO_BOTON_FINALIZAR = '''
    background-color: rgb(144, 244, 159);
    border-style: outset;
    border-width: 3px;
    border-radius: 15px;
    border-color: black;
    padding: 6px;
    color: black;
'''

ESTILO_BOTON_REGION = '''
    background-color: black;
    border-style: outset;
    border-width: 3px;
    border-radius: 15px;
    border-color: black;
    padding: 6px;
    color: rgb(213, 225, 232);
'''

ESTILO_SLIDER = '''
    QSlider::handle:horizontal {
    background: solid black;
    border: 1px solid #5c5c5c;
    width: 10px;
    margin: -2px 0;
    border-radius: 6px;
}'''

ESTILO_CALENDARIO = '''
    border-width: 1px;
    border-color: black;
    color: black;
'''

ESTILO_LABEL_SELECCION = '''
    background-color : rgb(213, 225, 232);
    border-style: solid;
    border-width: 3px;
    border-radius: 20px;
    border-color: black;
'''
