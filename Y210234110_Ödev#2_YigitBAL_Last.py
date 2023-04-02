#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import matplotlib.pyplot as plt


# In[3]:


import seaborn as sns


# In[4]:


import statistics


# In[5]:


from statistics import mean


# In[6]:


import operator


# In[7]:


df = pd.read_csv('melb_data.csv')


# In[8]:


df.head()


# In[9]:


df.shape


# In[10]:


df.sample(4)


# In[11]:


df.describe


# In[12]:


df.nunique()


# In[13]:


df.columns


# In[217]:


df.isna().sum()


# In[14]:


df['Suburb'].unique()


# In[15]:


df['Suburb'].unique().sum()


# In[16]:


len(df['Suburb'].unique())


# In[17]:


#unique olan Suburb kasabaların uzunluğu ile nunique olan Suburb kasabaların uzunluğu birbirine eşit olduğunu hesapladık.


# In[18]:


#(314 = 314)


# In[19]:


df['Suburb'].nunique()


# In[20]:


len(df['Suburb'].nunique())


# In[ ]:


df['Address'].unique()


# In[21]:


df['Address'].nunique()


# In[22]:


len(df['Address'].unique())


# In[23]:


#yine aynı şekilde, unique olan Address'ler ile nunique olan Address'ler eşittir. (13378 = 13378)


# In[24]:


df['Rooms'].unique()


# In[25]:


len(df['Rooms'].unique())


# In[26]:


df['Rooms'].nunique()


# In[27]:


# Burada da , Rooms uzunlukları, Unique ve Nunique değerleri birbirine eşittir. ( 9 = 9)


# In[28]:


df['Type'].unique()


# In[29]:


len(df['Type'].unique())


# In[30]:


df['Type'].nunique()


# In[31]:


#Type değerleri de Unique ve Nunique ortamda Birbirine eşittir. ( 3 = 3)


# In[32]:


df['Price'].unique()


# In[33]:


len(df['Price'].unique())


# In[34]:


df['Price'].nunique()


# In[35]:


#Price değerleri de Unique ve Nunique ortamda birbirine eşittir.


# In[36]:


df['Method'].unique()


# In[37]:


len(df['Method'].unique())


# In[38]:


df['Method'].nunique()


# In[39]:


#Method kriteri de Unique ve Nunique ortamda da 5 değerine eşittir.


# In[40]:


df['SellerG'].unique()


# In[41]:


len(df['SellerG'].unique())


# In[42]:


df['SellerG'].nunique()


# In[43]:


# SellerG değeri de Unique ve Nunique ortam olmak üzere her iki ortamda da birbirine eşittir.


# In[44]:


df['Date'].unique()


# In[45]:


len(df['Date'].unique())


# In[46]:


df['Date'].nunique()


# In[47]:


# Date değerleri de birbirine eşittir.


# In[48]:


df['Distance'].unique()


# In[49]:


len(df['Distance'].unique())


# In[50]:


df['Distance'].nunique()


# In[51]:


# Distance değerleri de birbirine eşittir.


# In[52]:


df['Postcode'].unique()


# In[53]:


len(df['Postcode'].unique())


# In[54]:


df['Postcode'].nunique()


# In[55]:


#Postcode değerleri de birbirine eşittir.


# In[56]:


df['Bedroom2'].unique()


# In[57]:


len(df['Bedroom2'].unique())


# In[58]:


df['Bedroom2'].nunique()


# In[59]:


#Bedroom2 değeri de birbirine eşittir.


# In[60]:


df['Bathroom'].unique()


# In[61]:


len(df['Bathroom'].unique())


# In[62]:


df['Bathroom'].nunique()


# In[63]:


#Bathroom değerleri de birbirine eşittir.


# In[64]:


df['Car'].unique()


# In[65]:


len(df['Car'].unique())


# In[66]:


df['Car'].nunique()


# In[67]:


df['Car'].isna()


# In[68]:


df['Car'].shape


# In[69]:


df['Car'].unique().sum()


# In[70]:


# Evet, sizin de görebildiğiniz gibi Car feature'unda sadece 1 değer Nan değeri gelmektedir.


# In[71]:


#İlk Unique değerleri hesapladığımızda 12 değerine ulaşmıştık.


# In[72]:


#Fakat diğer bir yandan ise Nunique değerlerinde 11 değerine ulaştık.


# In[73]:


# 1 adet Nan değeri Car Feature'unda değişkenlik göstermektedir.


# In[74]:


# Bu sebeple şu ana kadar 1 adet Car özelliğinde Unique değere sahibiz. O değer de 'Nan' değeridir.


# In[75]:


df['Landsize'].unique()


# In[76]:


len(df['Landsize'].unique())


# In[77]:


df['Landsize'].nunique()


# In[78]:


# Landsize değeri Unique ve Nunique ortamda birbirine eşittir.


# In[79]:


df['BuildingArea'].unique()


# In[80]:


len(df['BuildingArea'].unique())


# In[81]:


df['BuildingArea'].nunique()


# In[82]:


# BuildingArea özelliğinde de 1 adet farklılık bulunmaktadır, şimdi bu farklılığın hangi değer olduğunu bulalım.


# In[83]:


df['BuildingArea'].unique().sum()


# In[84]:


#BuildingArea özelliğinde de 1 adet nan değeri unique değerdir.


# In[85]:


#Bu durumun kanıtı olarak listelemedeki ilk değer nan değeri olarak gözükmektedir.


# In[86]:


#Şu ana kadar Unique değer sayısı 2 adettir. Car ve BuildingArea özelliklerinde birer adet (2 tane olacak şekilde)


# In[87]:


# nan değerleri Unique değer durumundadır.


# In[88]:


df['YearBuilt'].unique()


# In[89]:


len(df['YearBuilt'].unique())


# In[90]:


df['YearBuilt'].nunique()


# In[91]:


df['YearBuilt'].unique().sum()


# In[92]:


#YearBuilt özelliğinde de 1 adet 'nan' değeri Unique durumundadır.


# In[93]:


#Toplamda 3 adet Unique değerine sahip olmaktayız. Listedeki ilk değer görüldüğü gibi 'nan' değeridir.


# In[94]:


df['CouncilArea'].unique()


# In[95]:


len(df['CouncilArea'].unique())


# In[96]:


df['CouncilArea'].nunique()


# In[97]:


df['CouncilArea'].unique().sum()


# In[98]:


#     'Hume', nan, 'Knox',


# In[99]:


#Hume ve Knox değerleri arasında yine 1 adet 'nan' değeri bulunmaktadır.


# In[100]:


#Toplamda 4 adet Unique 'nan' değeri bulunmaktadır.


# In[101]:


df['Lattitude'].unique()


# In[102]:


len(df['Lattitude'].unique())


# In[103]:


df['Lattitude'].nunique()


# In[104]:


#Her iki ortamda da Unique ve Nunique değerleri eşittir.


# In[105]:


df['Longtitude'].unique()


# In[106]:


len(df['Longtitude'].unique())


# In[107]:


df['Longtitude'].nunique()


# In[108]:


#Her iki ortamda da Longtitude değeri eşittir.


# In[109]:


df['Regionname'].unique()


# In[110]:


len(df['Regionname'].unique())


# In[111]:


df['Regionname'].nunique()


# In[112]:


#her iki ortamda da Reigonname özelliği eşittir.


# In[113]:


df['Propertycount'].unique()


# In[114]:


len(df['Propertycount'].unique())


# In[115]:


df['Propertycount'].nunique()


# In[116]:


#her iki durumda da Properycount değeri eşittir.


# In[117]:


#Q1) see how many unique values does the dataframe have? 
#Toplamda 4 adet Unique 'nan' değeri bulunmaktadır.


# In[118]:


#Q2) describe the null values of each features
#'nan' değeri bulunan Feature'lar ise; 'Car','BuildingArea','YearBuilt','CouncilArea' özellikleridir.


# In[119]:


#Q3)Deal with the na values: try to apply the best strategy. 
#That is, if the number of nan values are too much then remove the column if the column is not necessary. 
#Otherwise, you can remove them from the dataset or you can fill na with an appropriate strategy. 
#Save the rearranged form as df2 without changing df -


# In[120]:


#Toplamda 4 adet 'nan' değeri bulunduğundan dolayı ( sayı çok az olduğu için)


# In[121]:


#bu 'nan' değerlerini Remove etmemize gerek bulunmamaktadır. 


# In[122]:


#Yaklaşık 13580 değerin içinde 4 sayısını Ignore ederek , görmezden gelebiliriz.


# In[123]:


df2 = df #herhangi bir değişiklik yapmadan df için yeni bir df olarak kaydettik.


# In[124]:


#Q4)Select the 'Suburb', 'Address', 'Rooms', 'Type', 'Price','Distance', 'Bedroom2', 'Bathroom', 'Car', 
#'Regionname', 'Propertycount' columns to describe df3: 


# In[125]:


df3 = df[['Suburb', 'Address', 'Rooms', 'Type', 'Price', 'Distance', 'Bedroom2', 'Bathroom', 'Car', 'Regionname', 'Propertycount']]


# In[126]:


#Q5)Describe the statistics of the dataset:


# In[127]:


#Without Cathegorical Data.


# In[128]:


# Burada mean, median, mode, standard deviation, variance, mode, range, maximum, minimum değerlerini hesaplayacağız.


# In[129]:


#mean


# In[130]:


df3ofPrice = df[['Price']]


# In[131]:


df3.columns


# In[132]:


df3[['Price']]


# In[133]:


df3ofPrice = df[['Price']]


# In[134]:


df3ofPrice = df[['Price']].values.tolist()


# In[135]:


print(df3ofPrice)


# In[136]:


len(df3ofPrice)


# In[137]:


list1 = [df3ofPrice]


# In[138]:


x=df3[['Price']].nunique()


# In[139]:


statistics.mean(x)


# In[140]:


#Mean değeri 2204.


# In[141]:


statistics.median(x)


# In[142]:


#Median değeri 2204.


# In[143]:


statistics.mode(x)


# In[144]:


#Mode değeri 2204.


# In[145]:


x.describe()


# In[146]:


#std ise standart variation değerini vermektedir, değeri Nan çıkmaktadır.


# In[147]:


statistics.pvariance(x)


# In[148]:


#variance değeri de 0 (sıfır) çıkmaktadır.


# In[149]:


len(x)


# In[150]:


MyRangeList = [*range(0,13580,10)]


# In[151]:


print(MyRangeList)


# In[152]:


# Range Değerimizi 10 alarak sıfırdan 13580 değerine kadar sayıları range ederek yazdırdık.


# In[153]:


#From Here, We are going to describe with Cathegorical Data.


# In[154]:


#Sort of Pros and Cons of Cathegorical Datas;

#Advantages of categorical data 
Categorical data is unique and does not have the same kind of statistical analysis that can be performed on other data.
There is no standardized interval scale which means that respondents cannot change their options before responding. It provides straightforward results. 
The results of categorical data are concrete, without subjective open-ended questions. 

#Disadvantages of categorical data 
Categorical data requires larger samples which are typically more expensive to gather.
The data research is most likely low sensitivity, for instance, either good/bad or yes/no.
Quantitative analysis cannot be performed on categorical data which means that numerical or arithmetic operations cannot be performed.
Ultimately, It’s beneficial to be able to categorize your data into groups, but you need quantitative data to be able to calculate results. 


# In[155]:


#Q6)Describe the counts of unique values of 'Suburb','Type','Regionname', 'Propertycount'


# In[156]:


df3['Suburb'].unique()


# In[157]:


df3['Type'].unique()


# In[158]:


df3['Regionname'].unique()


# In[159]:


#Q7)Describe the outliers by box plot: 
#Write a a loop for the object columns of df3 whose number of unique values is less than 10. 


# In[160]:


#Unique Value değeri 10'dan küçük olan Feature'lar; Bathroom, method, Type, Rooms, Reigonname olmalıdır.


# In[161]:


df3['Regionname'].unique()


# In[162]:


df3['Type'].unique()


# In[163]:


#Method ve Rooms yeni yaratılan df3 DataFramework'ünde yer almamaktadır. Bu sebeple de eklenmedi.


# In[164]:


a = df3['Regionname'].unique()


# In[165]:


b = df3['Type'].unique()


# In[166]:


plt.figure(figsize=(12,8))


# In[ ]:


#Q8)Describe the Correlation of df3


# In[167]:


import scipy as sp


# In[168]:


df3.corr(method='pearson')


# In[169]:


df3.corr(method='kendall')


# In[ ]:


#Q9)Describe the address # of rooms, # of bathrooms, distance for the highest Price house?: 


# In[185]:


df3['Price'].unique()


# In[198]:


PriceList = df3['Price'].unique()


# In[199]:


df3['Address'].unique()


# In[200]:


AdressList = df3['Address'].unique()


# In[201]:


df3['Rooms'].unique()


# In[202]:


RoomsList = df3['Rooms'].unique()


# In[203]:


df3['Bathroom'].unique()


# In[204]:


BathroomList = df3['Bathroom'].unique()


# In[187]:


max(df3['Price'].unique())


# In[324]:


dfNew= df3[['Price','Address','Rooms','Bathroom','Regionname']]


# In[325]:


dfNew.shape


# In[326]:


dfNew.head()


# In[327]:


dfNew.head()


# In[328]:


print(dfNew['Price'].max())


# In[329]:


dfNew.iloc[9000]


# In[330]:


dfNew.loc[900,'Price']


# In[331]:


dfNew.iloc[:13580]


# In[332]:


dfNew.loc[:'Price']


# In[334]:


dfNew.iloc[list(dfNew.Price == 9000000.0)]


# In[335]:


#Burada sürekli olarak price değerini string olarak atadığı için sürekli olarak hata almıştı.


# In[336]:


#305. satırdaki gibi list olarak sıralandığında sonuç alınmaktadır.


# In[ ]:





# In[ ]:





# In[ ]:





# In[337]:


#Q10)Is there any signaficant relation between Regionname and Price?


# In[338]:


df[['Price','Regionname']].nunique()


# In[339]:


df3['Regionname'].unique()


# In[340]:


df3['Price'].unique()


# In[341]:


df3['Price'].max()


# In[342]:


df3['Price'].min()


# In[343]:


df[['Price','Regionname']].describe()


# In[344]:


df[['Regionname']].describe()


# In[345]:


df[['Price']].describe()


# In[347]:


dfNew.loc[:, lambda dfNew: ['Regionname', 'Price']]


# In[348]:


dfNew.loc[:,('Price','Regionname')]


# In[352]:


dfNew.loc[:'Regionname']


# In[ ]:


#Regionname'i dfNew df içine ekledim, sürekli olarak dataset'in içinde bulunmadığı hatası veriyordu Regionname için !


# In[354]:


dfNew.sort_values('Price',axis=0, ascending = True)


# In[ ]:


#Yukarıdaki yapılan sıralamadan yola çıkarak, Regionname'i Southern Metropolitan olan Regionname'ler


# In[ ]:


#Price'ı çok yüksek olan Regionname'lere sahiptir.


# In[ ]:


#Diğer bir yandan ise Western Metropolitan olan Regionname'ler ise,


# In[ ]:


#Fiyatları düşük olan Price'lı evler.

