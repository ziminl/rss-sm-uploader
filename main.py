







import feedparser
from instagrapi import Client
from facebook import GraphAPI
import tweepy



INSTAGRAM_USERNAME = 'your_instagram_username'
INSTAGRAM_PASSWORD = 'your_instagram_password'
FACEBOOK_ACCESS_TOKEN = 'your_facebook_access_token'

TWITTER_CONSUMER_KEY = 'your_twitter_consumer_key'
TWITTER_CONSUMER_SECRET = 'your_twitter_consumer_secret'
TWITTER_ACCESS_TOKEN = 'your_twitter_access_token'
TWITTER_ACCESS_TOKEN_SECRET = 'your_twitter_access_token_secret'

instagram_client = Client()
instagram_client.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
facebook_client = GraphAPI(access_token=FACEBOOK_ACCESS_TOKEN)






auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
twitter_client = tweepy.API(auth)
rss_url = 'https://www.assembly.go.kr/portal/rss/rss/meopenRss.do?brd_sctn=A1'
feed = feedparser.parse(rss_url)

for item in feed.entries:
    title = item.title
    link = item.link
    description = item.description
    instagram_client.photo_upload(description, 'image.jpg')
    facebook_client.put_object("me", "feed", message=title, link=link)
    tweet = f"{title}\n{link}"
    twitter_client.update_status(tweet)











