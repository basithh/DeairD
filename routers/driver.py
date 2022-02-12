
from fastapi import APIRouter ,  Depends,Body,status
from model.LocationModel import LocationData,locationdb
from model.RouteModel import RouteData,routedb
# from schema.LocationSchema import Job
# from sqlalchemy.orm import Session



router = APIRouter()

@router.post("/")
async def create_todo(todo: LocationData):
    _id = locationdb.insert_one(dict(todo))
    return {"message":"Sucess"}

@router.post("/new")
async def create_todo(todo: RouteData):
    _id = routedb.insert_one(dict(todo))
    return {"message":"Sucess"}


# @router.post("/", response_description="Add new student", response_model=LocationData)
# async def create_student(student: LocationData = Body(...)):
#     student = jsonable_encoder(student)
#     new_student = await db["students"].insert_one(student)
#     created_student = await db["students"].find_one({"_id": new_student.inserted_id})
#     return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_student)



# @router.post("/")
# def create(details: LocationData, db: Session = Depends(get_db)):
#     to_create = Job(
#         name=details.name,
#     )
#     db.add(to_create)
#     db.commit()
#     return { 
#         "success": True,
#     }


# # temp database
# fakedb = []

# # course model to store courses
# # class Course(BaseModel):
# #     id: int
# #     name: str
# #     price: float
# #     is_early_bird: Optional[bool] = None

# # Home/welcome route
# @router.get("/")
# def read_root():
#     return {"greetings": "Your in Test"}

# # Get all courses
# @router.get("/courses")
# def get_courses():
#     return fakedb

# # get single course
# @router.get("/courses/{name_state}")
# def get_a_course(course_id: str):
#     course = course_id - 1
#     return fakedb[course]

# # add a new course
# @router.post("/courses")
# def add_course(course: LocationData):
#     fakedb.append(course.dict())
#     return fakedb

# # delete a course
# @router.delete("/courses/{course_id}")
# def delete_course(course_id: int):
#     fakedb.pop(course_id-1)
#     return {"task": "deletion successful"}