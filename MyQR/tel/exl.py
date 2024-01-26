import pandas as pd
import qrcode
import urllib.parse
 

# Read the Excel file into a Pandas DataFrame
df = pd.read_excel('D:\MyQR\D_Database.xlsx')

# Print the first 5 rows of the DataFrame

df=df.fillna(0)
# df=df.drop(0)
# print(df)



for index in df.index:
    df["Location"][index]=str(df["Location"][index]).replace("\n", "")
    # desc=df["Description_of_Item"][index]
    # desc_encoded = urllib.parse.quote(desc, safe='')
    # po=df["PO"][index]
    # po_encoded=urllib.parse.quote(po, safe='')
    Status=df.iloc[index,7]
    Remarks=df.iloc[index,8]

    qrurl = f'https://qrproject-iit.netlify.app?Sl_No={df["Sl_No"][index]}&Description_of_Item={urllib.parse.quote(str(df["Description_of_Item"][index]).replace(" ","%20"))}&P.O._No.with_Date={urllib.parse.quote(df["PO"][index])}&Qty={str(df["Qty"][index]).replace(" ","%20")}&Price={str(df["Price"][index]).replace(" ","%20")}&Location={urllib.parse.quote(df["Location"][index])}&Registration={urllib.parse.quote(df["Registration"][index])}&Status={urllib.parse.quote(Status)}&Remarks={urllib.parse.quote(Remarks)}'
    qrurl_encoded=urllib.parse.quote(qrurl,safe='')
    # print(df.iloc[index,7])
    print(qrurl)
    img = qrcode.make(qrurl)
    img.save(f'{df["Sl_No"][index]}.png')