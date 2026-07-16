from fastapi import FastAPI
from app.database import Base, engine
from app import models
from app.routers import users, gigs, applications
app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(gigs.router)
app.include_router(applications.router)
@app.get("/")
def root():
    return {"message": "GigRadar running"}