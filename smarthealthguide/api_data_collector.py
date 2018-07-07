import json
import os


'''All external API calls '''

def get_request_data(url, headers=None):
    """This appears to be how the data is wrapped in the responses"""
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    return r.json()['data']

def get_place_data(url):
    pass

def get_user_details(url):
    pass

def get_sleep_data(url):
    pass

def get_activity_data(url):
    pass

def get_heart_rate(url):
    pass
