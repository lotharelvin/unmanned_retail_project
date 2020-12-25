import os
os.chdir(r'G:\dachuang\unmanned_retail_project-master\recommendation\Collaborative Filtering')      #替换成对应的代码目录
import pandas as pd                                     #首先导入pandas和numpy
import numpy as np
import warnings
warnings.filterwarnings('ignore')
df = pd.read_csv('ml-1m/ratings.dat',sep='::', names=['user_id','item_id','rating','titmestamp'])      #利用pandas中的read_csv()对数据进行加载。数据集中的数据以tab进行分隔，我们需要设置sep = t来指定字符的分隔符号，然后通过names参数传入列名。
df.head()           #检查正在处理的数据
#print(df)
movie_titles = pd.read_csv('ml-1m/movies.dat',sep='::', names=['item_id','title','genres'])          #下载电影的标题并将它们整合到数据集中
movie_titles.head()
#print(movie_titles)
#movie_titles['item_id'] = movie_titles['item_id'].apply(int)
#df['item_id'] = df['item_id'].apply(int)
df = pd.merge(df, movie_titles, on='item_id')
#print(df)    #看看合并是否成功
df.head()
df.describe()
ratings = pd.DataFrame(df.groupby('title')['rating'].mean())        #计算每部电影的平均分
ratings.head()
ratings['number_of_ratings'] = df.groupby('title')['rating'].count()    #为评分次数设置一个阈值
ratings.head()
#import matplotlib.pyplot as plt                     #利用pandas中的绘图功能绘制直方图，可视化评分分布
#%matplotlib inline
ratings['rating'].hist(bins=50)
ratings['number_of_ratings'].hist(bins=60)          #对number_of_ratings进行可视化
#import seaborn as sns
#sns.jointplot(x='rating', y='number_of_ratings', data=ratings)      #接下来探索电影评分和被评分次数之间的关系。使用seaborn绘制散点图，通过jointplot()函数实现
movie_matrix = df.pivot_table(index='user_id', columns='title', values='rating')        #创建电影矩阵
movie_matrix.head()
ratings.sort_values('number_of_ratings', ascending=False).head(10)
AFO_user_rating = movie_matrix['Air Force One (1997)']          #假设某用户看过《空军一号》和《超时空接触》，我们想根据观看历史向该用户推荐电影。通过计算这两个电影和数据集中其他电影的之间的相关性，寻找与之最为相似的电影，为用户进行推荐。首先，用movie_matrix中的电影评分创建一个dataframe。
contact_user_rating = movie_matrix['Contact (1997)']
AFO_user_rating.head()                          #Dataframe中包含user_id和对应用户给这两个电影的评分
contact_user_rating.head()
similar_to_air_force_one=movie_matrix.corrwith(AFO_user_rating)
similar_to_air_force_one.head()
similar_to_contact = movie_matrix.corrwith(contact_user_rating)         #计算《超时空接触》和其他电影之间的相关性
similar_to_contact.head()
corr_contact = pd.DataFrame(similar_to_contact, columns=['Correlation'])
corr_contact.dropna(inplace=True)
corr_contact.head()
corr_AFO = pd.DataFrame(similar_to_air_force_one, columns=['correlation'])
corr_AFO.dropna(inplace=True)
corr_AFO.head()
corr_AFO = corr_AFO.join(ratings['number_of_ratings'])
corr_contact = corr_contact.join(ratings['number_of_ratings'])
corr_AFO .head()
corr_contact.head()
corr_AFO[corr_AFO['number_of_ratings'] > 100].sort_values(by='correlation', ascending=False).head(10)           #获取并查看前10部最为相关的电影 阈值设定为了100
corr_contact[corr_contact['number_of_ratings'] > 100].sort_values(by='Correlation', ascending=False).head(10)       #获取并查看与《超时空接触》最为相关的前10部电影

