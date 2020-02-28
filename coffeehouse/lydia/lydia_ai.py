from coffeehouse.exception import CoffeeHouseError
from coffeehouse.lydia.session import Session
from coffeehouse.api import API

import json
import requests


class LydiaAI(API):
    def __init__(self, *args, **kwargs):
        """
        Public constructor for Lydia
        :param access_key:
        :param endpoint:
        """

        super().__init__(*args, **kwargs)

    def create_session(self, language="en"):
        """
        Creates a new Session with the AI

        :type language: str
        :param language: The language that this session will be based in
        :raises: CoffeeHouseError
        :returns: The newly created session
        :rtype: Session
        """

        return Session(self._send("v1/lydia/session/create",
                                  target_language=language), self)

    def get_session(self, session_id):
        """
        Gets an existing session using a Session ID

        :type session_id: int
        :param session_id: The ID of the session to retrieve
        :raises: CoffeeHouseError
        :returns: The already existing session
        :rtype: Session
        """

        return Session(self._send("v1/lydia/session/get",
                                  session_id=session_id), self)

    def think_thought(self, session_id, text):
        """
        Processes user input and returns an AI text Response

        :param session_id:
        :type text: str
        :param text: The user input
        :raises: CoffeeHouseError
        :returns: The json payload of the response
        :rtype: str
        """
        
        return self._send("v1/lydia/session/think",
                          session_id=session_id,
                          input=text)["payload"]["output"]
