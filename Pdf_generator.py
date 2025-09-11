
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime

def generate_pdf(order, filename="receipt.pdf"):
    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("Brooklyn Pizza & Cafe", styles['Title']))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph(f"Sana: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", styles['Normal']))
    elements.append(Spacer(1, 12))

    total = 0
    for item, price in order.items():
        elements.append(Paragraph(f"{item}: ${price}", styles['Normal']))
        total += price

    elements.append(Spacer(1, 12))
    elements.append(Paragraph(f"Umumiy: ${total}", styles['Heading2']))
    doc.build(elements)
    return filename
