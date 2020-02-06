import numpy as np
import pandas as pd

seito = pd.DataFrame([[1,1,4,8,2,1,2],
                      [2,6,3,9,9,5,5],
                      [3,2,8,1,1,0,3],
                      [4,2,6,2,9,1,9],
                      [5,2,1,3,4,4,4]],
                      columns=['生徒No','成績','好嫌','性格','費用','自由さ','賑々しさ'])
print('seito:',seito)
juku = pd.DataFrame([[1,7,6,4,6,2,9],
                     [2,6,7,8,6,1,4],
                     [3,2,0,3,3,0,8],
                     [4,1,0,3,9,8,5],
                     [5,3,7,0,3,1,5]],
                     columns=['塾ID','成績','好嫌','性格','費用','自由さ','賑々しさ'])
print('juku:',juku)
clms = ['成績','好嫌','性格','費用','自由さ','賑々しさ']
for clm in clms:
    print(clm+'重要度')
for i in range(len(seito['生徒No'])):
    for clm in clms:
        if juku[clm][i] == 0:
            seito[clm][i] = seito[clm][i] / 2
seito


import decimal
"""import pickle"""
import decorator


for i in range(len(seito['生徒No'])):
    if juku['好嫌'][i] == 0:
        seito['好嫌'][i] = decimal.Decimal(seito['好嫌'][i] / 2)
print(seito['好嫌'])

w_params = {
'好嫌': 2,
'成績': 2,
'外向性': 1,
'協調性':1,
'勤勉性':1,
'繊細性':1,
'開放性':1,
'費用': 1,
'自由さ': 1,
'賑々しさ': 1
}

intercepts = {
'好嫌': 0,
'成績': 0,
'外向性': 0,
'協調性':0,
'勤勉性':0,
'繊細性':0,
'開放性':0,
'費用': 3,
'自由さ': 0,
'賑々しさ': 0
}

for key,w in w_params.items():
    seito.loc[:,key] = seito[key] * w
for key,w in intercepts.items():
    seito.loc[:,key] = seito[key] + w
print(seito)
studf = pd.read_csv('C:\\Users\\User\\Dropbox\\塾ログ共有\\個人用\\竹内芳州\\適塾診断関連\\seitodata_dummy.csv', encoding='cp932')
print(studf.head())
for key,w in w_params.items():
    studf.loc[:,key] = studf[key] * w
for key,w in intercepts.items():
    studf.loc[:,key] = studf[key] + w
studf.head()
stu_cod = pd.read_csv('C:\\Users\\User\\Dropbox\\塾ログ共有\\個人用\\竹内芳州\\適塾診断関連\\seito_cod_small.csv', encoding='cp932')
studf['成績']/(stu_cod['距離重要度'] + 1)
import pickle
intercepts = {
    '好嫌i': 0,
    '成績i': 0,
    '外向性i': 0,
    '協調性i': 0,
    '勤勉性i': 0,
    '繊細性i': 0,
    '開放性i': 0,
    '費用i': 0,
    '自由さi': 0,
    '賑々しさi': 0
}
for key in intercepts.keys():
    print(key.strip('i'))
pickle.dump(intercepts, open("intercepts.dump", "wb"))
