import json
import os
#initialise the file
def init_data_file():
    if not os.path.exist('recipes.json'):
        # Create an empty JSON structure
        with open('recipes.json','w') as file:
            json.dump({'recipes':[]},file)

#load existing data from file
def load_data():
    with open('recipes.json','r') as file:
        return json.load(file)

#save data to json file 
def save_data(data):
    with open('recipe.json','w')
    json.dump(data,file,indent=4)

#example to test
if __name__ == "main":
    init_data_file()
    data = load_data()
    print("initialise data:",data)
    
        
        