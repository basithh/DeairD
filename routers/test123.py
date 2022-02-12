from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
from  model.LocationModel import LocationData

app = APIRouter()

# temp database
fakedb = []

# course model to store courses
# class Course(BaseModel):
#     id: int
#     name: str
#     price: float
#     is_early_bird: Optional[bool] = None

# Home/welcome route
@app.get("/")
def read_root():
    return {"greetings": "Your in Test"}

# Get all courses
@app.get("/courses")
def get_courses():
    return fakedb

# get single course
@app.get("/courses/{name_state}")
def get_a_course(course_id: str):
    course = course_id - 1
    return fakedb[course]

# add a new course
@app.post("/courses")
def add_course(course: LocationData):
    fakedb.append(course.dict())
    return fakedb

# delete a course
@app.delete("/courses/{course_id}")
def delete_course(course_id: int):
    fakedb.pop(course_id-1)
    return {"task": "deletion successful"}