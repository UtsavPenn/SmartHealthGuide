import json


def suggestions(event, context):
    body = {
        "message": "Sport & Health located 2 miles away. Suggestion based on your activity data",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


def test_func():
    print("it works")






    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
