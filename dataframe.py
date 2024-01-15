import pandas as pd
import random
import matplotlib.pyplot as plt

file = 'dataframe.csv'

df = pd.read_csv(file)

list_ages = []
for i in range(len(df)):
    list_ages.append(random.randint(0, 99))
    
df['age'] = list_ages


df_pass = df[df['mark'] > 70]

df_age_pass = df[(df['age'] > 25)&(df['mark'] > 70)]


list_mark = []

list_class = []

list_id = []

list_gender = []

for i in range(len(df)):
    list_class.append(random.randint(1, 8))
    
for i in range(len(df)):
    list_mark.append(random.randint(1, 100))
    
for i in range(len(df)):
    list_gender.append(random.choice(['male', 'female', 'monkey']))
    
for i in range(len(df)):
    list_id.append(random.randint(1, 10000))
    
df['id'] = list_id
    
df['gender'] = list_gender

df['class'] = list_class

df['mark'] = list_mark

df['mark'].hist()


plt.plot(df['age'], df['mark'], 'h')
for x, y, text in zip(df['age'], df['mark'], df['name']):
    plt.text(x, y, text)