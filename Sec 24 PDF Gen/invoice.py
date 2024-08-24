import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

# Load ddata from excel and generate PDF invoice
filepaths = glob.glob("invoices/*xlsx")
#print(filepaths)

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    pdf = FPDF(orientation="P", unit='mm', format='a4')
    pdf.add_page()
    filename = Path(filepath).stem
    invoice_nr = filename.split("-")[0]
    pdf.set_font(family="Times", style="B",size=16)
    pdf.cell(w=50,h=8,txt=f"Invoice nr.{invoice_nr}")
    FILEPATH = f"D:\Learn Python in 60 Days\Sec 24 PDF Gen\PDF\{filename}.pdf"
    pdf.output(FILEPATH)


    