class API(object):

    def __init__(self, access_key, endpoint="https://api.intellivoid.info/coffeehouse"):
        """
        Public constructor for CoffeeHouse API

        :param access_key:
        :param endpoint:
        :return:
        """
        if isinstance(access_key, API):
            self.access_key = access_key.access_key
            self.endpoint = access_key.endpoint
        else:
            self.access_key = access_key
            self.endpoint = endpoint

    def _send(self, path, payload):
        response = requests.post("{}/{}".format(self.endpoint, path), payload)
        return CoffeeHouseError.parse_and_raise(response.status_code, response.text)
