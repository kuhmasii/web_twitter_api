from django.shortcuts import redirect
import tweepy
import os

def get_apikeys():
    """function returns API keys from env."""
    api_key = os.environ.get('API_KEY')
    api_secret_key = os.environ.get("API_KEY_SECRET")

    return api_key, api_secret_key

def get_endpoint(apikey,apisecretkey):
    """Function returns an endpoint that gets
       connected to the twitter's API App
    """
    callback_url = 'oob'
    auth = tweepy.OAuth1UserHandler(apikey, apisecretkey, callback_url)
    redirect_url = auth.get_authorization_url()
    return redirect_url

def getaccess_token(userpin, apikey, apisecretkey, callback):
    """Function uses token to access the API """
    auth = tweepy.OAuth1UserHandler(apikey, apisecretkey)
    auth.get_access_token(userpin)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api