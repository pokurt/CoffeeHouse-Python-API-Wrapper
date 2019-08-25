import coffeehouse

api_key = "<API KEY>"
api_client = coffeehouse.API(api_key)

session = api_client.create_session()
print("Session ID: {0}".format(session.id))
print("Session Available: {0}".format(str(session.available)))
print("Session Language: {0}".format(str(session.language)))
print("Session Expires: {0}".format(str(session.expires)))

while(True):
    output = session.think_thought(session.id, input("Input: "))
    print("Output: {0}".format(output))
