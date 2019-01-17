# memebot
import tweepy as tp
import time
import os

consumer_key='k7i5wIty0UZQmuUY6G8WJhJo4'
consumer_secret='tJKntdgKgNJpITghvt69NZdsZz3MODQ6JCKj0fOw5kNV8BLr3E'
access_token='1039920275578531840-yJWybU8AQOEavp73BoEtWRLjctd9zu'
access_secret='ELsJJLLhZ8iZdPiqqZKblZ2AeHElLGzQ599Nrl1sFy4JV'

auth=tp.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)
api=tp.API(auth)
os.chdir('memes')
for meme_image in os.listdir(','):
    api.update_with_media(meme_image)
    time.sleep(100)