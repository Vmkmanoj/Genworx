from model import UserCreateBlog
from fastapi import FastAPI , Depends
from database import get_db
from sqlalchemy.orm import Session
from pydantic import BaseModel
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class UserResponce(BaseModel):
    name : str
    blog : str



@app.post("/create-post")
def createPost(userBlog : UserResponce , db : Session = Depends(get_db)):
    
    userCreate = UserCreateBlog(name = userBlog.name,blog = userBlog.blog)
    db.add(userCreate)
    db.commit()

    return {"message" : "blog created...!"}


@app.get("/get-all-post")
def getpost(db: Session = Depends(get_db)):
    
    blog = db.query(UserCreateBlog).all()

    return blog

    

    