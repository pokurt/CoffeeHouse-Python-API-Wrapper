# CoffeeHouse API Wrapper for Python

This is a very simple API Wrapper for the CoffeeHouse API. Using
This Library only supports the v2 API which is based from
this [Documentation](https://gist.github.com/Netkas/d3617e5b5b66c7851c728d3c0073529a)

<p align="center">
  <img src="https://i.imgur.com/N19XyN2.png" alt="CoffeeHouse Python Example">
</p>


## Installation
```sh
python3 setup.py build
python3 setup.py install
```

or
```sh
# cd into the coffeehouse directory
sudo -H python3 -m pip install .
```

## Usage

```python
import coffeehouse

api_key = "<API KEY>"  # Your key here - coffeehouse.intellivoid.info

# Initialise client
api_client = coffeehouse.API(api_key)
# Create session (like a conversation with the AI)
# Note that sessions expire 3 hours after creation (see example.py for more)
session = api_client.create_session()

while(True):
    # Get the output from the AI
    output = session.think_thought(session.id, input("Input: "))
    print("Output: {0}".format(output))
```
