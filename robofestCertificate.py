from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from datetime import datetime
from uuid import uuid4
from wrapper import getWrapedText

today = datetime.today().strftime("%d/%m/%Y")

# Fonts for the certificate
NAME_FONT = "Roboto-Italic"
SCHOOL_FONT = "Roboto-Italic"
TITLE_FONT = "Roboto-Italic"

def generate_robofest_certificate(date:str, student_name:str, grade:str, schoolName:str, projectName:str, output_folder:str, template_path:str) -> None:
    c = canvas.Canvas(f"{output_folder}/{grade}_{student_name}.pdf", pagesize=landscape(A4))
    c.drawImage(template_path, 0, 0, landscape(A4)[0], landscape(A4)[1])

    c.setFont(NAME_FONT, 28)
    c.setFillColorRGB(0, 0, 0)

    # Studetn's Name
    c.drawCentredString(420, 360, student_name)
    
    # Studetn's Grade
    c.setFont(SCHOOL_FONT, 22)
    c.drawCentredString(280, 320,  grade)
    
    # School Name
    c.drawCentredString(480, 275,  schoolName) 

    
    # Studetn's project name
    getWrapedText(canvas=c, text=projectName, width=400, x_position=475, y_position=195, font_size=20, fontFamily=TITLE_FONT)

    # Robofest Conducted date
    c.drawCentredString(350, 150,  date)
    
    # Todays Date
    c.setFont(SCHOOL_FONT, 12)
    c.drawCentredString(220, 90, today)


    # Customize certificate with data
    c.setFont(SCHOOL_FONT, 10)
    c.drawCentredString(700, 10, str(uuid4()))

    c.save()

