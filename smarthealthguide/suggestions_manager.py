
import entities
import json
import api_data_collector as api
import commons
from math import sin, cos, sqrt
import random
import fitbit_data


'''
Place Types : 
Sleep Improvement 1
Food 2
Fitness 3
Water Intake 4

'''
place_types = [['sleep therapy'],['meal plan service'],['sport and health']]
suggested_place_types = []
suggested_places = []
user_details = entities.UserData()
sensor_data = entities.SensorData()
user_lat = 38.882066
user_long = -76.994269



def get_suggestions_list():
    suggestions_list =[]
    sg = entities.Suggestion()

    suggested_place_types_set = get_suggested_place_types()
    print(len(suggested_place_types_set))

    for suggested_place_type in suggested_place_types_set:
        get_suggested_places_by_category(suggested_place_type)

    for suggested_place in suggested_places:
        sg = entities.Suggestion()
        sg.name = suggested_place.name
        sg.icon = suggested_place.icon

        sg.distance = str(calculate_dist(suggested_place.lat, suggested_place.long))
        sg.discount = random.randint(1,10)*5
        sg.metric = suggested_place.metric
        suggestions_list.append(sg)

    suggestions_list.append(sg)
    print(len(suggestions_list))
    json_list = json.dumps([ob.__dict__ for ob in suggestions_list])
    print(json_list)
    return json_list

def calculate_dist(lat, lng):
    api_data = api.get_place_distance(lat, lng)
    distance = float(api_data['rows'][0]['elements'][0]['distance']['value'])/1600
    distance = round(distance,2)
    return distance

def get_user_details(fitbitdata):
    user_details.age = fitbitdata[0]
    user_details.height = fitbitdata[1]
    user_details.weight = fitbitdata[2]
    '''
    user_details.age = 28
    user_details.height = 65
    user_details.weight = 190
    '''

def get_average_sensor_data(fitbitdata):
    '''
    sensor_data.activity = 2200
    sensor_data.sleep = 11
    sensor_data.heart_rate = 70
    '''
    sensor_data.activity = fitbitdata[5]
    sensor_data.sleep = fitbitdata[4]
    sensor_data.heart_rate = fitbitdata[3]


def get_suggested_place_types():
    #fitbitdata = [0] * 7
    fitbitdata = fitbit_data.get_fit_bit_data()
    print ("Prinoting data from fitbtweb api")
    print(fitbitdata)

    get_user_details(fitbitdata)
    get_average_sensor_data(fitbitdata)
    sleep_score = commons.sleep_score(user_details.age, sensor_data.sleep)

    weight_score = commons.weight_score(user_details.weight,user_details.height)
    calorie_score = commons.calorie_score(user_details.age, sensor_data.activity)
    heart_rate_score = commons.heart_rate_score(sensor_data.heart_rate)

    '''By default add fitness recommendation to all users'''
    #suggested_place_types.append(3)

    if weight_score == 3:
        suggested_place_types.append(2)
        suggested_place_types.append(3)
        suggested_place_types.append(4)

    if calorie_score == 3:
        suggested_place_types.append(3)

    if sleep_score == 3:
        suggested_place_types.append(1)

    if heart_rate_score == 2:
        suggested_place_types.append(3)

    suggested_place_types_set = list(set(suggested_place_types))


    print(len(suggested_place_types_set))
    return suggested_place_types_set


def get_suggested_places_by_category(sugg_recom_cat):
    if sugg_recom_cat == 4:
        print("utsav")
        place = entities.Place()
        place.name = "AquaSana"
        place.icon = "https://visualpharm.com/assets/472/Water-595b40b65ba036ed117d2756.svg"
        place.lat = "38.88"
        place.long = "-76.99"
        place.metric = 3
        suggested_places.append(place)
        return

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

