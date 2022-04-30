import urllib.request,json
from .models import Article, Category, Source , Headlines


# Getting api key
api_key = app.config['NEWS_API_KEY']