from coffeehouse import NsfwClassifier

# Create the CoffeeHouse API instance
api_key = input("API Key: ")

# Create Classifier instance
classifier = NsfwClassifier(api_key)

# Reading the Image file and sending it through the API
with open("/home/poki/Desktop/penis_dont_look.png", "rb") as f:
    result = classifier.classify(f.read())

print(result.nsfw_classification)
