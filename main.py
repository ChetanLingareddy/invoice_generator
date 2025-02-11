
import pandas as pd
import glob
from fpdf  import FPDF
from  pathlib import Path

filepaths = glob.glob("invoices/*xlsx")

for filepath in filepaths:
    pdf = FPDF ( orientation="p", unit="mm", format="A4" )

    pdf.add_page()

    filename = Path(filepath).stem

    invoice_no,date  = filename.split("-")

    pdf.set_font(family="Times",style= "B",size=10)
    pdf.cell(w=50,h=8,txt=f"Invoice Number: {invoice_no}",align="L",ln = 1)
    pdf.cell (w=0, h=0, txt=f"Date: {date}", align="L")
    pdf.ln(5)

    df = pd.read_excel ( filepath )
    columns = df.columns
    columns = [item.replace("-"," ").title() for item in columns]
    pdf.set_font(family="Times",style= "B",size=8)
    pdf.cell(w = 30, h = 8, txt = columns[0], border= 1)
    pdf.cell ( w=70, h=8, txt= columns[1], border=1 )
    pdf.cell ( w=30, h=8, txt=columns[2], border=1 )
    pdf.cell ( w=30, h=8, txt=columns[3], border=1)
    pdf.cell ( w=30, h=8, txt=columns[4], border=1  ,ln =1)

    total = 0.0

    for index, row in df.iterrows():
        pdf.set_font(family="Times",size=8)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border = 1)
        pdf.cell( w=70, h=8, txt=str ( row["product_name"] ), border=1 )
        pdf.cell ( w=30, h=8, txt=str ( row["amount_purchased"] ), border=1 )
        pdf.cell(w=30,h=8, txt=str(row["price_per_unit"]),border=1)
        pdf.cell ( w=30, h=8, txt=str ( row["total_price"] ), border=1 ,ln =1)
        total = total + float(row["total_price"])
    pdf.cell(w= 0, h=8, txt=f"Total Amount : {str(total)}",align="R",border=1,ln =1)


    pdf.output(f"pdfs/{filename}.pdf")