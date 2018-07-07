import json
import suggestions_manager;


def suggestions(event, context):
    body = {
        "message": suggestions_manager.get_suggestions_list(),
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


def test_func():
    sugg_list = []
    sugg_list = suggestions_manager.get_suggestions_list()
    print(sugg_list)
    return sugg_list





