import pandas as pd

df = pd.read_csv('C:/temp/analyze/data.csv')

# drop useless
df.drop('Unnamed: 0', axis = 1, inplace = True)

# drop age
useless_age_idx = df[
    (df['age'] != '19세이하') &
    (df['age'] != '20~29') &
    (df['age'] != '30~39') &
    (df['age'] != '40~49') &
    (df['age'] != '50~59') &
    (df['age'] != '60~69') &
    (df['age'] != '70세이상')
]
df.drop(useless_age_idx.index, inplace = True)

# drop id
df.drop(['id'], axis = 1, inplace = True)

#drop is_emp
useless_isEmp_idx = df[
    (df['is_emp'] != '그룹사직원') &
    (df['is_emp'] != '해당사항없음')
]
df.drop(useless_isEmp_idx.index, inplace = True)

# drop is_moved
useless_isMoved_idx = df[
    (df['is_moved'] != 'Y') &
    (df['is_moved'] != 'N')
]
df.drop(useless_isMoved_idx.index, inplace = True)

int_sales = df['sales'].str.replace(',', '')

df['int_sales'] = int_sales

df['int_sales'] = df['int_sales'].astype(int)

df.drop('sales', axis = 1, inplace = True)

df2 = pd.read_excel('Z:/analyze/ams_data/서부대인광.xlsx')
df3 = pd.read_excel('Z:/analyze/ams_data/대울세경강.xlsx')
df4 = pd.read_excel('Z:/analyze/ams_data/나머지.xlsx')

df2 = df2.append([df3, df4], ignore_index = True)
print(df2)

df2 = df2.rename({'단지명' : 'apt'}, axis = 1)

df2.drop(['광역시도', '시군구', '행정동', '입주일', '세대수', '대상고객수', '구매고객수', '구매건수', '구매금액', '객단가', '건단가', '인당구매건수'], axis = 1, inplace = True)
df2.drop_duplicates(subset = 'apt', keep = False, inplace = True)



df = pd.merge(df, df2, how = 'left', on = 'apt')

df.drop('apt', inplace = True, axis = 1)

df = df.rename({'평균평형' : 'apt_size'}, axis = 1)
df = df.rename({'평균시세' : 'apt_price'}, axis = 1)



print(df)