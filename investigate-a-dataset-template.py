#!/usr/bin/env python
# coding: utf-8

# <a id='intro'></a>
# ## Introduction
# 
# > In this report, I am going to be looking at different factors of movies and if different variables are correlated to others. I will be looking at vote count and vote average. Basically how many people rated a movie and what the average rating was
# 
# > The dataset that we have is over 10,000 movies, big and small. It includes data like the cast, producing company, budget, release date, popularity, and more. I won't be using all of these columns but they're nice to have.

# In[2]:


# Use this cell to set up import statements for all of the packages that you
#   plan to use.
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import seaborn as sns
import matplotlib.plyplot as plt

# Remember to include a 'magic word' so that your visualizations are plotted
#   inline with the notebook. See this page for more:
#   http://ipython.readthedocs.io/en/stable/interactive/magics.html


# <a id='wrangling'></a>
# ## Data Wrangling
# 

# In[3]:


df = pd.read_csv("tmdb-movies.csv")
df.head()


# ### Data Cleaning
# 
# > You can tell that there is some issues that can be fixed. Issues with the cast, genres, production companies. Let's clean that up (I added a head() call at the end of each cell so you can see what happened)

# In[4]:


df['cast'] = df['cast'].str.replace('|', ', ')
df['genres'] = df['genres'].str.replace('|', ', ')
df['production_companies'] = df['production_companies'].str.replace('|', ', ')
df.head()


# In[5]:


df.drop(['overview', 'tagline', 'homepage', 'id', 'imdb_id', 'keywords'], axis=1, inplace=True)
df.head()


# In[7]:


df.describe()


# There are still some 0 values in revenue, runtime, and budget. In order to not skew the data, lets fix those.

# In[22]:


mean_revenue = df['revenue'].mean()
df['revenue'] = df['revenue'].replace(0, mean_revenue)
mean_revenue_adj = df['revenue_adj'].mean()
df['revenue_adj'] = df['revenue_adj'].replace(0, mean_revenue_adj)


# In[23]:


df.describe()


# Revenue is done, lets do budget.

# In[24]:


mean_budget = df['budget'].mean()
df['budget'] = df['budget'].replace(0, mean_revenue)
mean_budget_adj = df['budget_adj'].mean()
df['budget_adj'] = df['budget_adj'].replace(0, mean_revenue_adj)


# In[25]:


df.describe()


# Lastly, let's fix the runtime zeroes.

# In[20]:


mean_runtime = df['runtime'].mean()
df['runtime'] = df['runtime'].replace(0, mean_runtime)


# In[21]:


df.describe()


# Let's see the null value situation in our panda dataframe...

# In[46]:


df.info()


# Looks like theres some Null values, we can replace them all with 'None', since they are all for string values like cast or company.

# In[50]:


df.fillna('None', inplace=True) #filling in null values with 'None'
df.info()


# <a id='eda'></a>
# # Exploratory Data Analysis
# 
# 
# 
# ## Question 1: How do different variables affect viewer voting ratings?

# ### Histogram

# In[52]:


df['vote_average'].hist(figsize=(10, 8))


# This is a histogram of voter ratings for each movie. This stat seemed like the one that didn't have outliers and didn't have a crazy range (like budget or revenue), but still showed how much people that saw this movie liked it. If a movie company wanted one stat to be the highest, (aside from revenue), I feel like budget would be their top priority. 

# ### Comparison

# #### Budget vs Viewer Rating

# In[65]:


df.plot(x='budget', y='vote_average', kind='scatter')


# This was an interesting plot to look at, because it shows that there really isn't a strong correlation between budget and voter ratings. 
# 
# Even at 0 budget, it can be a really good movie or a really bad one. And the higher the budget, there are usually higher ranges, but the highest ratings come from the low budget films.

# #### Popularity vs Viewer Ratings

# In[67]:


df.plot(x='popularity', y='vote_average', kind='scatter')


# This chart, similar to the budget one, shows that there is little correlation between popularity and viewer ratings.
# 
# The one correlation is that the vote average doesn't get below 5 unless the popularity is very low. This might change if we had data on more popular movies. But with the data given, there is still an average of around 7-8.

# ## Question 2: Does vote count correlate with any other variables?

# #### Histogram

# In[27]:


df['vote_count'].hist(figsize=(10, 8))


# This is a histogram of vote counts. But as you can see we lose a lot of data by showing every value. Let's cut it down from 0 to 2000

# In[28]:


df['vote_count'].hist(figsize=(10, 8), range=(0, 2000))


# More of the same it looks like. Let's cut it down some more to get more info.

# In[20]:


df['vote_count'].hist(figsize=(10, 8), range=(0, 200))


# This helps us to see more of the data, most of it is between 0-25, then slowly goes down every interval. It helps me to visualize the first histogram more accurately to see this data.

# #### Comparison

# In[25]:


df.plot(x='popularity', y='vote_count', kind='scatter')


# From this, we can gather that popularity has a positive correlation with vote count. This makes sense because the more popular a movie is, the more votes it should get with a rating, either good or bad. The surprising part is that there can be movies that aren't that popular but get a lot of votes.

# In[29]:


df.plot(x='budget', y='vote_count', kind='scatter')


# As we can see, budget and vote count is not really correlated to one another. So the number of votes or ratings that a movie gets does not necessarily depend on the budget of the movie.

# ## Conclusion

# My favorite thing that I got out of this project is the little correlation that I found between ratings and popularity, and ratings and budget. It was nice to see that a movie can still get great or terrible ratings no matter the popularity or hoe much money they spent on it. However, as I imagined, popularity does have a factor in how many votes there are for a movie, even if the overall rating isn't better, more people will review it.
# 
# Some of the limitations that I found was there was a lot of missing data and the movies that it had where skewed. What I mean is that there were a lot of movies that are unpopular, with a lot budget and a lot revenue. It would have been cool to look at only big box office movies, or just to have more of those instead of just a handful.
# 
# Another limitation where I was not sure of what to do was when filling in the zeroes with missing data, it felt like it was messing up the data to fill in the zeroes with the average. It didn't end up changing much but I was not sure what else to do with the data given.

# In[ ]:




