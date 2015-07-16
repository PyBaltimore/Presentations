### THIS REDDIT BOT WAS BUILT TO SCORE THE LIKELYHOOD OF SUCIDE ON /r/Depression subreddit AND RESPOND WITH APPROPRIATE HOTLINE INFORMATION

## Files:

1.  All files are located in alchemyapi folder

2.  All files must be run from alchemyapi folder in order to work

3.  general_sentiment file runs analysis on suicide notes

4.  suicide notes are located within subfolder the alchemyapi folder 

5.  reddit_sentiment_scoring file calculates /r/depression scores 

6.  app.py file returns scoring and sentiment for /r/depression

7.  data.csv file has to be created by user... it contains title, upvotes, sentiment, and score of each /r/depression posts

8.  api_key.txt - contains api key - visit alchemyapi website if you would like to request your own free api key.  The free key only allows 1000 requests per day.

9.  all other files in alchemyapi_python folder belong to alchemyapi library, ie LICENSE, example.py, README

## To Run a file for example app.py:
     python app.py <api key>
     note:  api_key is found in api_key.txt file

## Goals of project

1.  Reddit bot which reads new posts in depression subreddit 

2.  Analyze sentiment of posts

3.  Score the likelyhood of suicide

4.  Respond with appropriate suicide hotline information

## Add Later:

Provide community psychiatrist/psychologist resources based on poster's location
