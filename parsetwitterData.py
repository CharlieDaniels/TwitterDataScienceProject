#parse twitter data

import json
#import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re #import regular expressions
from decimal import *

tweets_data_path = '/Users/Char/Documents/TwitterSearch/python-twitter/twitter_data7.txt'

#read data into an array called "tweets"
tweets_data = []
tweets_file = open(tweets_data_path, "r")

for line in tweets_file:
  try:
    tweet = json.loads(line)
    tweets_data.append(tweet)
  except:
    continue

#Print the number of tweets
num_tweets = len(tweets_data)
print(num_tweets)

def word_search(input):
  global di_count
  global diet_count
  global sk_count
  post = json.loads(input)
  # "text" is inside the dictionary "post".
  output = post["text"]
  if re.search('(D|d)iabetes', output):
    di_count=di_count+1
    print('diabetes count=', di_count)
  elif re.search('(D|d)iet',output):
    diet_count=diet_count+1
    print('diet count=',diet_count)
  elif re.search('(S|s)kin',output):
    sk_count=sk_count+1
    print('skin count=',sk_count)
  return output

tweets_file = open(tweets_data_path, "r")
di_count=0
diet_count=0
sk_count=0

for line in tweets_file:
  word_search(line)

print('Diet count=', diet_count)
diet_percent=100*(diet_count/float(num_tweets))
print('Percent comments containing word diet=', diet_percent)

print('Diabetes count=', di_count)
di_percent=100*(di_count/float(num_tweets))
print('Percent comments containing word diabetes=', di_percent)

print('Skin count=', sk_count)
sk_percent=100*(sk_count/float(num_tweets))
print('Percent comments containing word skin=', sk_percent)

#Plot percent of tweets with specific subject into a bar chart
terms = ['Diabetes','Diet','Skin']
x_pos = list(range(len(terms)))
width = 0.8
fig, ax = plt.subplots()
rects1=plt.bar(0,di_percent,width, color='r')
rects2=plt.bar(1,sk_percent,width, color='b')
rects3=plt.bar(2,diet_percent,width, color='g')
# Setting axis labels and ticks
ax.set_ylabel('Percent [%]', fontsize=15)
ax.set_title('Health vs. cosmetics concerns: Percent of tweets containing keywords', fontsize=10, fontweight='bold')
ax.set_xticks([p + 0.4 * width for p in x_pos])
ax.set_xticklabels(terms)
plt.grid()
plt.show()

#Count the number of followers of posters who use specific keywords
def followers_counts(input):
  post = json.loads(input)
  #"followers_count" is inside the dictionary user, which is inside the dictionary "post".
  output = post["user"]["followers_count"]
  if re.search('(D|d)iabetes', input):
  	di_followers.append(output)
  elif re.search('(D|d)iet',input):
    diet_followers.append(output)
  elif re.search('(S|s)kin',input):
    sk_followers.append(output)
  return output

#tweets_data_path2 = '/Users/Char/Documents/TwitterSearch/python-twitter/twitter_data_one_line.txt'
tweets_file = open(tweets_data_path, "r")
di_followers=[]
diet_followers=[]
sk_followers=[]
for line in tweets_file:
  followers_counts(line)

print('diabetes reach=', di_followers)
print('diet reach=',diet_followers)
print('skin reach=',sk_followers)

#Extract the first,2nd etc tweets of each list and plot them
#N is the number of terms being plot (diabetes, obesity)
N = 3
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence
fig, ax = plt.subplots()
#Increase this color matrix with the number of tweets
color = ['r','y','g','b','r','y','g','b','r','y','g','b','r','y','g','b','r','y','g','b','r','y','g','b','r','y','g','b','r','y','g','b','r','y','g','b','r','y','g','b','r']

matrix = []
matrix.append(di_followers)
matrix.append(sk_followers)
matrix.append(diet_followers)

#Find the maximum number of columns in the matrix
max_cols=len(matrix[0])
for row in matrix:
  if len(row)>max_cols:
    max_cols=len(row)

for column in range(max_cols):
  followers_tu = ()
  for row in matrix:
    if len(row)>column:
      followers_tu=followers_tu+(row[column],)
    else:
      followers_tu=followers_tu+(0,)
    #print(followers_tu)

  # Set color transparency (0: transparent; 1: solid)
  # Create a colormap
  customcmap = [(w/12.0,  w/48.0, 0.05) for w in range(len(diet_followers))]

  ax.set_ylabel('Number of Followers')
  ax.set_title('Audience for subtopics of microbiome tweets on twitter')
  ax.set_xticks(ind+width)
  ax.set_xticklabels(('Diabetes','Skin','Diet'))
  p1 = ax.bar(ind, followers_tu, width, color=color[column]) #color=customcmap[column])
plt.show()
