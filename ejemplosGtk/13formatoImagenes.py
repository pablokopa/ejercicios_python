from reportlab.graphics.shapes import Drawing, Image
from reportlab.graphics import renderPDF
from reportlab.lib.pagesizes import A4

# Crear una lista para almacenar los dibujos
guion = []

# Crear una imagen con las coordenadas (0,0), tamaño (512,233) y el archivo "foto2.png"
imaxe = Image(0, 0, 512, 233, "foto.png")

# Crear un dibujo y añadir la imagen
debuxo = Drawing(50, 30)
debuxo.add(imaxe)
debuxo.translate(0, 300)  # Trasladar el dibujo
guion.append(debuxo)  # Añadir el dibujo a la lista

# Crear otro dibujo, añadir la imagen y aplicar transformaciones
debuxo = Drawing(50, 30)
debuxo.add(imaxe)
debuxo.rotate(90)  # Rotar el dibujo 90 grados
debuxo.scale(1.5, 0.5)  # Escalar el dibujo
debuxo.translate(0, -500)  # Trasladar el dibujo
guion.append(debuxo)  # Añadir el dibujo a la lista

# Crear otro dibujo, añadir la imagen y aplicar transformaciones
debuxo = Drawing(50, 30)
debuxo.add(imaxe)
debuxo.rotate(45)  # Rotar el dibujo 45 grados
debuxo.translate(-40, 100)  # Trasladar el dibujo
guion.append(debuxo)  # Añadir el dibujo a la lista

# Crear un dibujo con el tamaño de una página A4
debuxo = Drawing(A4[0], A4[1])
for elemento in guion:
    debuxo.add(elemento)  # Añadir cada dibujo de la lista al dibujo principal

# Renderizar el dibujo a un archivo PDF
renderPDF.drawToFile(debuxo, "probaConDrawingImage.pdf")