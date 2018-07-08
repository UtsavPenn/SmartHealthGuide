
import entities
import json
import api_data_collector as api
import commons
from math import sin, cos, sqrt
import random
#import fitbit_data


'''
Place Types : 
Sleep Improvement 1
Food 2
Fitness 3
Water Intake 4

'''
place_types = [['matress store','meditation centre'],[],['gym'],[]]
suggested_place_types = []
suggested_places = []
user_details = entities.UserData()
sensor_data = entities.SensorData()
user_lat = 38.882066
user_long = -76.994269
fitbitdata = []


def get_suggestions_list():
    suggestions_list =[]
    sg = entities.Suggestion()
    #fitbitdata = fitbit_data.get_fit_bit_data()

    suggested_place_types_set = get_suggested_place_types()


    for suggested_place_type in suggested_place_types_set:
        get_suggested_places_by_category(suggested_place_type)

    for suggested_place in suggested_places:
        sg = entities.Suggestion()
        sg.name = suggested_place.name
        sg.icon = suggested_place.icon

	sg.distance = str(round((float(api.get_place_distance(suggested_place.lat + "," + suggested_place.long))/1.6),2))
        sg.discount = random.randint(1,10)*5
        sg.metric = suggested_place.metric
        suggestions_list.append(sg)

    suggestions_list.append(sg)
    print(len(suggestions_list))
    json_list = json.dumps([ob.__dict__ for ob in suggestions_list])
    print(json_list)
    return json_list

def calculate_dist(user_lat, user_lng, lat, lng):
    dlon = lng - user_lng
    dlat = lat - user_lat

    a = sin(dlat / 2) ** 2 + cos(user_lat) * cos(lat) * sin(dlon / 2) ** 2
    c = 2 * a*sin(sqrt(a))

    distance = 3956.0 * c
    return distance

def get_user_details():
    user_details.age = 28
    user_details.height = 65
    user_details.weight = 160
    '''
    user_details.age = fitbitdata['age']
    user_details.height = fitbitdata['height']
    user_details.weight = fitbitdata['weight']
    '''

def get_average_sensor_data():
    sensor_data.activity = 2000
    sensor_data.sleep = 8
    sensor_data.heart_rate = 70
    '''
    sensor_data.activity = fitbitdata['calories']
    sensor_data.sleep = fitbitdata['sleepHrs']
    sensor_data.heart_rate = fitbitdata['heartRate']
    '''

def get_suggested_place_types():
    get_user_details()
    get_average_sensor_data()
    sleep_score = commons.sleep_score(user_details.age, sensor_data.sleep)

    weight_score = commons.weight_score(user_details.weight,user_details.height)
    calorie_score = commons.calorie_score(user_details.age, sensor_data.activity)
    heart_rate_score = commons.heart_rate_score(sensor_data.heart_rate)

    '''By default add fitness recommendation to all users'''
    suggested_place_types.append(3)

    if weight_score == 3:
        suggested_place_types.append(1)
        suggested_place_types.append(2)
        suggested_place_types.append(4)

    if calorie_score == 3:
        suggested_place_types.append(3)

    if sleep_score == 3:
        suggested_place_types.append(1)

    if heart_rate_score == 2:
        suggested_place_types.append(2)

    suggested_place_types_set = list(set(suggested_place_types))
    print(sensor_data.activity)
    print(len(suggested_place_types_set))
    return suggested_place_types_set


def get_suggested_places_by_category(sugg_recom_cat):
    for text_query in place_types[sugg_recom_cat - 1]:
        api_data = api.get_place_details(text_query)
        for result in api_data['results']:
            place = entities.Place()
            place.name = result['name']
            place.icon = result['icon']
            place.lat = result['geometry']['location']['lat']
            place.long = result['geometry']['location']['lng']
            place.metric = sugg_recom_cat - 1
            suggested_places.append(place)




'''
sg.name = "Sport and Health"
    sg.distance = 2
    sg.categories = 4
    suggestions_list.append(sg)

    sg = entities.Suggestion()
    sg.name = "Sleepwell Matress Store"
    sg.distance = 3
    sg.categories = 2
'''

