import glob
from pathlib import Path
import pandas as pd
from fpdf import FPDF

#create a list of file path
filepaths = glob.glob("Files/*.txt")
print(filepaths)

#Create One PDF file
pdf = FPDF(orientation="P", unit="mm", format="a4")

# Go through each text file
for filepath in filepaths:
    pdf.add_page()
    #Get the file name without extension
    #and convert it to title case
    filename = Path(filepath).stem
    name = filename.title()
    pdf.set_font(family="Times",size=16,style="B")
    pdf.cell(w=50,h=1,txt=name,ln=1)

    # Get the content of each file
    with open(filepath,"r") as file:
        content = file.read()
    # Add the text File content to PDF
    pdf.set_font(family="Times",size=12)
    pdf.multi_cell(w=0,h=6,txt=content)

pdf.output("animal.pdf")