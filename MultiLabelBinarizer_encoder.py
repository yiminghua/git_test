from sklearn.preprocessing import MultiLabelBinarizer
#用于label encoding，生成一个(n_examples * n_classes)大小的0~1矩阵，每个样本可能对应多个label。
mlb = MultiLabelBinarizer()
print(mlb.fit_transform([(1, 2), (3,)]))
'''
# 输出
array([[1, 1, 0],
       [0, 0, 1]])
'''

print(mlb.classes_)
# 输出：array([1, 2, 3])

print(mlb.fit_transform([{'sci-fi', 'thriller'}, {'comedy'}]))
'''
# 输出：array([[0, 1, 1],
       [1, 0, 0]])
'''

print(list(mlb.classes_))
# 输出：['comedy', 'sci-fi', 'thriller']
