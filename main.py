import pandas as pd
import glob
from fpdf  import FPDF
from  pathlib import Path

filepaths = glob.glob("invoices/*xlsx")
for filepath in filepaths:
    df = pd.read_excel(filepath)
    pdf = FPDF ( orientation="p", unit="mm", format="A4" )
    pdf.set_auto_page_break ( auto=False, margin=0 )
    pdf.add_page()
    filename = Path(filepath).stem
    invoice_no = filename.split("-")[0]
    date = filename.split("-")[1]
    pdf.set_font(family="Times",style= "B",size=10)
    pdf.cell(w=50,h=8,txt=f"Invoice Number: {invoice_no}",align="L")
    pdf.cell (w=0, h=20, txt=f"Date: {date}", align="L" )
    print(df)
    pdf.output(f"pdfs/{filename}.pdf")