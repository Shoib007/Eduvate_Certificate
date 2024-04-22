from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape

FONT = "Helvetica"

cs_title_experties = {
    "GRADE 1": ["Emerging Coder", "Block Based Coding"],
    "GRADE 2": ["Junior Coder", "Block Based Coding"],
    "GRADE 3": ["Pro Coder", "Block Based Coding"],
    "GRADE 4": ["Emerging App Develoer", "App Lab"],
    "GRADE 5": ["Pro App Develoer", "MIT App Inventor"],
    "GRADE 6": ["Junior Web Develoer", "Web Development"],
    "GRADE 7": ["Pro Web Develoer", "Web Development"],
    "GRADE 8": ["Junior Pythonista", "Python 3"],
    "GRADE 9": ["Emerging AI Developer", "Artificial Intelligence"],
}

robotics_title_experties = {
    "GRADE 1": ["Emerging Technologist", "DIY & Electronics"],
    "GRADE 2": ["Emerging Technologist", "DIY & Electronics"],
    "GRADE 3": ["Emerging Technologist", "DIY & Electronics"],
    "GRADE 4": ["Emerging Electroniker", "Electronics"],
    "GRADE 5": ["Junior Electroniker", "Electronics & Arduino"],
    "GRADE 6": ["Junior Arduino Coder", "Arduino"],
    "GRADE 7": ["Expert Arduino Coder", "Arduino"],
    "GRADE 8": ["Emerging IoT Developer", "IoT & ESP32"],
    "GRADE 9": ["Junior IoT Developer", "IoT & ESP32"],
    "GRADE 10": ["Expert IoT Developer", "IoT & ESP32"],
}


# Get current date in DD/MM/YYYY format
today = datetime.today().strftime("%d/%m/%Y")

def generate_cs_robotics_certificate(schoolName:str, grade:str, student_name:str, output_folder:str, template_path:str, cert_type:str) -> None:
    c = canvas.Canvas(f"{output_folder}/{grade}_{student_name}.pdf", pagesize=landscape(A4))
    c.drawImage(template_path, 0, 0, landscape(A4)[0], landscape(A4)[1])

    # Customize certificate with data
    c.setFont(FONT, 24)
    c.setFillColorRGB(0, 0, 0)
    
    # Student Name
    c.drawCentredString(420, 355, student_name)  # Adjust coordinates
    c.setFont(FONT, 20)

    # Grade
    c.drawCentredString(280, 320,  grade.split()[1])  # Adjust coordinates

    # School Name
    c.drawCentredString(490, 280, schoolName.upper()) 

    # Titles and Experties
    if cert_type == "CS":
        c.drawCentredString(550, 235, cs_title_experties[grade][0].upper())
        c.drawCentredString(420, 160, cs_title_experties[grade][1].upper())
    else:
        c.drawCentredString(550, 235, robotics_title_experties[grade][0].upper())
        c.drawCentredString(420, 160, robotics_title_experties[grade][1].upper())
    c.setFont(FONT, 12)
    c.drawCentredString(180, 110, today)

    c.save()
