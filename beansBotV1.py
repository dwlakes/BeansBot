from logging import ERROR, error

import requests
from tweepy.errors import TweepyException
import beansBotConfig
import tweepy
import time
import random
from datetime import datetime

count = 0
i = 0

# searches tweets to like and retweet

# searches for internet connection before it needs internet


def test_connection():
    url = "http://www.kite.com"
    timeout = 5
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    try:
        request = requests.get(url, timeout=timeout)
    except:
        print("trying to connect to internet", current_time)
        time.sleep(30)
        test_connection()


def searchTweets(client, query):
    response = None
    test_connection()
    try:
        # web scapes and loads query in list for retweets
        response = client.search_recent_tweets(query=query, max_results=10, tweet_fields=[
            'created_at', 'lang'], expansions=['author_id'])
        print("got tweets")
    except:
        print("trying to load tweets")
        time.sleep(10)
        # incase missing internet connection, the function will be called until internet is reestablished
        searchTweets(client, query)

    time.sleep(5)
    return response

# replies to mention


def replyToMention(client, mentions, replied):
    print("attempting to reply to mention")

    # makes tweets for navy keyword
    navyFile = open(
        '/Users/dwlakes/Desktop/bots/beansBot/navyBeanTweets.txt', 'r')
    navyTxt = navyFile.readlines()
    navyList = []
    for line in navyTxt:

        if not line.strip():
            continue
        if line[-1] == '\n':
            navyList.append(line[:-1])
        else:
            navyList.append(line)

    # makes tweets for fava keyword
    favaFile = open(
        '/Users/dwlakes/Desktop/bots/beansBot/favaBeanTweets.txt', 'r')
    favaTxt = favaFile.readlines()
    favaList = []
    for line in favaTxt:

        if not line.strip():
            continue
        if line[-1] == '\n':
            favaList.append(line[:-1])
        else:
            favaList.append(line)

    # makes tweets for lima keyword
    limaFile = open(
        '/Users/dwlakes/Desktop/bots/beansBot/limaBeanTweets.txt', 'r')
    limaTxt = limaFile.readlines()
    limaList = []
    for line in limaTxt:

        if not line.strip():
            continue
        if line[-1] == '\n':
            limaList.append(line[:-1])
        else:
            limaList.append(line)

    # makes tweets for coffee keyword
    coffeeFile = open(
        '/Users/dwlakes/Desktop/bots/beansBot/coffeeBeanTweets.txt', 'r')
    coffeeTxt = coffeeFile.readlines()
    coffeeList = []
    for line in coffeeTxt:

        if not line.strip():
            continue
        if line[-1] == '\n':
            coffeeList.append(line[:-1])
        else:
            coffeeList.append(line)

    # makes tweets for black keyword
    blackFile = open(
        '/Users/dwlakes/Desktop/bots/beansBot/blackBeanTweets.txt', 'r')
    blackTxt = blackFile.readlines()
    blackList = []
    for line in blackTxt:

        if not line.strip():
            continue
        if line[-1] == '\n':
            blackList.append(line[:-1])
        else:
            blackList.append(line)

    # makes tweets for frijoles keyword
    frijolesFile = open(
        '/Users/dwlakes/Desktop/bots/beansBot/frijolesTweets.txt', 'r')
    frijolesTxt = frijolesFile.readlines()
    frijolesList = []
    for line in frijolesTxt:

        if not line.strip():
            continue
        if line[-1] == '\n':
            frijolesList.append(line[:-1])
        else:
            frijolesList.append(line)

    # makes tweets for pinto keyword
    pintoFile = open(
        '/Users/dwlakes/Desktop/bots/beansBot/pintoBeanTweets.txt', 'r')
    pintoTxt = pintoFile.readlines()
    pintoList = []
    for line in pintoTxt:

        if not line.strip():
            continue
        if line[-1] == '\n':
            pintoList.append(line[:-1])
        else:
            pintoList.append(line)

    # makes tweets for refried keyword
    refriedFile = open(
        '/Users/dwlakes/Desktop/bots/beansBot/refriedBeanTweets.txt', 'r')
    refriedTxt = refriedFile.readlines()
    refriedList = []
    for line in refriedTxt:

        if not line.strip():
            continue
        if line[-1] == '\n':
            refriedList.append(line[:-1])
        else:
            refriedList.append(line)

    # makes tweets for baked keyword
    bakedFile = open(
        '/Users/dwlakes/Desktop/bots/beansBot/bakedBeanTweets.txt', 'r')
    bakedTxt = bakedFile.readlines()
    bakedList = []
    for line in bakedTxt:

        if not line.strip():
            continue
        if line[-1] == '\n':
            bakedList.append(line[:-1])
        else:
            bakedList.append(line)

    for tweet in mentions.data:
        # converts each tweet to lowercase to search for keywords
        tweetToLower = str(tweet)
        test_connection()
        try:
            # makes sure the replies haven't alreaedy been replied to
            if tweet.id not in replied:
                # searches for keywords in mentions tweets
                if (tweetToLower.lower().find('navy') != -1
                    or tweetToLower.lower().find('navy bean') != -1
                    or tweetToLower.lower().find('navy beans') != -1
                    or tweetToLower.lower().find('navybean') != -1
                        or tweetToLower.lower().find('navybeans') != -1):
                    client.like(tweet.id, user_auth=True)
                    client.create_tweet(in_reply_to_tweet_id=tweet.id,
                                        text=random.choice(navyList), user_auth=True)
                    print("responded to navy tweet")
                elif (tweetToLower.lower().find('fava') != -1
                        or tweetToLower.lower().find('fava bean') != -1
                        or tweetToLower.lower().find('fava beans') != -1
                        or tweetToLower.lower().find('favabean') != -1
                        or tweetToLower.lower().find('favabeans') != -1):
                    client.like(tweet.id, user_auth=True)
                    client.create_tweet(in_reply_to_tweet_id=tweet.id,
                                        text=random.choice(favaList), user_auth=True)
                    print("responded to fava tweet")
                elif (tweetToLower.lower().find('lima') != -1
                        or tweetToLower.lower().find('lima bean') != -1
                        or tweetToLower.lower().find('lima beans') != -1
                        or tweetToLower.lower().find('limabean') != -1
                        or tweetToLower.lower().find('limabeans') != -1):
                    client.like(tweet.id, user_auth=True)
                    client.create_tweet(in_reply_to_tweet_id=tweet.id,
                                        text=random.choice(limaList), user_auth=True)
                    print("responded to lima tweet")
                elif (tweetToLower.lower().find('coffee') != -1
                        or tweetToLower.lower().find('coffee bean') != -1
                        or tweetToLower.lower().find('coffee beans') != -1
                        or tweetToLower.lower().find('coffeebean') != -1
                        or tweetToLower.lower().find('coffeebeans') != -1):
                    client.like(tweet.id, user_auth=True)
                    client.create_tweet(in_reply_to_tweet_id=tweet.id,
                                        text=random.choice(coffeeList), user_auth=True)
                    print("responded to coffee tweet")
                elif (tweetToLower.lower().find('black') != -1
                        or tweetToLower.lower().find('black bean') != -1
                        or tweetToLower.lower().find('black beans') != -1
                        or tweetToLower.lower().find('blackbean') != -1
                        or tweetToLower.lower().find('blackbeans') != -1):
                    client.like(tweet.id, user_auth=True)
                    client.create_tweet(in_reply_to_tweet_id=tweet.id,
                                        text=random.choice(blackList), user_auth=True)
                    print("responded to black tweet")
                elif (tweetToLower.lower().find('frijol') != -1
                        or tweetToLower.lower().find('frijoles') != -1):
                    client.like(tweet.id, user_auth=True)
                    client.create_tweet(in_reply_to_tweet_id=tweet.id,
                                        text=random.choice(frijolesList), user_auth=True)
                    print("responded to frijol tweet")
                elif (tweetToLower.lower().find('pinto') != -1
                        or tweetToLower.lower().find('pinto bean') != -1
                        or tweetToLower.lower().find('pinto beans') != -1
                        or tweetToLower.lower().find('pintobean') != -1
                        or tweetToLower.lower().find('pintobeans') != -1):
                    client.like(tweet.id, user_auth=True)
                    client.create_tweet(in_reply_to_tweet_id=tweet.id,
                                        text=random.choice(pintoList), user_auth=True)
                    print("responded to pinto tweet")
                elif (tweetToLower.lower().find('refried') != -1
                        or tweetToLower.lower().find('refried bean') != -1
                        or tweetToLower.lower().find('refried beans') != -1
                        or tweetToLower.lower().find('refriedbean') != -1
                        or tweetToLower.lower().find('refriedbeans') != -1):
                    client.like(tweet.id, user_auth=True)
                    client.create_tweet(in_reply_to_tweet_id=tweet.id,
                                        text=random.choice(refriedList), user_auth=True)
                    print("responded to refried tweet")
                elif (tweetToLower.lower().find('baked') != -1
                        or tweetToLower.lower().find('baked bean') != -1
                        or tweetToLower.lower().find('baked beans') != -1
                        or tweetToLower.lower().find('bakedbean') != -1
                        or tweetToLower.lower().find('bakedbeans') != -1):
                    client.like(tweet.id, user_auth=True)
                    client.create_tweet(in_reply_to_tweet_id=tweet.id,
                                        text=random.choice(bakedList), user_auth=True)
                    print("responded to baked tweet")
                 # if tweet doesn't contain a keyword, reply the following
                else:
                    client.create_tweet(in_reply_to_tweet_id=tweet.id, exclude_reply_user_ids="1489347220222611456",
                                        text="Beep bop you've summoned the beans bot. My keywords are: fava bean, navy bean, lima bean, coffee bean, black bean, frijoles, pinto beans, refried beans, baked beans. Mention me with one of those words to learn a poorly sourced fact about that bean.", user_auth=True)
                    print("responded to general tweet")
            # adds replies to avoid tweeting to a reply more than once
            replied.append(tweet.id)
        except Exception as e:
            print("tried to respond to mention")
            print(e)
        time.sleep(10)


def likeAndRetweet(tweets):
    for tweet in tweets.data:
        tweetToLower = str(tweet)
        test_connection()
        try:
            client.like(tweet.id, user_auth=True)
            # print(tweet.id)
            # client.retweet(tweet.id, user_auth=True)
            if (tweetToLower.lower().find('baked beans') != -1):
                client.create_tweet(in_reply_to_tweet_id=tweet.id,
                                    text="Hey! Did you know that there are approximately 465 beans in a standard 415gm can of Heinz beans? Tweet at me to start a conversation!")
            if (tweetToLower.lower().find('refried beans') != -1):
                client.create_tweet(in_reply_to_tweet_id=tweet.id,
                                    text="Hey! Did you know that refried beans are only fried once? The reason for this misconception is a translation error. The originals are frijoles refritos which actually means “well fried beans” - not re-fried. Tweet at me to start a conversation!")
            if (tweetToLower.lower().find('pinto bean') != -1
                    or tweetToLower.lower().find('pinto beans') != -1):
                client.create_tweet(in_reply_to_tweet_id=tweet.id,
                                    text="Hey! Did you know that the pinto bean was cultivated by early Mexican and Peruvian civilizations more than 5,000 years ago? Tweet at me to start a conversation!")
            if (tweetToLower.lower().find('frijol') != -1
                    or tweetToLower.lower().find('frijoles') != -1):
                client.create_tweet(in_reply_to_tweet_id=tweet.id,
                                    text="Hola! ¿Sabes que hay 150 especies de plantas de frijol en el mundo? Enviame un tweet para hacer una conversación!")
            if (tweetToLower.lower().find('black bean') != -1
                    or tweetToLower.lower().find('black beans') != -1):
                client.create_tweet(in_reply_to_tweet_id=tweet.id,
                                    text="Hey! Did you know that black beans are actually more of a dark blue color? Tweet at me to start a conversation!")
            if (tweetToLower.lower().find('coffee bean') != -1
                    or tweetToLower.lower().find('coffee beans') != -1):
                client.create_tweet(in_reply_to_tweet_id=tweet.id,
                                    text="Hey! Did you know that coffee beans are actually seeds and that Brazil grows the most coffee in the world? Tweet at me to start a conversation!")
            if (tweetToLower.lower().find('lima bean') != -1
                    or tweetToLower.lower().find('lima beans') != -1):
                client.create_tweet(in_reply_to_tweet_id=tweet.id,
                                    text='Hey! Did you know when the lima bean became popular in North America and Europe, it was often transported from South America in boxes marked with "Lima, Peru", to inform recipients on the origin of food and that\'s its name comes from? Tweet at me to start a conversation!')
            if (tweetToLower.lower().find('fava bean') != -1
                    or tweetToLower.lower().find('fav beans') != -1):
                client.create_tweet(in_reply_to_tweet_id=tweet.id,
                                    text='Hey! Did you know the Orphics believed that Pythagoras had forbidden the eating of favas because they contain the souls of the dead? Tweet at me to start a conversation!')
            if (tweetToLower.lower().find('navy bean') != -1
                    or tweetToLower.lower().find('navy beans') != -1):
                client.create_tweet(in_reply_to_tweet_id=tweet.id,
                                    text='Hey! Did you know the navy bean is the official Bean of Massachusetts, the Baked Bean State? Tweet at me to start a conversation!')
            if (tweetToLower.lower().find('beans on toast') != -1):
                client.create_tweet(in_reply_to_tweet_id=tweet.id,
                                    text='Would you mind telling me the ingredients for beans on toast? I seem to have lost my copy. Tweet at me to start a conversation!')

            print("liked and retweeted")
            time.sleep(5)
        except:
            # else:
            print("trying to like and retweet")

            time.sleep(10)


def sendTweet(count):
    print(count)
    test_connection()
    try:
        client.create_tweet(text=newList[count])
        print("sent tweet number", count)
        time.sleep(10)
    # catches the tweet if laptop doesn't have internet connection and keeps trying
    except:
        print("trying to create tweet")
        time.sleep(10)
        # incase no internet connection, the function will be called until there is a connection
        sendTweet(count)
    return count


# creates new query for retweets
query = 'baked beans -is:retweet OR refried beans -is:retweet OR pinto bean -is:retweet OR pinto beans -is:retweet OR frijol -is:retweet OR frijoles -is:retweet OR black bean -is:retweet OR coffee bean -is:retweet OR coffee beans -is:retweet OR black beans -is:retweet OR lima bean -is:retweet OR lima bean -is:retweet OR fava bean -is:retweet OR fava beans -is:retweet OR navy beans -is:retweet OR beans on toast -is:retweet'


# an array to keep track of tweets that have already been replied to
replied = []
file = open('/Users/dwlakes/Desktop/bots/beansBot/beansBotTweets.txt', 'r')
f = file.readlines()
newList = []


for line in f:

    if not line.strip():
        continue
    if line[-1] == '\n':
        print("reached end")
        newList.append(line[:-1])
    else:
        newList.append(line)

    retweetCounter = 0
    # while loop looks for tweets to like and retweet
    while retweetCounter < 3:
        mentionReplyCounter = 0
        # while loop looks for mentions to reply to
        while mentionReplyCounter < 450:
            test_connection()
            client = tweepy.Client(bearer_token=beansBotConfig.BEARER_TOKEN,
                                   wait_on_rate_limit=True)
            # gets all the mentions
            test_connection()
            mentions = client.get_users_mentions(
                beansBotConfig.USERID, tweet_fields=['lang'])
            test_connection()
            client = tweepy.Client(consumer_key=beansBotConfig.CONSUMER_KEY,
                                   consumer_secret=beansBotConfig.CONSUMER_SECRET,
                                   access_token=beansBotConfig.ACCESS_KEY,
                                   access_token_secret=beansBotConfig.ACCESS_SECRET,
                                   wait_on_rate_limit=True)
            print("mention coutner: " + str(mentionReplyCounter))
            mentionReplyCounter += 1
            replyToMention(client, mentions, replied)

        test_connection()
        client = tweepy.Client(
            bearer_token=beansBotConfig.BEARER_TOKEN, wait_on_rate_limit=True)
        tweets = searchTweets(client, query)
        test_connection()
        client = tweepy.Client(consumer_key=beansBotConfig.CONSUMER_KEY,
                               consumer_secret=beansBotConfig.CONSUMER_SECRET,
                               access_token=beansBotConfig.ACCESS_KEY,
                               access_token_secret=beansBotConfig.ACCESS_SECRET,
                               wait_on_rate_limit=True)
        likeAndRetweet(tweets)
        # time.sleep(7200)
        time.sleep(10)
        #i += 1
        print("retweet coutner: " + str(retweetCounter))
        retweetCounter += 1

    sendTweet(count)
    count += 1

    time.sleep(5)
    # time.sleep(14400)

print("finished list")
