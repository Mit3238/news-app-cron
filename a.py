import requests

def get_data():
    return requests.get('https://apinews.mit3238.online/news-refresh').text

get_data()
