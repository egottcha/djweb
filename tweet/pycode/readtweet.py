import time


def getTweets(screen_name, tweet_number):
    tweets = []

    from tweet.pycode import auth
    consumer_key = auth.consumer_key
    consumer_secret = auth.consumer_secret
    access_token_key = auth.access_token_key
    access_token_secret = auth.access_token_secret

    try:
        import twitter
        api = twitter.Api(consumer_key=consumer_key,
                          consumer_secret=consumer_secret,
                          access_token_key=access_token_key,
                          access_token_secret=access_token_secret)
        latest = api.GetUserTimeline(screen_name=screen_name, count=tweet_number)
        for tweet in latest:
            if tweet.retweeted_status:
                status = tweet.retweeted_status.text
                user = tweet.retweeted_status.user.screen_name
                head = tweet.user.screen_name + ' Retweeted'
                for url in tweet.retweeted_status.urls:
                    link = url.url
            else:
                status = tweet.text
                user = tweet.user.screen_name
                head = 'Tweet'
                for url in tweet.urls:
                    link = url.url
            tweet_date = time.strftime('%Y-%m-%d %H:%M:%S',
                                       time.strptime(tweet.created_at, '%a %b %d %H:%M:%S +0000 %Y'))
            tweets.append({'user': user, 'status': status, 'date': tweet_date, 'head': head, 'url': link})
    except:
        tweets.append(
            {'user': 'dummy', 'status': 'Something is not quite right', 'date': 'Less than a minute ago', 'head': '?',
             'url': '#'})
    return {'tweets': tweets}
