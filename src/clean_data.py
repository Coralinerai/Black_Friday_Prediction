import pandas as pd 
data=pd.read_csv("Data/raw/blackfriday.csv")
#print(data.head())
#print(data.info())
#print(data.describe())


cats = ["Product_Category_1", "Product_Category_2", "Product_Category_3"]
#print(len(data["Product_ID"].unique()))
pid = "P00000542"
combos = data[["Product_ID"] + cats].drop_duplicates().sort_values("Product_ID")
combos_one = data.loc[data["Product_ID"] == pid, cats].drop_duplicates()
print(combos_one)

#checking the unique values in categories 
#print(data['Product_Category_1'].unique(),data['Product_Category_2'].unique(),data['Product_Category_3'].unique())

#removing duplicate rows 
data=data.drop_duplicates()

#filling null values in categories with O 
cats = ["Product_Category_2", "Product_Category_3"]
data[cats] = data[cats].fillna(0).astype(int)
print(data[cats].isna().sum())


#checking the unique values un Age column 
print(data['Age'].unique())
#['0-17' '55+' '26-35' '46-50' '51-55' '36-45' '18-25']  7 values 

print(data['Stay_In_Current_City_Years'].unique())
#['2' '4+' '3' '1' '0']

data["Stay_In_Current_City_Years"] = (data["Stay_In_Current_City_Years"].replace("4+", "4").astype(int))

#Checking City category unique values
print(data['City_Category'].unique())
#City Category has 3 unique values ['A' 'C' 'B']

#Occupation
print(data['Occupation'].unique())

data.to_csv("data/cleaned/blackfriday_cleaned.csv", index=False)









