#%%
import tweepy
import csv
import pandas as pd
import json

consumer_key = "FZmC6ZsaQr9NiR2aEd8UU5R3q"
consumer_secret = "yBuspMruGaO290JkOpWE8w74lKCAggcuiFjhZXWKA7DVleYrfP"
access_token = "878359622670622720-erNskBKsT7eQBSJEm6dcVyrXc2Eg10b"
access_token_secret = "k7W00oNbxIzQRZyL1aTUcqSOJqAW7wqsjli1RMCipHzoT"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

#csvFile = open('data3.csv', 'a')
#csvWriter = csv.writer(csvFile)

file = open("DataTwitter.txt",'w')
file_full = open("DataTwitterComplete.txt",'w')

def get_tweets(query, jumlah):

    for tweet in tweepy.Cursor(api.search, tweet_mode='extended',q=query).items(jumlah):
        print(tweet.full_text)
        file.write(json.dumps(tweet.full_text)+"\n")
        #csvWriter.writerow([tweet.full_text.encode('utf-8')])
        file_full.write(json.dumps(tweet._json)+"\n")
        
    
queries = ['#CapresO1Bohong','#JokowiBohongLagi','#2019GantiPresiden']
jumlah = [30,35,35]

for i in range(len(queries)):
    get_tweets(queries[i],jumlah[i])

file.close()

#%%
tweets_filename = 'DataTwitter.txt'
tweets_file = open(tweets_filename, "r")

tweets_data = []
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

tweets = pd.DataFrame(tweets_data)
