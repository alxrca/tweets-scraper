# Tweets Scraper
Collect tweets and replies from a specific user, and export the data in a csv file. (Twitter API)

# Getting Started
## Install Tweepy
To scrape tweets from Twitter, I used [Tweepy](http://docs.tweepy.org/en/latest/getting_started.html), but there are several other options. 
To install tweepy:
  ```python
  pip install tweepy
  ```
## Get your Consumer Key and Consumer Secret
Then, you will have to go to [Twitter’s developer page](https://developer.twitter.com/en/apps) to create an app and register it. 
Fill all mandatory fields. After that, you should be redirected to a page where you can create your access token. Click on the “Create my access token” button. Copy and paste your Consumer Key and Consumer Secret in the code. Don't share them!
  ```python
  #Enter your consumer key and consumer secret codes
consumer_key = 'CONSUMER KEY'
consumer_secret = 'CONSUMER SECRET'
  ```
## Write the name of the profile you want to collect tweets from
Go to the Twitter profile of the person you'd like to collect tweets and replies from. Copy is username (you don't need the @), and paste it in the code.
  ```python
#Write the name of the profile you want to collect tweets from
user = 'USERNAME'
  ```
  
  ## And you're good to go!
