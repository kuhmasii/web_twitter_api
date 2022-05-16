from django.conf import settings
import tweepy


def get_apikeys():
    """function returns API keys from env."""
    api_key = settings.API_KEY
    api_secret_key = settings.API_SECRET_KEY

    return api_key, api_secret_key


def getaccess_token(request, apikey, apisecretkey, user_pin=None):
    """Function returns an endpoint that gets
       connected to the twitter's API App using 
       the  GET method and function uses token 
       to access the API using the POST method.
    """
    auth = tweepy.OAuth1UserHandler(apikey, apisecretkey, 'oob')

    if request.method == 'GET':
        api = auth.get_authorization_url()

    if request.method == 'POST':
        try:
            auth = auth.get_access_token(verifier=user_pin)
            api = tweepy.API(auth, wait_on_rate_limit=True)
        except tweepy.TweepyException:
            api = None
    return api
