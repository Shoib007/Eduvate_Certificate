from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape

from uuid import uuid4
from wrapper import getWrapedText

# Fonts for the certificate
NAME_FONT = "Roboto-Italic"
SCHOOL_FONT = "Roboto-Italic"
TITLE_FONT = "Roboto-Italic"

def generate_teachers_certificate(teacher_name, grades, school_name, total_hr_of_training, output_folder, template_path, subject="Robotics") -> None:
    c = canvas.Canvas(f"{output_folder}/{teacher_name}_{subject}.pdf", pagesize=landscape(A4))
    c.drawImage(template_path, 0, 0, landscape(A4)[0], landscape(A4)[1])

    c.setFont(NAME_FONT, 32)
    c.setFillColorRGB(0, 0, 0)

    # Teacher's Name
    c.drawCentredString(422, 320, teacher_name)

    c.setFont(SCHOOL_FONT, 15)
    
    # Total hours of Training
    # c.drawCentredString(380, 277,  total_hr_of_training)

    # Subject
    c.drawCentredString(502, 277,  subject)

    # Training's grades
    c.drawCentredString(650, 277,  grades)

    
    # School Name
    c.drawCentredString(550, 257,  school_name)



    # Customize certificate with data
    c.setFont(SCHOOL_FONT, 10)
    c.drawCentredString(740, 40, str(uuid4()))

    c.save()

