from database import db
from model.RouteModel import LocationData

from itertools import permutations
import pandas as pd

data = pd.read_csv('state.csv.txt')

# for i in data["state"].unique():
#   db["state_db"].insert_one({"state":i})


# for i in state:
#     db["location_db"].insert_one({"state":i})

# print(len(permutations(state,2)))
    # db["route_db"].insert_one({"tostate":i[0]['_id'],"forstate":i[1]['_id']})


for i in range(len(data)):
  a = db["state_db"].find_one({"state":data["state"][i]})
  db["city_db"].insert_one({"city":data["city"][i],"stateid":a['_id']})
