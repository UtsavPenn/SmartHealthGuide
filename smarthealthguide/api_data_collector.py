import json
import os
import requests


'''All external API calls '''

def get_request_data(url, headers=None):
    """This appears to be how the data is wrapped in the responses"""
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    return r.json()

def get_place_details(textquery):
    #placeid = get_palace_id(textquery)
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?key=AIzaSyD-3egv6QjDN_H-oGpqqCs7aMaCDf1OuB8&location=38.904513,-77.197910&radius=2000&query={}".format(textquery)
    return get_request_data(url)

def get_palace_id(textquery):
    url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?key=AIzaSyD-3egv6QjDN_H-oGpqqCs7aMaCDf1OuB8&input={}&inputtype=textquery&locationbias=ipbias".format(textquery)
    return get_request_data(url)['candidates'][0]['place_id']

def get_user_details(url):
    pass

def get_sleep_data(url):
    pass

def get_activity_data(url):
    pass

def get_heart_rate(url):
    pass

def get_place_distance(lat,lng):
    url = "https://maps.googleapis.com/maps/api/distancematrix/json?key=AIzaSyB5VWqn2rvzCE-5V5HEn_rJnd3xkfGj0YU&origins=38.904513,-77.197910&destinations={},{}".format(lat,lng)
    return get_request_data(url)

