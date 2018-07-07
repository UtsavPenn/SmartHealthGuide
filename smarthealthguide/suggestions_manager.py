
import entities
import json

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

def get_suggested_place_types():
    suggested_place_types = []
    return suggestedPlaceTypes

def get_suggested_places():
    suggestedPlaces = []
    return suggestedPlaces

