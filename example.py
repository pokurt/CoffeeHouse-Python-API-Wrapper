import coffeehouse

api_key = "<API KEY>"
api_client = coffeehouse.API(api_key)

session = api_client.create_session()
print("Session ID: {0}".format(session.id))
print("Session Available: {0}".format(str(session.available)))
print("Session Language: {0}".format(str(session.language)))
print("Session Expires: {0}".format(str(session.expires)))

while(True):
    output = session.think_thought(input("Input: "))
    print("Output: {0}".format(output))


## In the case you want to save the Session ID to reuse the session
## Use api_client to invoke think_thought instead, for example;
##
## while(True):
##     output = api_client.think_thought(session.id, input("Input: "))
##     print("Output: {0}".format(output))
##
## This is the same effect as above but uses the client directly.
