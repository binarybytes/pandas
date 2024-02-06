# import required modules
import zipfile
import pandas as pd
 
# open zipped dataset
with zipfile.ZipFile("sheet.zip") as z:
   # open the csv file in the dataset
   with z.open("sheet.csv") as f:
       # read the dataset
        df = pd.read_csv(f)

#print(df[df.payload.str.contains('evil')])
print(df[df.payload.str.contains('re|evil', case=False, regex=True)])

#python -W ignore test.py
