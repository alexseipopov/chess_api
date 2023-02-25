from .utils import SerializeTable
from ...database.model import User
from ...database import db
from .. import api


@api.get("/user")
def get_all_user():
    user = SerializeTable(User).all_data()
    print(user)
    return {
        "status": "OK",
        "data": user
    }


@api.get("/user/<int:id>")
def get_user(id):
    user = SerializeTable(User, userId=id).data()
    return {
        "status": "OK",
        "data": user[0]
    } if user else {
        "status": "FAILURE",
        "description": "User does not exist"
    }
