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
    def __init__(self, api_key,
                 endpoint="https://api.intellivoid.info/coffeehouse"):
        self.api_key = api_key
        self.endpoint = endpoint

    def create_session(self, language="en"):
        """
        Creates a new Session with the AI

        :type language: str
        :param language: The language that this session will be based in
        :raises: CoffeeHouseError
        :rtype: Session
        """
        request_payload = {
            "api_key": self.api_key,
            "language": language
        }

        response = requests.post("{0}/v2/CreateSession"
                                 .format(self.endpoint), request_payload)
        CoffeeHouseError.raise_for_status(response.status_code, response.text)
        return Session(json.loads(response.text)["payload"], self)

    def get_session(self, session_id):
        """
        Gets an existing session using a Session ID

        :type session_id: int
        :param session_id: The ID of the session to retrieve
        :raises: CoffeeHouseError
        :rtype: Session
        """
        request_payload = {
            "api_key": self.api_key,
            "session_id": session_id
        }

        response = requests.post("{0}/v2/GetSession".format(self.endpoint),
                                 request_payload)
        CoffeeHouseError.raise_for_status(response.status_code, response.text)
        return Session(json.loads(response.text)["payload"], self)

    def think_thought(self, session_id, text):
        """
        Processes user input and returns an AI text Response

        :type text: str
        :param text: The user input
        :raises: CoffeeHouseError
        :rtype: str
        """
        request_payload = {
            "api_key": self.api_key,
            "session_id": session_id,
            "input": input
        }

        response = requests.post("{0}/v2/ThinkThought".format(self.endpoint),
                                 request_payload)
        CoffeeHouseError.raise_for_status(response.status_code, response.text)
        return json.loads(response.text)["payload"]["output"]
