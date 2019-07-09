class Session(object):

    def __init__(self, data):
        self.id = data['session_id']
        self.language = data['language']
        self.available = data['available']
        self.expires = data['expires']