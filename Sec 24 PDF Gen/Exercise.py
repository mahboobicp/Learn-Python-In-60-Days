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

pdf.output("animal.pdf")