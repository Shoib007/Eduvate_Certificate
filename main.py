import openpyxl, os, argparse
from robofest import generate_robofest_certificate
from CSR_certificate import generate_cs_robotics_certificate
from datetime import datetime

# Read the cert_type from the keyword argument if not exist return error
parser = argparse.ArgumentParser()
parser.add_argument("--cert_type", type=str, help="The type of certificate to generate", required=True, choices=["CS", "ROBOTICS", "ROBOFEST", "TEACHERS"])
args = parser.parse_args()


# get working directory
cwd = os.getcwd()

# Read all the files in the cwd/data folder
data_folder = os.path.join(cwd, "data")
output_folder = os.path.join(cwd, "certificates")


# Check if the output_folder exists or not
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


data_files = os.listdir(data_folder)



# Get template path
CSR_template = os.path.join(cwd, "template","CSR_template.png")
Robofest_template = os.path.join(cwd,"template", "Robofest_template.png")


# Main Logic for generating certificates
for school_file in data_files:
    schoolName = school_file.split(".")[0].upper()
    print(f"Creating certificate for {schoolName} -> {args.cert_type} ...")

    # Load the school sheet
    ws = openpyxl.load_workbook(os.path.join(data_folder, school_file))

    # Get the list of sheet names within that school sheet
    sheetNames = ws.sheetnames

    for grade in sheetNames:
        sheet = ws[grade]

        for row in sheet.iter_rows(min_row=2, values_only=True):  # Skip header
            if args.cert_type == "CS" or args.cert_type == "ROBOTICS":
                # Creating folder for each school, Subject and grade
                folder = os.path.join(cwd, output_folder, schoolName , args.cert_type, grade)
                if not os.path.exists(folder):
                    os.makedirs(folder)

                if row[0] is None:
                    break
                student_name = row[0].upper()
                grade = grade.upper()
                generate_cs_robotics_certificate(schoolName, grade, student_name, folder, template_path=CSR_template, cert_type=args.cert_type)
            elif args.cert_type == "ROBOFEST":
                if row[0] is None:
                    break
                date = str(row[0])
                student_name = row[1].upper()
                grade = str(row[2])
                projectName = row[4].upper()

                # Creating folder for each school, Subject and grade
                folder = os.path.join(cwd, output_folder, schoolName , args.cert_type)
                if not os.path.exists(folder):
                    os.makedirs(folder)

                generate_robofest_certificate(date, student_name, grade, schoolName, projectName, output_folder=folder, template_path=Robofest_template)
    
    print(f"Certificate for {schoolName} -> {args.cert_type} created successfully!")

