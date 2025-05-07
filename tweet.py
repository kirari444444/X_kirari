import os
import tweepy

# 環境変数からAPIキーを読み込む
api_key = os.environ["API_KEY"]
api_secret = os.environ["API_SECRET"]
access_token = os.environ["ACCESS_TOKEN"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]

# 認証を設定
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# ツイート本文
tweet = "GitHub Actionsから自動ツイートしています！ #GitHubActions"

# ツイートを投稿
api.update_status(tweet)
