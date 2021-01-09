#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tweepy
import webbrowser
import json
import datetime


# In[2]:


consumer_key=''
consumer_secret_key = ''


# In[3]:


callback_url='oob'


# In[4]:


auth = tweepy.OAuthHandler(consumer_key,consumer_secret_key,callback_url)


# In[5]:


try:
    redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
    print('Error! Failed to get request token.')


# In[6]:


redirect_url


# In[8]:


webbrowser.open(redirect_url)


# In[9]:


user_pint_input = input('what is pin value')


# In[10]:


try:
    auth.get_access_token(user_pint_input)
except tweepy.TweepError:
    print('Error! Failed to get access token.')


# In[11]:


print(auth.access_token, auth.access_token_secret)


# In[12]:


api=tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


# In[13]:


me = api.me()


# In[14]:


print(me.screen_name)


# In[15]:


query = "#IndiaFightsCorona"


# In[14]:


tweets = api.search(q=query, lang="en", rpp=10, count=1)


# In[15]:


tweets = tweepy.Cursor(api.search,q="Covid", tweet_mode='extended').items(200)


# In[67]:


tweets_list = [[tweet.text, tweet.created_at, tweet.id_str, tweet.user.name, tweet.user.screen_name, tweet.user.id_str, tweet.user.location, tweet.user.url, tweet.user.description, tweet.user.verified, tweet.user.followers_count, tweet.user.friends_count, tweet.user.favourites_count, tweet.user.statuses_count, tweet.user.listed_count, tweet.user.created_at, tweet.user.profile_image_url_https, tweet.user.default_profile, tweet.user.default_profile_image] for tweet in tweets]


# In[55]:


with open("Sample.json", "w") as p: 
     json.dump(tweets[0]._json, p)


# In[16]:


advanced_query='(Covid19 OR Covid OR Coronavirus OR Chinavirus OR COVID OR COVID19) AND -(RECRUITMENT EXAMS OR exam OR NEET OR UPSC OR student) AND (@pmoindia OR @MoHFW_INDIA OR @drharshvardhan)'
lang='hi'


# In[70]:


tweets = tweepy.Cursor(api.search,q=advanced_query,lang=lang,tweet_mode='extended').items(1)


# In[71]:



with open("sample_a.json", "a") as p:
    for tweet in tweets:
        
        sa = 'my tweet'
        hashtag_string=''
        mentions_string=''
        
        sa = tweet
        
        userDict = sa._json.__getitem__('user')
        screen_name=userDict.__getitem__('screen_name')
        id=userDict.__getitem__('id')
        
        sa._json.__setitem__('poi_name',screen_name)
        sa._json.__setitem__('poi_id',id)
        
        entity_dct = sa._json.__getitem__('entities')
        
        hastags_list = entity_dct.__getitem__('hashtags')
        
        for i in hastags_list:
            hashtag_string =  i.__getitem__('text') + ' ' +hashtag_string
        
        sa._json.__setitem__('hashtag',hashtag_string)
        
        user_mention_list=entity_dct.__getitem__('user_mentions')
        
        for i in user_mention_list:
            mentions_string = i.__getitem__('screen_name') + ' ' +mentions_string
            
        sa._json.__setitem__('mentions',mentions_string)
        
        json.dump(sa._json,p,indent=4)
     


# In[69]:


userDict = sa._json.__getitem__('user')
screen_name=userDict.__getitem__('screen_name')
id=userDict.__getitem__('id')
sa._json.__setitem__('poi_name',screen_name)
sa._json.__setitem__('poi_id',id)


# In[54]:


entity_dct = sa._json.__getitem__('entities')
hastags_list = entity_dct.__getitem__('hashtags')
  


# In[58]:


hashtag_string=''
for i in hastags_list:
    hashtag_string =  i.__getitem__('text') + ' ' +hashtag_string 


# In[60]:


sa._json.__setitem__('hashtag',hashtag_string)


# In[63]:


user_mention_list=entity_dct.__getitem__('user_mentions')


# In[64]:


mentions_string=''
for i in user_mention_list:
    mentions_string = i.__getitem__('screen_name') + ' ' +mentions_string


# In[66]:


sa._json.__setitem__('mentions',mentions_string)


# In[ ]:




