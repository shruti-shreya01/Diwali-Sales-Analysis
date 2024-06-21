#!/usr/bin/env python
# coding: utf-8

# # Import libraries

# In[258]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# # Load data

# In[259]:


df= pd.read_csv('Diwali Sales Data.csv', encoding='latin1')


# In[260]:


df.head()


# # Data cleaning

# In[261]:


#percentage of data that is null
df.isnull().mean()*100


# In[262]:


df.shape


# In[264]:


#drop unnecessary columns
df.drop(columns=['Status', 'unnamed1'],axis=1, inplace=True)


# In[265]:


#After dropping columns, the remaining missing values
df.isnull().sum()


# In[266]:


#Remove missing data
df.dropna(inplace=True)


# In[18]:


df.isnull().sum()


# In[267]:


df.info()


# In[268]:


#Change the data type of amount from float to integer
df['Amount']=df['Amount'].astype('int')


# In[269]:


#find statistics of data and analyse
df[['Age','Amount','Orders']].describe()


# In[270]:


#Use boxplot to observe for outliers if any and remoe if it troubles
sns.boxplot(df[['Amount','Age','Orders']])


# # EDA

# ## Gender

# In[276]:


# Plot gender vs its count
ax=sns.countplot(x='Gender',data=df)
sns.set(rc={'figure.figsize':(6,3)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[58]:


# Plot gender vs amount spent 
gender_amt= df.groupby('Gender')['Amount'].sum().reset_index()
gender_amt


# In[74]:


plt.bar(gender_amt['Gender'],gender_amt['Amount'],color=['brown','green'])
plt.xlabel('Gender')
plt.ylabel('Amount')


# #From above graphs we can see that most of the buyers are females and even the purchasing power of females are greater than men

# ## Age

# In[81]:


ax= sns.countplot(x='Age Group', data=df,hue='Gender')
for bar in ax.containers:
    ax.bar_label(bar)


# In[98]:


# Total Amount vs Age Group
sales_age= df.groupby(['Age Group'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sales_age


# In[99]:


sns.barplot(x='Age Group', y='Amount', data=sales_age)


# In[100]:


#Orders vs age
order_age= df.groupby(['Age Group'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False)
order_age


# In[101]:


sns.barplot(x='Age Group', y='Orders', data=order_age)


# ## State

# In[138]:


# total number of orders from top 10 states
orders_state= df.groupby(['State'],as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
orders_state


# In[152]:


sns.barplot(x='State',y='Orders', data= orders_state)
sns.set(rc={'figure.figsize':(11,10)})


# In[153]:


# total amount/sales from top 10 states
sales_state= df.groupby('State', as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)


# In[167]:


sns.barplot(x='State', y='Amount', data=sales_state)
sns.set(rc={'figure.figsize':(15,9)})


# ## Marital status

# In[195]:


ax=sns.countplot(data= df, x='Marital_Status',hue='Gender')
sns.set(rc={'figure.figsize':(6,4)})
for bar in ax.containers:
    ax.bar_label(bar)


# In[201]:


sales_married= df.groupby(['Marital_Status','Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending= False)
sns.barplot(x= 'Marital_Status', y='Amount', data= sales_married, hue='Gender')


# In[277]:


# From above graphs we can see that most of the buyers are married (women) and they have high purchasing power


# ## Occupation

# In[228]:


sns.countplot(x='Occupation', data= df)
sns.set(rc={'figure.figsize':(20,5)})


# In[231]:


sales_occupation= df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(x='Occupation', y='Amount', data=sales_occupation)


# In[279]:


#From above graphs we can see that most of the buyers are working in IT, Healthcare and Aviation sector


# ## Product Category

# In[253]:


ax= sns.countplot(x='Product_Category', data=df)
sns.set(rc={'figure.figsize':(24,6)})
for bar in ax.containers:
    ax.bar_label(bar)


# In[254]:


sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_Category',y= 'Amount')


# In[280]:


#From above graphs we can see that most of the sold products are from Food, Clothing and Electronics category


# In[255]:


sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_ID',y= 'Orders')


# # Conclusion

# Married women age group 26-35 yrs from UP, Maharastra and Karnataka working in IT, Healthcare and Aviation are more likely to buy products from Food, Clothing and Electronics category
