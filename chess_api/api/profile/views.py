from flask import request
from .utils import SerializeTable, validate_request, get_invalid_params, validate_requires, create_res_obj
from ...database.model import User
from ...database import db
from .. import api


@api.get("/user")
def get_all_user():
    user = SerializeTable(User).all_data()
    print(user)
    return create_res_obj(data=user)


@api.get("/user/<int:id>")
def get_user(id):
    user = SerializeTable(User, userId=id).data()
    return create_res_obj(data=user[0]) if user else create_res_obj(status="FAILURE", description="User does not exist")


@api.post("/user")
def post_user():
    require_fields = ["name", "isParent", "phone"]
    if validate_requires(require_fields, request.form):
        # TODO white check for illigal parametrs or inset into table only nessesary params (ignore illigal)
        pass
    return create_res_obj(status="FAILURE", description="No such parametrs")


@api.put("/user/<int:id>")
def put_user(id):
    user = User.query.filter_by(userId=id).first()
    if user:
        if validate_request(User, request.form):
            User.query.filter_by(userId=id).update(dict(request.form))
            db.session.commit()
            update_user = SerializeTable(User, userId=id).data()
            return create_res_obj(data=update_user[0])
        error_msg = ', '.join(get_invalid_params(User, request.form))
        return create_res_obj(status="FAILURE", description=f"Invalid params {error_msg}")
    return create_res_obj(status="FAILURE", description=f"User id = {id} does not exist")
