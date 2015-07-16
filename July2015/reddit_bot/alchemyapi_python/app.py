# coding: utf-8
import praw
import time
#import IBM Watson Text Analysis API
from alchemyapi import AlchemyAPI
alchemyapi = AlchemyAPI()

# Define Reddit bot
user_agent = ("depression_bot v0.1")
r = praw.Reddit(user_agent=user_agent)
# Retreive Depression Subreddit
subreddit = r.get_subreddit("depression")
submission = subreddit.get_new_by_date(limit=20)
# loop through posts
for info in submission:
    print "TITLE: ", info.title
    print "TEXT: ", info.selftext
    print "SCORE: ", info.score
    myText = info.selftext
    response = alchemyapi.sentiment("text", myText)
    print "Sentiment: ", response["docSentiment"]["type"], ' ', response["docSentiment"]['score']
    print "----------------------\n"
