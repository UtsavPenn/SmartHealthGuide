import handler
import api_data_collector as api
import suggestions_manager as sug_man
import entities

def main():
    #handler.test_func()
    #place = entities.Place();
    #print(api.get_place_details("bars"))
    sug_man.get_suggested_places(0)
    #place.get_data("bars")


if __name__ == "__main__":
    main()