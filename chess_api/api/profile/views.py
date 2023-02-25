from flask import request
from .utils import SerializeTable, validate_request, get_invalid_params
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


@api.put("/user/<int:id>")
def put_user(id):
    user = User.query.filter_by(userId=id).first()
    if user:
        if validate_request(User, request.form):
            User.query.filter_by(userId=id).update(dict(request.form))
            db.session.commit()
            return {"status": "OK", "ID": user.userId}
        return {
            "status": "FAILURE",
            "description": f"Invalid params {', '.join(get_invalid_params(User, request.form))}"
        }
    return {
        "status": "FAILURE",
        "description": f"User id = {id} does not exist"
    }
