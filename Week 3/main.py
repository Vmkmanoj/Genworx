from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    age: int
    city: str

users = []

@app.post("/addUser")
def user_add(user: User):
    users.append(user)
    return {"message": "User added successfully!"}

@app.get("/getUser")
def getUsers():
    return users

@app.get("/getUser/{userId}")
def getById(userId: int):
    for user in users:
        if user.id == userId:
            return user

    return {"message": "User not found"}

@app.delete("/deleteUser/{userId}")
def delUserId(userId: int):
    for index, user in enumerate(users):
        if user.id == userId:
            deleteUser = users.pop(index)
            return {"message": "User deleted","userDelete":deleteUser}

    return {"message": "User not found"}