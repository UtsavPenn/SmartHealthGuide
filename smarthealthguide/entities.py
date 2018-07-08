
import api_data_collector as api

class SensorData:
    sleep = None
    activity = None
    heart_rate = None

    def get_data(self):
        pass


class UserData:
    weight = None
    height = None
    age = None
    gender = None

    def get_data(self):
        pass


class Suggestion:
    name = None
    type = None
    distance = None
    categories = None
    discount = None
    icon = None

    def get_data(self):
        pass


class Place:
    lat = None
    long = None
    name = None
    icon = None


    def get_data(self,textquery):
        api_data = api.get_place_details(textquery)
        self.name = api_data['result']['name']
        self.long = api_data['result']['geometry']['location']['lng']
        self.lat = api_data['result']['geometry']['location']['lat']
        self.icon = api_data['result']['icon']
        print(self.name)
        return api_data
