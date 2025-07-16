# Week 4: Libraries
import json
import requests
import sys

# checking if arg is provided
if len(sys.argv) != 2:
    sys.exit("No arg provided")

# using itunes API and use Python to get info about a band
response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1])

# if you want to see whole data, execute line below:
# print(json.dumps(response.json(), indent=4))

# saving values gotten from the URL, in a json format
o = response.json()

# if you want to see only a specific field value
for result in o["results"]:
    print(result["trackName"])
