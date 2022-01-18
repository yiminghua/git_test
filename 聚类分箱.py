from sklearn.cluster import KMeans
import pandas as pd

k = 3
kmodel=KMeans(n_clusters=k)  #k为聚成几类
kmodel.fit(data.reshape(len(data), 1)) #训练模型
c = pd.DataFrame(kmodel.cluster_centers_) #求聚类中心
c = c.sort_values(by='列索引') #排序　　
w = pd.rolling_mean(c, 2).iloc[1:] #用滑动窗口求均值的方法求相邻两项求中点，作为边界点
w = [0] + list(w[0] + [data.max()])  #把首末边界点加上
d3= pd.cut(data, w, labels=range(k)) #cut函数