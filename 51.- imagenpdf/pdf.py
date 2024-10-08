from fpdf import FPDF

# Crear un objeto PDF
pdf = FPDF()

# Agregar una página
pdf.add_page()

# Establecer la fuente y el tamaño de la fuente
pdf.set_font("Arial", size=12)

# Agregar el texto
pdf.multi_cell(0, 5, txt="Solución : Pesaje Batch")
pdf.multi_cell(0, 5, txt="Cliente : Aramark")
pdf.multi_cell(0, 5, txt="Atención: Skarlet")

pdf.ln(10)

pdf.multi_cell(0, 5, txt="Escenario técnico:")
pdf.multi_cell(0, 5, txt="En términos generales la presente propuesta consta del diseño construcción y programación, de un sistema de pesaje, que de manera integrada, permita realizar el proceso de pesaje manual, con funciones de agrupación peso exacto e impresión integrada.")
pdf.multi_cell(0, 5, txt="El desarrollo propuesto, integra tecnologías de impresión dedicada, pesaje, consolidación de magnitudes y el registro de los pesos específicos, considerando tara preseleccionada, como parte de la lógica y el proceso productivo regular.")
pdf.multi_cell(0, 5, txt="Es importante mencionar que tanto la lógica, como la técnica, es de completo desarrollo particular, y en esto no existen licenciamiento, dependencias y/o proveedores externos por tanto la autoría y diseño y confección es completamente especifico según los requerimientos particulares y especificados por el cliente.")

pdf.ln(10)

pdf.multi_cell(0, 5, txt="Valorización:")
pdf.multi_cell(0, 5, txt="En cuanto a esto y hablando de números concretamente presento la siguiente tabla.")

pdf.ln(10)

pdf.multi_cell(0, 5, txt="Estación de pesaje móvil.")
pdf.multi_cell(0, 5, txt="Índice Descripción Valor")
pdf.multi_cell(0, 5, txt="2 Cpu. US 1.050")
pdf.multi_cell(0, 5, txt="3 Pantalla touch. US 305")
pdf.multi_cell(0, 5, txt="4 Pesa auto soportado. US 980")
pdf.multi_cell(0, 5, txt="5 Software pesaje etiquetaje consolidación. US 1.100")
pdf.multi_cell(0, 5, txt="6 Carrito y batería recargable. US 670")
pdf.multi_cell(0, 5, txt="Total US 4.005")

pdf.ln(10)

pdf.multi_cell(0, 5, txt="Estación de impresión fija.")
pdf.multi_cell(0, 5, txt="Índice Descripción Valor")
pdf.multi_cell(0, 5, txt="1 Impresora Térmica. US 1.190")
pdf.multi_cell(0, 5, txt="2 Cpu, pantalla, ups US 1.050")
pdf.multi_cell(0, 5, txt="3 Software pesaje etiquetaje consolidación. US 850")
pdf.multi_cell(0, 5, txt="Total US 3.090")

pdf.ln(10)

pdf.multi_cell(0, 5, txt="Sin perjuicio delo anterior es que frente a cualquier desarrollo es preciso de aportar el 30% del proyecto, al iniciar los trabajos, y una vez aceptado la propuesta y definido los tiempos de entrega , no sin antes precisar el equipo de trabajo que de parte del cliente, aportaran y proveerán de las condiciones y medios para el correcto desarrollo , refiriéndonos específicamente , a accesos, tiempo , situaciones de pruebas, calibraciones y por lo demás, la cooperación y aporte que podría ser de relevancia , y que contribuya constructivamente al exitosa conclusión del presente proyecto.")

pdf.ln(10)

pdf.multi_cell(0, 5, txt="Sin más que detallar.")

pdf.ln(10)

pdf.multi_cell(0, 5, txt="José Manuel Adasme")
pdf.multi_cell(0, 5, txt="Desarrollos de productos y servicios")

# Agregar la imagen en la esquina inferior derecha
pdf.image("x.png", x=170, y=250, w=30, h=30)

# Guardar el PDF
pdf.output("propuesta.pdf")