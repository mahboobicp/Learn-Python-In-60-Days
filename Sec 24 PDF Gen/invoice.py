import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

# Load ddata from excel and generate PDF invoice
filepaths = glob.glob("invoices/*xlsx")
#print(filepaths)

for filepath in filepaths:
    pdf = FPDF(orientation="P", unit='mm', format='a4')
    pdf.add_page()
    filename = Path(filepath).stem
    # Exteract invoice number and date from 
    # File name and store at in a variable to add
    # them to the invoice
    invoice_nr = filename.split("-")[0]
    date = filename.split("-")[1]
    # Add invoice Number
    pdf.set_font(family="Times", style="B",size=16)
    pdf.cell(w=50,h=8,txt=f"Invoice nr.{invoice_nr}",ln=1)
    # Add Date
    pdf.set_font(family="Times", style="B",size=14)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=50,h=8,txt=f"Date : {date}",ln=1)
    
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    colum = df.columns
    # Exteract Table Heading
    colum =[item.replace("_"," ").title() for item in colum]
    # Fonts Syle for Headings
    pdf.set_font(family="Times",size=10,style="B")
    pdf.set_text_color(80,80,80)
    pdf.cell(w=30,h=8,txt=colum[0],border=1)
    pdf.cell(w=65,h=8,txt=colum[1],border=1)
    pdf.cell(w=35,h=8,txt=colum[2],border=1)
    pdf.cell(w=30,h=8,txt=colum[3],border=1)
    pdf.cell(w=30,h=8,txt=colum[4],border=1,ln=1)
    
    # Add rows to table
    for index, row in df.iterrows():
        pdf.set_font(family="Times",size=10)
        pdf.set_text_color(80,80,80)
        pdf.cell(w=30,h=8,txt=str(row["product_id"]),border=1)
        pdf.cell(w=65,h=8,txt=str(row["product_name"]),border=1)
        pdf.cell(w=35,h=8,txt=str(row["amount_purchased"]),border=1)
        pdf.cell(w=30,h=8,txt=str(row["price_per_unit"]),border=1)
        pdf.cell(w=30,h=8,txt=str(row["total_price"]),border=1,ln=1)

    # Add total price Sum
    totalprice = df["total_price"].sum()
    pdf.set_font(family="Times",size=10)
    pdf.set_text_color(80,80,80)
    pdf.cell(w=30,h=8,txt="",border=1)
    pdf.cell(w=65,h=8,txt="",border=1)
    pdf.cell(w=35,h=8,txt="",border=1)
    pdf.cell(w=30,h=8,txt="",border=1)
    pdf.cell(w=30,h=8,txt=str(totalprice),border=1,ln=1)

    # Add total sum in sentence
    pdf.set_font(family="Times",size=12)
    pdf.set_text_color(100,100,100)
    pdf.ln(3)
    pdf.cell(w=30,h=8,txt=f"The total amount is : {totalprice} only",ln=1)

    # Company name
    pdf.set_font(family="Times",size=14,style="B")
    pdf.set_text_color(100,100,100)
    pdf.cell(w=30,h=8,txt="KPEZDMC")


    # By default it save the output at project 
    # directory we will specify own path
    FILEPATH = f"D:\Learn Python in 60 Days\Sec 24 PDF Gen\PDF\{filename}.pdf"
    pdf.output(FILEPATH)


    