import pandas as pd

df = pd.read_csv('Z:/data.csv')

# drop useless
df.drop('Unnamed: 0', axis = 1, inplace = True)

def drop_useless(data_frame, column, useless_list):
    useless_idx = pd.DataFrame({})
    for useless in useless_list :
        idx = data_frame[
            (data_frame[column] != useless)
        ]
        useless_idx.append(idx, ignore_index = True)

    data_frame.drop(useless_idx.index, inplace = True)
    

useless_age_list = ['19세이하', '20~29', '30~39', '40~49', '50~59', '60~69', '70세이상', '미분류', '해당사항없음']
drop_useless(df, 'age', useless_age_list)

# df.drop(['id'], axis = 1, inplace = True)

# useless_isEmp_idx = df[
#     (df['is_emp'] != '그룹사직원') 
#     & (df['is_emp'] != '해당사항없음')
#     ]
# df.drop(useless_isEmp_idx.index, inplace = True)

print(df)
