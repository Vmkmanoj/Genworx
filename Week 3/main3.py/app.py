import database
from pydantic import BaseModel

from fastapi import FastAPI


app = FastAPI()

class User(BaseModel):
    id : int
    name : str
    age : int

class updateDetails(BaseModel):
    id : int
    name : str

class userResponce(BaseModel):
    id : int
    name :str
    age : int



@app.post("/addUser")
def userAdduser(users : User):
    database.cur.execute(""" 
        INSERT INTO users
        (id, name, age)
        VALUES (%s, %s, %s)
        """,
        (
            users.id,
            users.name,
            users.age
        )
    )

    database.conn.commit()

    return {"message" : "User created"}


@app.delete("/deleteUserId/{id}")
def deleteUserId(id: int):
    database.cur.execute(
        """
        DELETE FROM users
        WHERE id = %s
        """,
        (id,)
    )

    database.conn.commit()

    return {"message": f"user deleted {id}"}

@app.patch("/updateDate/{id}")
def updateData(id: int, user: User):
    database.cur.execute(
        """
        UPDATE users
        SET name = %s,
            age = %s
        WHERE id = %s
        """,
        (
            user.name,
            user.age,
            id
        )
    )

    database.conn.commit()

    return {"message": "User updated successfully"}


@app.get("/getAll",response_model=list[userResponce])
def getAll():
    database.cur.execute("SELECT * FROM users")
    respone =  database.cur.fetchall()


    return [
        {
            "id":res[0],
            "name":res[1],
            "age":res[2]
        }
        for res in respone
    ]

