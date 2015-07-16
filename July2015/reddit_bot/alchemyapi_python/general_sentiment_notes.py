# coding: utf-8
import os
import nltk.data
from alchemyapi import AlchemyAPI

#Add nltk_data to path
path = os.path.expanduser('~/nltk_data')
path in nltk.data.path

#open IBM Watson API
a = AlchemyAPI()

#cycle through Sucide not corpora
logdir = "/home/lwgray/nltk_data/corpora/reddit/"
logfiles = sorted([f for f in os.listdir(logdir) if f.endswith('.txt')])

results = {'negative': 0, 'positive': 0}
for index,note in enumerate(logfiles):
    letter = nltk.data.load('corpora/reddit/{0}'.format(note), format='raw')
    response = a.sentiment('text', letter)
    print index, note, response
    if response['docSentiment']['type'] == 'negative':
        results['negative'] += float(response['docSentiment']['score'])
    else:
        results['positive'] += float(response['docSentiment']['score'])

# Tally Score
avg_score = (results['negative'] + results['positive'])/25
if avg_score < 0:
    print "Overall Sentiment: Negative"
else:
    print "Overall Sentiment: Positive"

print "Average Score = {0}".format(avg_score)


print "Average Positive Sentiment", results['positive']/7
print "Average Negative Sentiment", results['negative']/18
