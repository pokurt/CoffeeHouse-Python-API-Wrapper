from coffeehouse.exception import coffeehouse_error
from coffeehouse.session import session
import json
import requests

class api(object):
    
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
        """
        Creates a new Session with the AI

        :type self:
        :param self:
        :type language:
        :param language: The language that this session will be based in
        :raises:
        :rtype:
        """
        request_payload = {
            "api_key": self.api_key,
            "language": language
        }

        response = requests.post("{0}/v2/CreateSession".format(self.endpoint), request_payload)
        if(response.status_code != 200):
                raise coffeehouse_error(response.text, response.status_code)
        return session(json.loads(response.text)["payload"])

    def get_session(self, session_id):
    
        """
        Gets an existing session using a SessionID

        :type self:
        :param self:
        :type session_id:
        :param session_id: The ID of the session to retrieve
        :raises: CoffeeHouseError
        :rtype: Session
        """
        request_payload = {
            "api_key": self.api_key,
            "session_id": session_id
        }

        response = requests.post("{0}/v2/GetSession".format(self.endpoint), request_payload)
        if(response.status_code != 200):
                raise coffeehouse_error(response.text, response.status_code)
        return session(json.loads(response.text)["payload"])

    def think_thought(self, session_id, input):
    
        """ 
        Processes user input and returns an AI text Response

        :type self:
        :param self:
        :type session_id:
        :param session_id: The ID of the session to get an output from
        :type input:
        :param input: The user input
        :raises: CoffeeHouseError
        :rtype: str
        """
        request_payload = {
            "api_key": self.api_key,
            "session_id": session_id,
            "input": input
        }

        response = requests.post("{0}/v2/ThinkThought".format(self.endpoint), request_payload)
        if(response.status_code != 200):
                raise coffeehouse_error(response.text, response.status_code)
        return json.loads(response.text)["payload"]["output"]