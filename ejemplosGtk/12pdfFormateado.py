import os

from reportlab.graphics.charts.piecharts import Pie, Pie3d
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.widgets.markers import makeMarker
from reportlab.platypus import Paragraph, Image, SimpleDocTemplate, Spacer
from reportlab.graphics.charts.barcharts import VerticalBarChart, VerticalBarChart3D
from reportlab.graphics.charts.linecharts import LineChart, HorizontalLineChart
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.legends import LineLegend, Legend
from reportlab.graphics.charts.textlabels import Label
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import Table

# Obtener la hoja de estilo predeterminada
hojaEstilo = getSampleStyleSheet()

# Lista para almacenar los elementos del documento
documento = []

# Configuración de la cabecera del documento
cabecera = hojaEstilo['Heading1']
cabecera.pageBreakBefore = 4
cabecera.keepWithNext = 0
cabecera.backColor = colors.blue

# Creación del primer párrafo con la cabecera
parrafo1 = Paragraph("Cabecera del documento", cabecera)
documento.append(parrafo1)

# Cadena de texto larga para el segundo párrafo
cadena = "vinicius balon de oro, vinicius balon de oro, vinicius balon de oro" * 1000

# Estilo del cuerpo del texto
estiloP = hojaEstilo['BodyText']
parrafo2 = Paragraph(cadena, estiloP)
documento.append(parrafo2)

# Añadir un espacio en blanco
documento.append(Spacer(0, 20))

# Comentado: Añadir una imagen al documento
# imagen = Image(os.path.relpath("/home/dam/Imágenes/vinivini.jpg"), width=150, height=150)
# documento.append(imagen)

# Añadir otro espacio en blanco
documento.append(Spacer(0, 20))

# Listas para la tabla de horarios
cabeceira = ['', 'Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
manhana = ['Mañana', 'Estudiar', 'Gimnasio', 'Jugar', 'correr', 'ver al madrid', 'cagar', 'descansar']
tarde = ['Tarde', 'Trabajar', 'Trabajar', 'Cagar', 'Trabajar', 'Trabajar', 'descanso', 'cagar']
Noche = ['Noche', 'descanso', 'Trabajar', 'descanso', 'Trabajar', 'salir', 'descanso', 'furbol']

# Crear la tabla con las listas
tabla = Table([cabeceira, manhana, tarde, Noche])
documento.append(tabla)

# Aplicar diferentes estilos a la tabla
tabla.setStyle([('BACKGROUND', (1, 1), (-1, -1), colors.lightgrey)])  # Fondo de la tabla
tabla.setStyle([('BOX', (1, 1), (-1, -1), 0.5, colors.darkgrey)])  # Caja que engloba la tabla
tabla.setStyle([('INNERGRID', (1, 1), (-1, -1), 0.25, colors.white)])  # Líneas de la tabla
tabla.setStyle([('TEXTCOLOR', (0, 0), (0, -1), colors.red)])  # Texto de la columna izquierda
tabla.setStyle([('TEXTCOLOR', (1, 0), (-1, 0), colors.pink)])  # Texto de la fila superior
tabla.setStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER')])  # Alineación del texto

# Añadir un espacio en blanco
documento.append(Spacer(0, 20))

# Datos para la segunda tabla
datos = [['Esquina sup', '', '02', '03', '04'],
         ['', '', '12', '13', '14'],
         ['20', '21', '22', 'Esquina inf', ''],
         ['30', '31', '32', '', '']]

# Estilos para la segunda tabla
estilo = [('LINEABOVE', (0, 0), (4,0), 1, colors.blue),
          ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.grey),
          ('BACKGROUND', (0, 0), (1, 1), colors.lavenderblush),
          ('SPAN', (0, 0), (1, 1)),
          ('BACKGROUND', (-2, -2), (-1, -1), colors.bisque),
          ('SPAN', (3, 2), (-1, -1)),
          ('LINEBELOW', (0, -1), (-1, -1), 1, colors.blue),
          ('VALIGN', (0,0), (1,1), 'MIDDLE'),
          ('VALIGN', (-2, -2), (-1,-1), 'MIDDLE'),
          ('ALIGN', (0,0), (-1,-1), 'CENTER')]

# Crear la segunda tabla con los datos y estilos
tabla2 = Table(data=datos, style=estilo)
documento.append(tabla2)

# Añadir un espacio en blanco
documento.append(Spacer(0, 20))

# Datos para la tabla de temperaturas
temperaturaTablas = [['','Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dec'],
                     ['Máximas', 15, 16, 20, 25, 27, 31, 35, 38, 33, 25, 20, 18],
                     ['Mínimas', -3, -4, -1, 5, 7, 9, 12, 15, 16, 10, 2, -1]]

# Estilos para la tabla de temperaturas
estiloTablaTemperaturas = [('TEXTCOLOR', (0,0), (-1, 0), colors.grey),
                           ('TEXTCOLOR', (0,1), (0, -1), colors.grey),
                           ('BOX', (1,1), (-1,-1), 1.5, colors.grey),
                           ('INNERGRID', (1,1), (-1, -1), 0.5, colors.grey)]

# Aplicar colores a las celdas según los valores de temperatura
for i, fila in enumerate(temperaturaTablas):
    for j, valor in enumerate(fila):
        if type(valor) == int:
            if valor > 0:
                estiloTablaTemperaturas.append(('TEXTCOLOR', (j,i), (j,i), colors.black))
                if valor > 30:
                    estiloTablaTemperaturas.append(('BACKGROUND', (j,i), (j,i), colors.red))
                elif 30 >= valor > 20:
                    estiloTablaTemperaturas.append(('BACKGROUND', (j,i), (j,i), colors.orange))
                elif 20 >= valor > 10:
                    estiloTablaTemperaturas.append(('BACKGROUND', (j, i), (j, i), colors.lightpink))
                elif 10 >= valor > 0:
                    estiloTablaTemperaturas.append(('BACKGROUND', (j, i), (j, i), colors.lightblue))
            else:
                estiloTablaTemperaturas.append(('TEXTCOLOR', (j, i), (j, i), colors.blue))
                estiloTablaTemperaturas.append(('BACKGROUND', (j, i), (j, i), colors.lightgrey))

# Crear la tabla de temperaturas con los datos y estilos
tabla3 = Table(data = temperaturaTablas, style=estiloTablaTemperaturas)
documento.append(tabla3)

# Añadir un espacio en blanco
documento.append(Spacer(0, 20))

# Crear un gráfico de barras verticales
grafica = VerticalBarChart()
dibujo = Drawing(400, 200)
dibujo.add(grafica)
documento.append(Spacer(0, 20))
documento.append(dibujo)

# Configuración del gráfico de barras
grafica.x = 50
grafica.y = 50
grafica.height = 125
grafica.width = 300
grafica.strokeColor = colors.black  # Esta línea si la dejas en 3D genera error
grafica.valueAxis.valueMin = -10
grafica.valueAxis.valueMax = 50
grafica.valueAxis.valueStep = 5
grafica.categoryAxis.labels.boxAnchor = 'ne'
grafica.categoryAxis.labels.dx = 8
grafica.categoryAxis.labels.dy = -2
grafica.categoryAxis.labels.angle = 30
grafica.categoryAxis.categoryNames = temperaturaTablas[0][1:]
grafica.groupSpacing = 10  # Agrupas los 2 como datos, tanto máxima como mínima pero los separas de los demás
grafica.barSpacing  = 2  # Separación de unidades de enero, febrero...
grafica.bars[0].fillColor = colors.fidred
grafica.bars[1].fillColor = colors.lightblue  # Cambiar el color de la barra
grafica.bars[1].strokeColor = colors.pink  # Color de la línea del gráfico
grafica.data = [temperaturaTablas[1][1:], temperaturaTablas[2][1:]]  # Datos que recibe la gráfica

# Crear un gráfico de líneas horizontales
grafica2 = HorizontalLineChart()
dibujoLineChart = Drawing(400, 200)
dibujoLineChart.add(grafica2)
documento.append(dibujoLineChart)

# Configuración del gráfico de líneas
documento.append(Spacer(0, 20))
grafica2.x = 30
grafica2.y = 50
grafica2.height = 125
grafica2.width = 350
grafica2.data = [temperaturaTablas[1][1:], temperaturaTablas[2][1:]]
grafica2.categoryAxis.categoryNames = temperaturaTablas[0][1:]
grafica2.categoryAxis.labels.boxAnchor = 'ne'
grafica2.valueAxis.valueMin = -10
grafica2.valueAxis.valueMax = 50
grafica2.valueAxis.valueStep = 10
grafica2.lines[0].strokeWidth = 2
grafica2.lines[0].symbol = makeMarker('FilledCircle')
grafica2.lines[1].strokeWidth = 1.5
grafica2.lines[0].strokeColor = colors.red
grafica2.lines[1].strokeColor = colors.blue

# Crear un gráfico de líneas con etiquetas
dibujoPlot = Drawing(400, 200)
etiqueta = Label()
etiqueta.setOrigin(175, 195)
etiqueta.dx = 0
etiqueta.dy = -5
etiqueta.boxStrokeColor = colors.grey
etiqueta.setText("Una grafica\n con 2 series")
dibujoPlot.add(etiqueta)

# Configuración del gráfico de líneas
grafica3 = LinePlot()
dibujoPlot.add(grafica3)
datosPlot = [
    ((1,1), (2,2), (2.5,2), (3,3.5), (4,7)),
    ((1,2), (2,3), (2.5,1), (3.5, 3), (4,2))
]
grafica3.data = datosPlot
grafica3.x = 30
grafica3.y = 50
grafica3.height = 125
grafica3.width = 350
grafica3.joinedLines = 1
grafica3.fillColor = colors.lightsalmon
grafica3.lines[0].symbol = makeMarker('FilledCircle')
grafica3.lines[1].symbol = makeMarker('Triangle')
grafica3.lineLabelFormat = '%2.0f'
grafica3.strokeColor = colors.gray
grafica3.xValueAxis.valueMin = 0
grafica3.xValueAxis.valueMax = 5
grafica3.yValueAxis.valueMin = 0
grafica3.yValueAxis.valueMax = 8
grafica3.yValueAxis.valueSteps = [1,2,3,5,6]
grafica3.lines[0].strokeColor = colors.red
grafica3.lines[1].strokeColor = colors.blue

# Crear una leyenda para el gráfico de líneas
leyenda = LineLegend()
leyenda.fontName = 'Helvetica'
leyenda.fontSize = 7
leyenda.alignment = 'right'
leyenda.x = 30
leyenda.y = 20
leyenda.columnMaximum = 2
etiquetas = ['Caso 1', 'Caso2']
leyenda.colorNamePairs = [(colors.red, etiquetas[0]), (colors.blue, etiquetas[1])]
dibujoPlot.add(leyenda)
documento.append(dibujoPlot)

# Crear un gráfico de tarta en 3D
debuxo = Drawing(300,200)
tarta = Pie3d()
tarta.x=60
tarta.y=15
tarta.width=200
tarta.height=130
tarta.data = [8,6,2,4,7,3]
tarta.labels = ["AD","PMDM","EIE","SXE","DI","PSP"]
tarta.slices.strokeWidth = 0.5
tarta.slices[4].popout = 10
tarta.slices[4].strokeWidth = 2
tarta.slices[4].strokeDashArray = [2,2]
tarta.slices[4].labelRadius = 1.75
tarta.slices.fontColor = colors.red
tarta.sideLabels = 1

# Crear una leyenda para el gráfico de tarta
lenda = Legend()
lenda.x=370
lenda.y=10
lenda.dx=8
lenda.dy=8
lenda.fontName = 'Helvetica'
lenda.fontSize = 8
lenda.boxAnchor = 'n'
lenda.columnMaximum = 10
lenda.strokeWidth = 1
lenda.strokeColor = colors.black
lenda.deltax = 75
lenda.autoXPadding = 5
lenda.yGap = 0
lenda.dxTextSpace = 5
lenda.alignment = 'right'
lenda.dividerLines = 1|2|4
lenda.dividerOffsY = 4.5
lenda.subCols.rpad = 30

# Asignar colores a las porciones de la tarta y añadir la leyenda
cores = [colors.red,colors.blue,colors.green, colors.orange, colors.yellow,colors.lavender ]
for i,colors in enumerate(cores):
    tarta.slices [i].fillColor = colors
    lenda.colorNamePairs = [(tarta.slices[i].fillColor,(tarta.labels[i][0:20],'%0.2f'% tarta.data [i])
                             )for i in range(len (tarta.data))]

# Añadir el gráfico de tarta y la leyenda al dibujo
debuxo.add(tarta)
debuxo.add(lenda)
documento.append(debuxo)

# Crear el documento PDF
doc = SimpleDocTemplate("probaPlatypusTaboa.pdf",pagesize=A4, showBoundary=1)
doc.build(documento)