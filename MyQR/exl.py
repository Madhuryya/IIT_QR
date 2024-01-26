import pandas as pd
import qrcode
 

# Read the Excel file into a Pandas DataFrame
df = pd.read_excel('D:\MyQR\D_Database.xlsx')

# Print the first 5 rows of the DataFrame

df=df.fillna(0)
df=df.drop(0)
print(df)

for index in df.index:
    df["Location"][index]=str(df["Location"][index]).replace("\n", "")
    df["Description_of_Item"][index]=str(df["Description_of_Item"][index]).replace("\n", "")
   
    qrurl = f'https://qrproject-iit.netlify.app?Sl_No={df["Sl_No"][index]}&Description_of_Item={str(df["Description_of_Item"][index]).replace(" ","%20")}&P.O._No.with_Date={str(df["PO"][index]).replace(" ","%20")}&Qty={str(df["Qty"][index]).replace(" ","%20")}&Price={str(df["Price"][index]).replace(" ","%20")}&Location={str(df["Location"][index]).replace(" ","%20")}&Registration={str(df["Registration"][index]).replace(" ","%20")}'
    print(qrurl)
    img = qrcode.make(qrurl)
    img.save(f'{df["Sl_No"][index]}.png')
