import json
from google.colab import drive
drive.mount('/content/drive', force_remount=True) #to connect colab to your google drive where the names.json file is stored.
path='/content/drive/My Drive/secretsanta/names.json' #replace with path to your names.json file. Here 'secretsanta' is a folder name.
def load_assigned():
    try:
        with open(path, 'r') as f:
            return json.load(f)  #load the file in read mode.
    except FileNotFoundError:
        print("FileNotFound")
        return []  #if the file doesn't exist, return an empty list
def save_assigned(assigned):
    with open(path, 'w') as f: #write to the file
      json.dump(assigned,f)

import random
friends=["A","B","C","D","E","F"] #write the names of the participants
assigned=load_assigned() #initialize assigned list with contents of the names.json file
def assign(val):
  random.shuffle(friends) #ensures randomness
  if friends[0]!=val and friends[0] not in assigned: #ensures you do not get your own name, or a name that someone else got
    print("You got: ",friends[0])
    assigned.append(friends[0])
    save_assigned(assigned) #saves your result in the names.json file
    
val=input("Enter your name:")
assign(val)
