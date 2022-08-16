import pandas as pd
 
df = pd.read_csv("/home/haseeb/Desktop/NLU/CB/files/chatbot_menu - Sheet1.csv")
order = pd.read_csv("/home/haseeb/Desktop/NLU/CB/files/user_menu - Sheet1.csv")

item = "cheese pizza"
list = []
for index in df.index:
    if item == df["item"][index]:
        list.append(df["item"][index])
        list.append(df["price"][index])
        length = len(order)
        order.loc[length] = list
    
print(order)

order = order[0:0]