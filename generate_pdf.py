from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import datetime

def generate_pdf(order_data, filename="order_receipt.pdf"):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "Nashville Halal Food")

    c.setFont("Helvetica", 12)
    c.drawString(50, height - 80, f"Sana: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    y = height - 120
    for item in order_data["items"]:
        c.drawString(50, y, f"{item['name']} x{item['qty']} - ${item['price'] * item['qty']}")
        y -= 20

    c.drawString(50, y - 20, f"Jami: ${order_data['total']}")
    c.drawString(50, y - 40, f"Mijoz: {order_data['customer_name']}")
    c.drawString(50, y - 60, f"Telefon: {order_data['phone']}")

    c.save()
