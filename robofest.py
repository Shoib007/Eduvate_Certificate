from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from datetime import datetime
from uuid import uuid4

today = datetime.today().strftime("%d/%m/%Y")

def generate_robofest_certificate(date:str, student_name:str, grade:str, schoolName:str, projectName:str, output_folder:str, template_path:str) -> None:
    c = canvas.Canvas(f"{output_folder}/{grade}_{student_name}.pdf", pagesize=landscape(A4))
    c.drawImage(template_path, 0, 0, landscape(A4)[0], landscape(A4)[1])

    c.setFont("Helvetica", 24)
    c.setFillColorRGB(0, 0, 0)

    # Studetn's Name
    c.drawCentredString(420, 360, student_name)  
    
    # Studetn's Grade
    c.setFont("Helvetica", 20)
    c.drawCentredString(280, 320,  grade)  
    
    # School Name
    c.drawCentredString(480, 275,  schoolName) 

    # Studetn's project name
    c.drawCentredString(475, 195,  projectName)

    # Robofest Conducted date
    c.drawCentredString(350, 150,  date)
    
    # Todays Date
    c.setFont("Helvetica", 12)
    c.drawCentredString(220, 90, today)


    # Customize certificate with data
    c.setFont("Helvetica", 10)
    c.drawCentredString(700, 10, str(uuid4()))

    c.save()

