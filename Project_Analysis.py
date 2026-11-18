#!/usr/bin/env python
# coding: utf-8

# # World Happiness Report 2019
# ## 1. Data Loading
# ## 2. Data Exploration
# ## 3. Data Analysis

# In[202]:


import pandas as pd


# In[203]:


# Read the CSV file
df=pd.read_csv(r"C:\Users\sarah\OneDrive - King Khalid University\Desktop\Pandas\2019.csv")


# In[204]:


# Show the first 5 rows
df.head()


# In[205]:


# Show information about the dataset
df.info()


# In[206]:


# Show the number of rows and columns
df.shape


# In[207]:


# Show all column names
df.columns


# In[282]:


df.duplicated().sum()


# In[208]:


# Show statistical information about numerical columns
df.describe()


# In[212]:


# Get information about the country names
df['Country or region'].describe()


# In[213]:


# Show all unique country names
df['Country or region'].unique()


# In[221]:


# Check for missing values in the dataset
df.isnull()


# In[280]:


# Count missing values in each column
df.isnull().sum()


# In[209]:


# Calculate the average happiness score
df['Score'].mean()


# In[210]:


print('Min of Happiness_Score=',df['Score'].min())


# In[211]:


print('Max of Happiness_Score=',df['Score'].max())


# In[158]:


df['Score'].value_counts().sort_index()


# In[259]:


# Rename columns to make them easier to use
df=df.rename(columns={'Country or region':'Country_or_region','GDP per capita':'GDP_per_capita','Social support':'Social_support','Freedom to make life choices':'Freedom_to_make_life_choices','Perceptions of corruption':'Perceptions_of_corruption'})


# In[260]:


df.head()


# In[123]:


# Find the country with the highest GDP per capita
df.groupby(['Country_or_region']).GDP_per_capita.mean().idxmax()


# In[216]:


# Find the country with the highest happiness score
df.groupby(['Country_or_region']).Score.mean().idxmax()


# In[218]:


# Select the row for Saudi Arabia
df.loc[df.Country_or_region.isin(['Saudi Arabia'])] 


# In[225]:


# Select a country using its column position
df['Country_or_region'][100]


# In[226]:


df.iloc[27] #Select the row at position 27 (Saudi Arabia)


# In[227]:


# Select the first 10 countries
df.iloc[:10,1]


# In[170]:


# Select countries from index 100 to 150
df.loc[100:150,'Country_or_region']


# In[228]:


df


# In[229]:


# Select countries with a happiness score of 5 or more
# and social support of 1.50 or more
df.loc[(df.Score>=5)&(df.Social_support>=1.50)]


# In[230]:


# Select Bahrain using isin()
df.loc[df.Country_or_region.isin(['Bahrain'])]


# In[232]:


# Calculate the average happiness score for each country
d=df.groupby('Country_or_region').Score.mean()
d


# In[233]:


# Sort the average scores from highest to lowest
d.sort_values(ascending=False)


# In[234]:


# Calculate the overall average happiness score
Country_Score_mean=df.Score.mean()
Country_Score_mean


# In[235]:


# Calculate the difference between each country's score and the average
df.Score.map(lambda p:p-Country_Score_mean)


# In[236]:


# Calculate the average social support
mean_Social_support=df.Social_support.mean()
mean_Social_support


# In[238]:


# Create a function to calculate the difference from the average
def m_Social_support(row):
    row.Social_support=row.Social_support-mean_Social_support
    return row
df.apply(m_Social_support,axis='columns')


# In[257]:


# Find the country with the highest freedom score
df.groupby('Country_or_region').Freedom_to_make_life_choices.mean().idxmax()


# In[258]:


# Find the country with the highest social support score
df.groupby('Country_or_region').Social_support.mean().idxmax()


# In[264]:


# Find the country with the highest perceptions of corruption value
df.groupby('Country_or_region').Perceptions_of_corruption.mean().idxmax()


# In[268]:


# Select Singapore to check its perceptions of corruption value 
df.loc[(df.Country_or_region=='Singapore')]


# In[273]:


df[['Score', 'GDP_per_capita', 'Social_support']].agg(['mean', 'min', 'max'])


# In[275]:


df.dtypes


# In[222]:


#There is a strong positive correlation between GDP per capita and happiness score.
#This means that countries with higher GDP per capita tend to have higher happiness scores,
#but correlation does not mean causation.
df['GDP_per_capita'].corr(df['Score'])


# In[223]:


# Calculate the correlation between social support and happiness score
df['Social_support'].corr(df['Score'])


# In[224]:


# GDP per capita has the strongest positive correlation with happiness score.
# Healthy life expectancy and social support come next.
# Freedom has a moderate positive correlation, while generosity has a very weak correlation.
df.corr(numeric_only=True)

