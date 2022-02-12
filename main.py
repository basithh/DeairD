from fastapi import  FastAPI

from routers import dealer, driver,user

app = FastAPI()

app.include_router(dealer.router,prefix="/dealer")
# app.include_router(driver.router,prefix="/driver")
app.include_router(user.router,prefix='/user')


@app.get("/")
async def root():
    return {"message": "Hello Welcome to Deaird Please visit <a href='/docs'>Docs</a>"}