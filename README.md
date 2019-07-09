# CoffeeHouse API Wrapper for Python

This is a very simple API Wrapper for the CoffeeHouse API. Using
This Library only supports the v2 API which is based from
this [Documentation](https://gist.github.com/Netkas/d3617e5b5b66c7851c728d3c0073529a)


## Installation
```sh
python3 setup.py build
python3 setup.py install
```

## Usage

```python
import coffeehouse

CoffeeHouse = coffeehouse.API("<API KEY>")

# Creating a session
Session = CoffeeHouse.create_session("en")

print("Session ID: {0}".format(Session.id))
print("Session Available: {0}".format(str(Session.available)))
print("Session Language: {0}".format(Session.language))
print("Session Expires: {0}".format(str(Session.expires)))

# Getting AI Output using the session
Output = CoffeeHouse.think_thought(Session.id, "Hello!")
print("Output: {0}".format(Output))
```

## Example chat script
```python
import coffeehouse

CoffeeHouse = coffeehouse.API("<API KEY>")
Session = CoffeeHouse.create_session("en")

while(True):
    Output = CoffeeHouse.think_thought(Session.id, input("Input: "))
    print("Output: {0}".format(Output))
```