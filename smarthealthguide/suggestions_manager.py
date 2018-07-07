
import entities
import json
import api_data_collector as api

'''
Place Types : 
Sleep Improvement 1
Food 2
Fitness 3
Water Intake 4

'''
place_types = [['matress store','meditation centre']]
suggested_places = []

def get_suggestions_list():
    suggestions_list =[]
    sg = entities.Suggestion()
    sg.name = "Sport and Health"
    sg.distance = 2
    sg.categories = 4
    suggestions_list.append(sg)

    sg = entities.Suggestion()
    sg.name = "Sleepwell Matress Store"
    sg.distance = 3
    sg.categories = 2
    suggestions_list.append(sg)

    json_list = json.dumps([ob.__dict__ for ob in suggestions_list])

    return json_list

def get_suggested_place_types(place):
    suggested_place_types = []
    return suggestedPlaceTypes


def get_suggested_places(placeCategoryId):
    place = entities.Place()
    for text_query in place_types[placeCategoryId - 1]:
        api_data = api.get_place_details(text_query)
        for result in api_data['results']:
            place.name = result['name']
            place.icon = result['icon']
            place.lat = result['geometry']['location']['lat']
            place.long = result['geometry']['location']['lng']
            suggested_places.append(place)





