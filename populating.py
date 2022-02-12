from database import db
from model.RouteModel import LocationData

from itertools import permutations


state = db["location_db"].find()
# for i in state:
#     db["location_db"].insert_one({"state":i})

print(len(permutations(state,2)))
    # db["route_db"].insert_one({"tostate":i[0]['_id'],"forstate":i[1]['_id']})

    