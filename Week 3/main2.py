from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

posts = []


class PostCreate(BaseModel):
    title: str
    content: str
    user_id: int


class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    user_id: int


class MessageResponse(BaseModel):
    message: str


@app.post(
    "/posts",
    response_model=MessageResponse
)
def create_post(post: PostCreate):
    posts.append(post)
    return {"message": "Post created"}


@app.get(
    "/posts",
    response_model=list[PostCreate]
)
def get_posts():
    return posts