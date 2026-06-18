import json # Lets python convert lists and dictionaries to json text and v.v
import os # Lets python interact with the os
from models.user import User

DATA_FILE = "data/storage.json" # Write in capital letters to make it a constant

def load_data():
  if not os.path.exists(DATA_FILE): # Checks my os to see if the file path exists if not it returns an empty users object
    return {"users": {}}
  try:
    with open(DATA_FILE, "r") as file: # Stores DATA_FILE in variable file
      raw = json.load(file) # Takes the text in the json file and changes it to a dictionary
      users = [User.from_dict(u) for u in raw.get("users", [])]
      return {"users": users}
  except json.JSONDecodeError:
    return {"users": []} # If file is empty
  
def save_data(data):
  with open(DATA_FILE, "w") as file:
    json.dump(
      {"users": [u.to_dict() for u in data.get("users", [])]},
        file,
        indent=4) 
    # Takes the python dictionary and changes it to json text
    # Use indent to make it readablen