import credentials
import tweepy

consumer_key = credentials.TWITTER_CONSUMER_KEY
consumer_secret = credentials.TWITTER_CONSUMER_SECRET
access_token = credentials.TWITTER_ACCESS_TOKEN
access_token_secret = credentials.TWITTER_ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def authentication():
    try:
        redirect_url = auth.get_authorization_url()
        return redirect_url
    except tweepy.TweepError:
        print ('Error! Failed to get request token.')

# def sessiokn_set():
#     session.set('request_token', auth.request_token)


def authentication_final(user_verifier):
    # session.set('request_token', auth.request_token)
    global auth
    session =	{
        "request_token": auth.request_token,
    }


    # verifier = user_verifier
    # Let's say this is a web app, so we need to re-build the auth handler
    # first...
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    token = session["request_token"]
    # session.get('request_token')
    # session.delete('request_token')
    session.pop("request_token")
    auth.request_token = token

    try:
        ts = auth.get_access_token(user_verifier)
        token = ts[0]
        secret = ts[1]
        print(token)
        # print(auth.get_access_token(user_verifier))
        auth.set_access_token(token, secret)
        api = tweepy.API(auth)
        api.update_status('test tweet!') # test
    except tweepy.TweepError:
        print ('Error! Failed to get access token.')




def callsomething():
    public_tweets = api.home_timeline(count=5)
    s = ""
    for tweet in public_tweets:
        s += "{0} ".format(tweet.text)
        # print (tweet.text)
    return s


# if __name__ == '__main__':
#     pass
