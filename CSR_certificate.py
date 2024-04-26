from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from utils import CS_ROBOTICS_COMBINED_TITLES, ROBOTICS_TITLE_EXPERTIES, CS_TITLE_EXPERTIES


NAME_FONT = "Roboto-Italic"
SCHOOL_FONT = "Roboto-Italic"
TITLE_FONT = "Roboto-Italic"


# Get current date in DD/MM/YYYY format
today = datetime.today().strftime("%d/%m/%Y")

def generate_cs_robotics_certificate(schoolName:str, grade:str, student_name:str, output_folder:str, template_path:str, cert_type:str) -> None:
    c = canvas.Canvas(f"{output_folder}/{grade}_{student_name}.pdf", pagesize=landscape(A4))
    c.drawImage(template_path, 0, 0, landscape(A4)[0], landscape(A4)[1])

    # Customize certificate with data
    c.setFont(NAME_FONT, 28)
    c.setFillColorRGB(0, 0, 0)
    
    # Student Name
    c.drawCentredString(420, 355, student_name)  # Adjust coordinates
    # c.setFont(FONT, 20)
    c.setFont(SCHOOL_FONT, 22)

    # Grade
    c.drawCentredString(280, 320,  grade.split()[1])  # Adjust coordinates

    # School Name
    c.drawCentredString(490, 280, schoolName) 

    # Font for the Title and Experties
    c.setFont(TITLE_FONT, 20)

    # Titles and Experties
    if cert_type == "CS":
        c.drawCentredString(550, 235, CS_TITLE_EXPERTIES[grade][0])
        c.drawCentredString(420, 160, CS_TITLE_EXPERTIES[grade][1])
    elif cert_type == "ROBOTICS":
        c.drawCentredString(550, 235, ROBOTICS_TITLE_EXPERTIES[grade][0])
        c.drawCentredString(420, 160, ROBOTICS_TITLE_EXPERTIES[grade][1])
    elif cert_type == "CSR_COMBO":
        c.drawCentredString(550, 235, CS_ROBOTICS_COMBINED_TITLES[grade][0])
        c.drawCentredString(420, 160, CS_ROBOTICS_COMBINED_TITLES[grade][1])

    c.setFont(SCHOOL_FONT, 12)
    c.drawCentredString(180, 110, today)

    c.save()
