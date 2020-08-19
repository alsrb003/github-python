#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd


# In[10]:


df = pd.read_csv("C:/Users/Kosmo_07/Downloads/python-master/data/gapminder.tsv", sep="\t")


# In[11]:


print(df)


# In[12]:


print(df.head())


# In[13]:


print(df.tail())


# In[14]:


print(type(df))


# In[15]:


print(df.shape)


# In[16]:


print(df.columns)


# In[17]:


print(df.dtypes)


# In[18]:


print(df.info())


# In[19]:


countries = df['country']


# In[20]:


print(countries.head())


# In[21]:


print(type(countries))


# In[22]:


subset = df[['country', 'continent', 'year']]


# In[23]:


print(subset.head())


# In[24]:


print(type(subset))


# In[25]:


print(df.loc[3])


# In[26]:


print(df.iloc[3])


# In[27]:


print(df.loc[df.shape[0] - 1])


# In[28]:


print(df.iloc[-1])


# In[29]:


print(df.tail(n=1))


# In[30]:


print(df.loc[[0, 99, 999]])


# In[31]:


subset2 = df.loc[:,['year','pop']]


# In[32]:


print(subset2.head())


# In[33]:


subset3 = df.iloc[:,[2,4,-1]]


# In[34]:


print(subset3.head())


# In[35]:


u3_range = range(4)


# In[36]:


print(u3_range)


# In[37]:


print(df.iloc[:,u3_range].head())


# In[38]:


subset4 = df.iloc[:,range(0,df.shape[1],2)]


# In[39]:


print(subset4.head())


# In[40]:


grouped_year_df = df.groupby('year')


# In[41]:


print(grouped_year_df)


# In[42]:


print(type(grouped_year_df))


# In[106]:


from pandas.plotting import table


# In[107]:


import matplotlib.pyplot as plt


# In[ ]:





# In[108]:


raw = {'name':['kim','lee','park','cho','choi'],
'jan':[4,24,31,2,3],
    'fab':[25,94,57,62,70],
        'mar':[5,43,23,23,51]}


# In[109]:


df = pd.DataFrame(raw, columns = ['name','jan','fab','mar'])


# In[120]:


df['total'] = df['jan']+df['fab']+df['mar']


# In[121]:


plt.figure(figsize=(16,8))


# In[122]:


ax1 = plt.subplot(121, aspect='equal')


# In[123]:


df.plot(kind='pie',y='total',ax=ax1, autopct='%1.1f%%',
       startangle=90, shadow=False, labels=df['name'],legend = False, fontsize=14)


# In[124]:


ax2 = plt.subplot(122)


# In[125]:


plt.axis('off')


# In[126]:


tb1 = table(ax2,df,loc='center')


# In[127]:


tb1.auto_set_font_size(False)


# In[128]:


tb1.set_fontsize(14)


# In[129]:


plt.show()


# In[131]:


# sample data
raw_data = {'officer_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
        'jan_arrests': [4, 24, 31, 2, 3],
        'feb_arrests': [25, 94, 57, 62, 70],
        'march_arrests': [5, 43, 23, 23, 51]}
df = pd.DataFrame(raw_data, columns = ['officer_name', 'jan_arrests', 'feb_arrests', 'march_arrests'])
df['total_arrests'] = df['jan_arrests'] + df['feb_arrests'] + df['march_arrests']

plt.figure(figsize=(16,8))
# plot chart
ax1 = plt.subplot(121, aspect='equal')
df.plot(kind='pie', y = 'total_arrests', ax=ax1, autopct='%1.1f%%', 
 startangle=90, shadow=False, labels=df['officer_name'], legend = False, fontsize=14)

# plot table
ax2 = plt.subplot(122)
plt.axis('off')
tbl = table(ax2, df, loc='center')
tbl.auto_set_font_size(False)
tbl.set_fontsize(14)
plt.show()


# In[132]:


import matplotlib.pyplot as plt


# In[135]:


import pandas as pd


# In[137]:


s = pd.Series(['홍길동',28])


# In[138]:


print(s)


# In[139]:


s = pd.Series(['홍길동',28], index = ['Name','Age'])


# In[140]:


print(s)


# In[141]:


kor = [80, 75,90,100,65]


# In[142]:


kor_s = pd.Series(kor)


# In[143]:


kor_s.describe()


# In[144]:


scores_df = pd.DataFrame({"KOR":[80,90,75],"ENG":[90,80,70],"MATH":[80,90,85]},index =["홍길동","김철수","이영희"])


# In[145]:


print(scores_df)


# In[146]:


print(scores_df.loc['김철수'])


# In[147]:


print(type(scores_df.loc['김철수']))


# In[148]:


scores_df['TOTAL'] = scores_df['KOR'] +scores_df['ENG'] +scores_df['MATH']


# In[149]:


print(scores_df)


# In[153]:


scores_df['AVERAGE'] = scores_df['TOTAL']/3


# In[154]:


print(scores_df)


# In[155]:


scores_df['AVERAGE'] > 80


# In[156]:


filtered_df = scores_df[scores_df['AVERAGE'] >= 80]


# In[157]:


print(filtered_df)


# In[158]:


thieves_df = pd.read_csv("C:/Users/Kosmo_07/Downloads/python-master/data/thieves.txt",sep="\t")


# In[159]:


print(thieves_df)


# In[160]:


thieves_df2 = pd.read_csv("C:/Users/Kosmo_07/Downloads/python-master/data/thieves.txt",sep="\t",header=None)


# In[161]:


print(thieves_df2)


# In[164]:


from numpy import nan, NaN, NAN


# In[165]:


exam_scores = pd.Series([90,80,120,nan,95,80,-10])


# In[166]:


print(exam_scores)


# In[167]:


print(pd.isnull(exam_scores))


# In[168]:


import numpy as np


# In[169]:


print("결측자 수 : ", np.count_nonzero(exam_scores.isnull()))


# In[170]:


num_rows = exam_scores.shape[0]


# In[171]:


num_missing = num_rows - exam_scores.count()


# In[172]:


print("결측자 수 : ", num_missing)


# In[173]:


~exam_scores.isin(range(0,101))


# In[174]:


exam_scores[~exam_scores.isin(range(0,101))] = nan


# In[175]:


print(exam_scores)


# In[176]:


med_score = exam_scores[exam_scores.notnull()].median()


# In[177]:


print(med_score)


# In[179]:


exam_scores[exam_scores.isnull()] = med_score


# In[180]:


print("평균 : " , exam_scores.mean())


# In[ ]:




