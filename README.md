# <span style="font-family:Bebas Neue; font-size:2em;">COVIGRAPHER</span>

## Indice
- [Introducción](#Introducción)
- [Uso](#Uso)
- [Por hacer](#Por-hacer)
- [Fuentes de los datos](Fuentes-de-los-datos)

---

## Introducción

Ante la emergencia sanitaria actual, surge la necesidad de visualizar la gran cantidad de datos recopilados día a día. Ante esta necesidad, nace covigrapher, que permite generar tus propios gráficos estadísticos del COVID-19 en Chile con varias opciones de personalización, desde el periodo de visualización hasta opciones gráficas, todo mediante una interfaz amigable con el usuario desarrollada con *PyQt5*.

---

## Uso

Para generar un gráfico se debe ejecutar el programa `main.py` y seguir los siguientes pasos:

* Iniciar el programa
* Seleccionar periodo de visualización manualmente o mediante un predefinido
* Seleccionar un indicador estadístico
* Seleccionar si se quiere visualizar la información por 100.000 habitantes o en su totalidad, la presencia de grilla y la utilización de promedio móvil, para este último se debe agregar el tamaño de la ventana
* Agregar región por región, cada una con el color de preferencia del usuario
* Finalizar el gráfico y guargar como archivo `.jpg` o `.png` en el directorio deseado

---

## Por hacer
Lo que falta implementar en covigrapher es:

* Ventana Final que permita al usuario generar otro gráfico
* Opción de generar gráficos predeterminados
* `covigrapher.exe`

---

## Fuentes de los datos

* Población por región obtenida de [Wikipedia](https://es.wikipedia.org/wiki/Anexo:Regiones_de_Chile_por_poblaci%C3%B3n).
* Datos diarios obtenidos del [repositorio](https://github.com/MinCiencia/Datos-COVID19) de COVID-19 del Ministerio de Ciencia, Tecnología, Conocimiento, e Innovación. 
