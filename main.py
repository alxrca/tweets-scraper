import tweepy, sys, json, csv, pandas as pd

#Enter your consumer key and consumer secret codes
consumer_key = 'CONSUMER KEY'
consumer_secret = 'CONSUMER SECRET' 

auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)

api = tweepy.API(auth)

#Write the name of the profile you want to collect tweets from
user = 'USERNAME'

#Collect all tweets & replies from the account
data = pd.DataFrame(columns=['User', 'Text', 'ID', 'Retweets', 'Favorites', 'Dates'])
for pages in tweepy.Cursor(api.user_timeline, id=user, count=200).pages():   
    for tweet in pages:  
        #To collect more information, check parameters names in json response 
        #https://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline   
        #and add tweet._json["parameter_name"]
        text = tweet._json["text"].strip()
        textid = 'https://twitter.com/' + user + '/status/' + tweet._json["id_str"]
        retweets = tweet._json["retweet_count"]
        favorites = tweet._json["favorite_count"]
        date = tweet._json["created_at"]
        new_row = {'User': user, 'Text': text, 'ID': textid, 'Retweets': 'retweets', 'Favorites': favorites, 'Dates': date}
        data= data.append(new_row, ignore_index=True, sort = False)
print(data)

#Export collected data to csv
data.to_csv('data.csv',index=False)
