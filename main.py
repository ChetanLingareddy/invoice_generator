import pandas as pd
import glob

filepaths = glob.glob("invoices/*xlsx")
for filepath in filepaths:
    df = pd.read_excel(filepath)
    print(df)