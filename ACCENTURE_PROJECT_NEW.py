#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np


# In[ ]:


content = pd.read_csv('/content/Content.csv',index_col=0)
reactiontypes = pd.read_csv('/content/ReactionTypes.csv',index_col=0)
reactions = pd.read_csv('/content/Reactions.csv',index_col=0)


# In[ ]:


# Checking for missing values in each column on reactions
missing_values_reactions = reactions.isnull().sum()
missing_values_reactions


# In[ ]:


#drop the URL column from 'content'
content.drop('URL', inplace=True, axis=1)

# #drop User ID from reactions
# reactions.drop('User ID', inplace=True, axis=1)

# #drop User ID from content
# content.drop('User ID', inplace=True, axis=1)

#Rename "Type" column to "Content Type" in content_clean dataframe
content.rename(columns={'Type': 'Content Type'}, inplace=True)


# In[ ]:


#drop all the rows with null values from content
content_clean = content.dropna()

#drop all the rows with null values from reactiontypes
reactiontypes_clean = reactiontypes.dropna()

#drop all the rows with null values from reactions
reactions_clean = reactions.dropna()


# In[ ]:


#Size of the dataframes

print(content_clean.shape)
print(reactiontypes_clean.shape)
print(reactions_clean.shape)


# In[ ]:


#Priviewing the summary of the dataset

print(content_clean.info())
print("-----")
print(reactiontypes_clean.info())
print("-----")
print(reactions_clean.info())


# In[ ]:


# Finding unique values in 'Type' and 'Category' columns in "Content_clean"
unique_types = content['Content Type'].unique()
unique_categories = content['Category'].unique()

print("Unique values in 'Type' column:", unique_types)

print("-----")

print("Unique values in 'Category' column:", unique_categories)


# In[ ]:


#turn all observations to lowecase in "Content" column Type
content_clean['Category'] = content_clean['Category'].str.lower()

# Removing double quotes from 'Type' column
content_clean['Category'] = content_clean['Category'].str.replace('"', '', regex=False)


# In[ ]:


# Finding unique values in 'Type' and 'Category' columns in "Content"
unique_types = content_clean['Content Type'].unique()
unique_categories = content_clean['Category'].unique()

print("Unique values in 'Type' column:", unique_types)

print("-----")

print("Unique values in 'Category' column:", unique_categories)


# In[ ]:


#viewing cleaned datasets

#content_clean

#reactiontypes_clean.shape

reactions_clean.shape


# In[ ]:





# In[ ]:


#download clean datasets

from google.colab import files

content_clean.to_csv('content_clean.csv')
files.download('content_clean.csv')

reactiontypes_clean.to_csv('reactiontypes_clean.csv')
files.download('reactiontypes_clean.csv')

reactions_clean.to_csv('reactions_clean.csv')
files.download('reactions_clean.csv')


# In[ ]:


# Creating a pivot table with users as rows, categories as columns, and average sentiment score as values
user_sentiment_pivot = top_categories_data.pivot_table(
    index='User ID',
    columns='Category',
    values='Score',
    aggfunc='mean'
)

# Calculating the correlation matrix
user_sentiment_correlation = user_sentiment_pivot.corr()

# Displaying the correlation matrix
user_sentiment_correlation

