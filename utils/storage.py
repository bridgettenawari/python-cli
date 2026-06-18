import json # Lets python convert lists and dictionaries to json text and v.v
import os # Lets python interact with the os

DATA_FILE = "data/storage.json" # Write in capital letters to make it a constant

def load_data():
  if not os.path.exists(DATA_FILE): # Checks my os to see if the file path exists if not it returns an empty users object
    return {"users": {}}
  with open(DATA_FILE, "r") as file: # Stores DATA_FILE in variable file
    try:
      return json.load(file) # Takes the text in the json file and changes it to a dictionary
    except json.JSONDecodeError:
      return {"users": []} # If file is empty
  
def save_data(data):
  with open(DATA_FILE, "w") as file:
    json.dump(data, file, indent=4) # Takes the python dictionary and changes it to json text
    # Use indent to make it readablen