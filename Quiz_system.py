import numpy as np
import random
import os
import pandas as pd
import random

from oauthlib.oauth2.rfc6749.tokens import random_token_generator

# df = pd.read_excel("VendorProducts.xlsx")
# print(df)
# dfitems= pd.read_excel("VendorProducts.xlsx")
# # print(dfitems['Name',"Pr"])
# print(dfitems.heaad())
#
# dictat={
#          'name': ["Ali ","haadi","ayyan"],
#         'age': [2,3,1]
# }
# df=pd.DataFrame(dictat)
# print(df.to_csv("ClassFirstTable.csv"))
# dfitems= pd.read_excel("VendorProducts.xlsx")
# print(dfitems[Name])




read questions file
df = pd.read_csv("QuestionareDummy.csv")

try:
    scores = pd.read_csv("student_score.csv")
except:
    scores = pd.DataFrame(columns=["Name","Score"])

name = input("Enter your name: ")
if name in scores["Name"].values:
    print("You already attempted the quiz")
    exit()

questions = df.sample(5)
score = 0

for i in range(len(questions)):
    print("\nQuestion:", questions.iloc[i]["Question"])
    print("A.", questions.iloc[i]["Option A"])
    print("B.", questions.iloc[i]["Option B"])
    print("C.", questions.iloc[i]["Option C"])
    print("D.", questions.iloc[i]["Option D"])

    ans = input("Enter answer (A/B/C/D): ").upper()

    if ans == questions.iloc[i]["Right Answer"]:
        print("Correct")
        score += 1
    else:
        print("Wrong answer. Game Over.")
        break

print("Final Score:", score)
new = pd.DataFrame([[name,score]], columns=["Name","Score"])
scores = pd.concat([scores,new])
scores.to_csv("student_score.csv",index=False)


