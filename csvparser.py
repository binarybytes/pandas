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
#print(df[df.payload.str.contains('re|evil', case=False, regex=True)])

#define a search function
def search_string(s, search):
    return search in str(s).lower()

# Search for the string 'al' in all columns
mask = df.apply(lambda x: x.map(lambda s: search_string(s, '.php')))

# Filter the DataFrame based on the mask
filtered_df = df.loc[mask.any(axis=1)]
print(filtered_df)


#python -W ignore test.py
