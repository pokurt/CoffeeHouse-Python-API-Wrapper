class Session(object):

    def __init__(self, data, client):
        """
        AI Session Object
        """
        self._client = client
        self.id = data['session_id']
        self.language = data['language']
        self.available = data['available']
        self.expires = data['expires']

    def think_thought(self, text):
        """
        Processes user input and returns an AI text Response

        :type text: str
        :param text: The user input
        :raises: CoffeeHouseError
        :rtype: str
        """
        return self._client.think_thought(self.id, text)
