from sklearn.preprocessing import OneHotEncoder

#注：当特征是字符串类型时，需要先用 LabelEncoder() 转换成连续的数值型变量，再用 OneHotEncoder() 二值化 。
enc = OneHotEncoder()
enc.fit([[0, 0, 3], [1, 1, 0], [0, 2, 1], [1, 0, 2]])    # fit来学习编码
array = enc.transform([[0, 1, 3]]).toarray() # 进行编码
print(array)
# 输出：array([[ 1., 0., 0., 1., 0., 0., 0., 0., 1.]])

import pandas as pd
import numpy as np

sex_list = ['MALE', 'FEMALE', np.NaN, 'FEMALE', ]
df = pd.DataFrame({'SEX': sex_list})
print(df)
'''
# 输出
     SEX
0    MALE
1    FEMALE
2    NaN
3    FEMALE
'''

df = pd.get_dummies(df['SEX'], prefix='IS_SEX')
print(df)

'''
# 输出
  IS_SEX_FEMALE   IS_SEX_MALE
0    0               1
1    1               0
2    0               0
3    1               0
'''