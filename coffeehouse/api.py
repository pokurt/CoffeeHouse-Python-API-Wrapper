from coffeehouse.exception import CoffeeHouseError
from coffeehouse.session import Session
import json
import requests

class API(object):
    
    """
    Generic API Client for all API Features from the v2 API

    :param api_key: Your API Key
    :type api_key: str
    :param endpoint: The API Endpoint to make HTTP Requests to
    :type endpoint: str
    """
    def __init__(self, api_key, endpoint = "https://api.intellivoid.info/coffeehouse"):
        self.api_key = api_key
        self.endpoint = endpoint

    def create_session(self, language = "en"):
        request_payload = {
            "api_key": self.api_key,
            "language": language
        }

        response = requests.post("{0}/v2/CreateSession".format(self.endpoint), request_payload)
        if(response.status_code != 200):
                raise CoffeeHouseError(response.text, response.status_code)
        return Session(json.loads(response.text)["payload"])

    def get_session(self, session_id):
        request_payload = {
            "api_key": self.api_key,
            "session_id": session_id
        }

        response = requests.post("{0}/v2/GetSession".format(self.endpoint), request_payload)
        if(response.status_code != 200):
                raise CoffeeHouseError(response.text, response.status_code)
        return Session(json.loads(response.text)["payload"])

    def think_thought(self, session_id, input):
        request_payload = {
            "api_key": self.api_key,
            "session_id": session_id,
            "input": input
        }

        response = requests.post("{0}/v2/ThinkThought".format(self.endpoint), request_payload)
        if(response.status_code != 200):
                raise CoffeeHouseError(response.text, response.status_code)
        return json.loads(response.text)["payload"]["output"]