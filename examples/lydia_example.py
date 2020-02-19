from coffeehouse.lydia import LydiaAI
from coffeehouse.api import API

# Create the CoffeeHouse API instance
api_key = "<API KEY>"
coffeehouse_api = API(api_key)

# Create Lydia instance
lydia = LydiaAI(coffeehouse_api)

# Create a new chat session (Like a conversation)
session = lydia.create_session()
print(f"Session ID: {session.id}")
print(f"Session Available: {session.available}")
print(f"Session Language: {session.language}")
print(f"Session Expires: {session.expires}")

# Talk to the bot!
while True:
    output = session.think_thought(input("Input: "))
    print(f"Output: {output}")

# In the case you want to save the Session ID to reuse the session
# Use lydia to invoke think_thought instead, for example;
#
# while True:
#     output = lydia.think_thought(session.id, input("Input: "))
#     print(f"Output: {output}")
#
# This is the same effect as above but uses the lydia instance directly