
import numpy as np

import pandas as pd
import matplotlib.pyplot as plt

import re  
  
from collections import Counter  


df = pd.read_json('data.json')


def extract_numbers(input_string):   
    pattern = re.search(r'\d+\.\d+', input_string)
    numbers = -100
    if pattern:
        numbers = pattern.group()
    return float(numbers)

artists = df['画师']  

# 创建Counter字典  
artist_counts = Counter(artists)  

num_ones = 0

for i in artist_counts.values():
    if( i == 1 ):
        num_ones+=1

artist_counts['其他'] = num_ones

artist_counts = {key: value for key, value in artist_counts.items() if value != 1} 

artist_op = {}


for i in artist_counts.keys():
    artist_op[i] = []   

for i in df['画师']:
    f = 0
    for j in artist_op.keys():
        if(i == j):
            artist_op[j].append()
            f = 1 

print(artist_op)
    



'''# 打印结果  
for artist, count in artist_counts.items():  
    print(f"{artist}: {count}")'''


# print(df.head(1))
# print(df.生命上限.describe())

shuju = ['代号','身高','职业','生命上限','攻击','防御','法术抗性','再部署','部署费用','阻挡数','攻击速度']


a_values = df['生命上限'].str.split('/').str[0]  
b_values = df['生命上限'].str.split('/').str[1]  

  

df['初始生命值'] = list(map(int, a_values)) 
df['满级生命值'] = list(map(int, b_values)) 

a_values = df['攻击'].str.split('/').str[0]  
b_values = df['攻击'].str.split('/').str[1]  
  
df['初始攻击'] = a_values  
df['满级攻击'] = b_values

a_values = df['防御'].str.split('/').str[0]  
b_values = df['防御'].str.split('/').str[1]  
  
df['初始防御'] = a_values  
df['满级防御'] = b_values

a_values = df['法术抗性'].str.split('/').str[0]  
b_values = df['法术抗性'].str.split('/').str[1]  
  
df['初始法术抗性'] = a_values  
df['满级法术抗性'] = b_values

a_values = []
for i in df['再部署']:
    x = extract_numbers(i)
    a_values.append(x)

df['再部署时间'] = a_values  

a_values = df['部署费用'].str.split('/').str[0]  
b_values = df['部署费用'].str.split('/').str[1]  
  
df['满潜部署费用'] = a_values  
df['零潜部署费用'] = b_values

a_values = []
for i in df['攻击速度']:
    x = extract_numbers(i)
    a_values.append(x)

df['攻速'] = a_values  

print(df['攻速'])

# 创建一个新的图形  
plt.figure(figsize=(18, 100))

x , y  = df['代号'], df['满级生命值']


indices = np.argsort(y)  
x_sorted = x[indices]  
y_sorted = y[indices]  
  
