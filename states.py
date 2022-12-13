import json

# Read the United states file
with open("united states.json") as states_file:
    USA_STATES = json.load(states_file)
# Read the canada states file
with open("canada states.json") as canada_file:
    CANADA_STATES = json.load(canada_file)
# Read the australia states file
with open("australia states.json") as australia_file:
    AUSTRALIA_STATES = json.load(australia_file)
