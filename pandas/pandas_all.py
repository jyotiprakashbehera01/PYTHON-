import pandas as pd

 #pratice conecting  dataframe :


# data = {
#     "Name" : ["jyoti","jaya","gudu","somya","amit"],
#     "age" :[21,20,23,26,25],
#     "city" :["cuttack","arhuhad","sambalpur","kendrapara","bokachoda"]
# }
# df = pd.DataFrame(data)

# print(df)
# print(df.shape)
# print(df.columns)

#conecting Execl sheet :



# df = pd.series([1,2,3,4])
# print(df)



df = pd.read_excel(r"C:\Users\Jyoti Prakash Behera\Downloads\SAP_Dump.xlsx")
print(df)
print(df.head(5))
print(df.tail(5))
print(df.columns)
# print(df.dtypes)
# print(df.info())
# print(df.describe())
# print(df.size)
# print(df.shape)
# print(df.sample())

# print(df.loc[0])  # label-based lookup on the index
# print(df.iloc[0]) # position-based lookup

# print(type(df["Account"]))

# print(df["Account"].head(5))

# filtered_df = df[df["Document type"] == "AB"]

# print(filtered_df)

