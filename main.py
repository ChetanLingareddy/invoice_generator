
import pandas as pd
import glob
from fpdf  import FPDF
from  pathlib import Path

# using glob we are getting files ending with *xlsx and assigning to filepaths.
filepaths = glob.glob("invoices/*xlsx")

# for loop to iterate over filepaths and create a pdf.
for filepath in filepaths:
    pdf = FPDF ( orientation="p", unit="mm", format="A4" )

    pdf.add_page()

    # Takes the entire excel file name and with stem we split the extensions leaving only the filename.
    filename = Path(filepath).stem


    invoice_no,date  = filename.split("-")

    # Print invoice number and date on each respective pdf.
    pdf.set_font(family="Times",style= "B",size=10)
    pdf.cell(w=50,h=8,txt=f"Invoice Number: {invoice_no}",align="L",ln = 1)
    pdf.cell (w=0, h=0, txt=f"Date: {date}", align="L")
    pdf.ln(5)#break line

    # Extracting data from the files using pandas
    df = pd.read_excel ( filepath )

#  Extracting headers from the Excel files to their respective pdfs.
    columns = df.columns
    # Replacing headers with spaces and capitalizing first letter of each word using title().
    columns = [item.replace("-"," ").title() for item in columns]
    pdf.set_font(family="Times",style= "B",size=8)
    pdf.cell(w = 30, h = 8, txt = columns[0], border= 1)
    pdf.cell ( w=70, h=8, txt= columns[1], border=1 )
    pdf.cell ( w=30, h=8, txt=columns[2], border=1 )
    pdf.cell ( w=30, h=8, txt=columns[3], border=1)
    pdf.cell ( w=30, h=8, txt=columns[4], border=1  ,ln =1)

# Extracting  data from the Excel and printing it in their respective pdfs.
    for index, row in df.iterrows():
        pdf.set_font(family="Times",size=8)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border = 1)
        pdf.cell( w=70, h=8, txt=str ( row["product_name"] ), border=1 )
        pdf.cell ( w=30, h=8, txt=str ( row["amount_purchased"] ), border=1 )
        pdf.cell(w=30,h=8, txt=str(row["price_per_unit"]),border=1)
        pdf.cell ( w=30, h=8, txt=str ( row["total_price"] ), border=1 ,ln =1)

# Calculating and printing the total amount of all the orders from total price.
    total = df["total_price"].sum()
    pdf.cell ( w=30, h=8, txt="", border=1 )
    pdf.cell ( w=70, h=8, txt="", border=1 )
    pdf.cell ( w=30, h=8, txt="", border=1 )
    pdf.cell ( w=30, h=8, txt="", border=1 )
    pdf.cell(w= 0, h=8, txt=str(total),border=1)

# Printing last line.
    pdf.ln(20)
    pdf.set_font(family="times", style="B", size=8)
    pdf.cell(w=0, h=8, txt=f"The Total Amount Due Is {total} Dollars.", ln =1)

    # Creating pdfs with their respective file names.
    pdf.output(f"pdfs/{filename}.pdf")