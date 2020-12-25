import os
os.chdir(r'G:\dachuang\unmanned_retail_project-master\recommendation\Collaborative Filtering')      #替换成对应的代码目录
import pandas as pd                                     #首先导入pandas和numpy
import numpy as np
import warnings
warnings.filterwarnings('ignore')
df = pd.read_csv('urp/records.dat',sep='::', names=['user_id','commodity_id','record','titmestamp'])      #利用pandas中的read_csv()对数据进行加载。数据集中的数据以tab进行分隔，我们需要设置sep = t来指定字符的分隔符号，然后通过names参数传入列名。
df.head()           #检查正在处理的数据
print(df)
commodity_name = pd.read_csv('urp/commodities.dat',sep='::', names=['commodity_id','name','genres'])          #下载商品的名称并将它们整合到数据集中
commodity_name.head()
print(commodity_name)
df = pd.merge(df, commodity_name, on='commodity_id')
print(df)    #看看合并是否成功
df.head()
df.describe()
records = pd.DataFrame(df.groupby('name')['record'].mean())        #计算每件商品的平均销量
records.head()
records['number_of_records'] = df.groupby('name')['record'].count()    #为销量设置一个阈值
records.head()
#import matplotlib.pyplot as plt                     #利用pandas中的绘图功能绘制直方图，可视化评分分布
#%matplotlib inline`
records['record'].hist(bins=50)
records['number_of_records'].hist(bins=60)          #对number_of_ratings进行可视化
#import seaborn as sns
#sns.jointplot(x='record', y='number_of_records', data=records)      #使用seaborn绘制散点图，通过jointplot()函数实现
commodity_matrix = df.pivot_table(index='user_id', columns='name', values='record')        #创建商品矩阵
commodity_matrix.head()
records.sort_values('number_of_records', ascending=False).head(10)      #列出销量前10
Fresh_Grade_Legs_user_record = commodity_matrix['Fresh Grade Legs']       
Chicken_Wings_user_record = commodity_matrix['Chicken Wings']
Fresh_Grade_Legs_user_record.head()                         
Chicken_Wings_user_record.head()
similar_to_Chicken_Wings=commodity_matrix.corrwith(Chicken_Wings_user_record)
similar_to_Chicken_Wings.head()
similar_to_Fresh_Grade_Legs = commodity_matrix.corrwith(Fresh_Grade_Legs_user_record)         #计算相关性
similar_to_Fresh_Grade_Legs.head()
corr_Fresh_Grade_Legs = pd.DataFrame(similar_to_Fresh_Grade_Legs, columns=['Correlation'])
corr_Fresh_Grade_Legs.dropna(inplace=True)
corr_Fresh_Grade_Legs.head()
corr_Chicken_Wings = pd.DataFrame(similar_to_Chicken_Wings, columns=['correlation'])
corr_Chicken_Wings.dropna(inplace=True)
corr_Chicken_Wings.head()
corr_Chicken_Wings = corr_Chicken_Wings.join(records['number_of_records'])
corr_Fresh_Grade_Legs = corr_Fresh_Grade_Legs.join(records['number_of_records'])
corr_Chicken_Wings .head()
corr_Fresh_Grade_Legs.head()
corr_Chicken_Wings[corr_Chicken_Wings['number_of_records'] > 1].sort_values(by='correlation', ascending=False).head(10)           #获取并查看和鸡翅前10项最为相关的商品
corr_Fresh_Grade_Legs[corr_Fresh_Grade_Legs['number_of_records'] > 1].sort_values(by='Correlation', ascending=False).head(10)       #获取并查看和鸡腿前10项最为相关的商品

