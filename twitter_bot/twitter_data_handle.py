import credentials
import tweepy

consumer_key = credentials.TWITTER_CONSUMER_KEY
consumer_secret = credentials.TWITTER_CONSUMER_SECRET
access_token = credentials.TWITTER_ACCESS_TOKEN
access_token_secret = credentials.TWITTER_ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



def callsomething():
    public_tweets = api.home_timeline(count=5)
    s = ""
    for tweet in public_tweets:
        s += "{0} ".format(tweet.text)
        # print (tweet.text)
    return s


# if __name__ == '__main__':
#     pass
