# pip install reportlab

from reportlab.pdfgen import canvas

c = canvas.Canvas("output.pdf")
c.drawString(100.750, "Hello from Gaurav Bhatt")
c.save()
