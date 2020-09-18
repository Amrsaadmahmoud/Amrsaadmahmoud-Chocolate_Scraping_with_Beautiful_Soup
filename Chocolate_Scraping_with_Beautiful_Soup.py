
# coding: utf-8

# In[43]:

from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# In[9]:

webpage=requests.get('https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/cacao/index.html')


# In[10]:

webpage_content=webpage.content
soup=BeautifulSoup(webpage_content,"html.parser")


# In[21]:

#rating data
rate_data=soup.find_all(attrs={'class':'Rating'})
ratings=[]
for rating_data in rate_data[1:]:
    ratings.append(float(rating_data.string))


# In[22]:

print(ratings)


# In[24]:

#create a histogram of the ratings values
plt.hist(ratings)
plt.show()


# ***Which chocolatier makes the best chocolate?***

# In[25]:

company_data=soup.select(".Company")
company_name=[]
for company in company_data[1:]:
    company_name.append(company.string)


# In[26]:

print(company_name)


# In[29]:

#create a dataframe with two columns[company_name and rating]

df=pd.DataFrame({'Company_name':company_name,'Ratings':ratings})


# In[31]:

df.head(7)


# In[32]:

avg_rating=df.groupby('Company_name').Ratings.mean()


# In[35]:

top_ten=avg_rating.nlargest(10)


# In[36]:

top_ten


# ***Is more cacao better?***

# In[37]:

coco=soup.select('.CocoaPercent')
coco_percent=[]
for caco in coco[1:]:
    coco_percent.append(int(float(caco.string[:-1])))


# In[38]:

print(coco_percent)


# In[39]:

df['Cocoa_Percent']=coco_percent


# In[40]:

df.head(5)


# In[44]:

plt.scatter(df.Cocoa_Percent, df.Ratings)
z = np.polyfit(df.Cocoa_Percent, df.Ratings, 1)
line_function = np.poly1d(z)
plt.plot(df.Cocoa_Percent, line_function(df.Cocoa_Percent), "r--")
plt.show()

