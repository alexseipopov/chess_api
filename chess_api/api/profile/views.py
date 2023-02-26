from flask import request
from .utils import SerializeTable, validate_request, get_invalid_params, validate_requires, create_res_obj, bool_transform
from ...database.model import User, Child
from ...database import db
from .. import api


@api.get("/user")
def get_all_user():
    user = SerializeTable(User).all_data()
    return create_res_obj(data=user)


@api.get("/user/<int:id>")
def get_user(id):
    user = SerializeTable(User, userId=id).data()
    return create_res_obj(data=user[0]) if user else create_res_obj(status="FAILURE", description="User does not exist")


@api.post("/user")
def post_user():
    require_fields = ["name", "isParent", "phone"]
    if validate_requires(require_fields, request.form):
        if validate_request(User, request.form):
            insert_data = bool_transform(request.form, ["isParent"])
            user = User(**insert_data)
            db.session.add(user)
            db.session.commit()
            created_user = SerializeTable(User, userId=user.userId).data()
            return create_res_obj(data=created_user[0])
        error_msg = ', '.join(get_invalid_params(User, request.form))
        return create_res_obj(status="FAILURE", description=f"Invalid params {error_msg}")
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


@api.get("/child")
def get_all_child():
    child = SerializeTable(Child).all_data()
    return create_res_obj(data=child)


@api.get("/child/<int:id>")
def get_child(id):
    child = SerializeTable(Child, childId=id).data()
    return create_res_obj(data=child[0]) if child else create_res_obj(status="FAILURE", description="Child does not exist")


@api.post("/child")
def post_child():
    require_fields = ["userId", "name"]
    if validate_requires(require_fields, request.form):
        if validate_request(Child, request.form):
            insert_data = request.form
            child = Child(**insert_data)
            db.session.add(child)
            db.session.commit()
            created_user = SerializeTable(Child, childId=child.childId).data()
            return create_res_obj(data=created_user[0])
        error_msg = ', '.join(get_invalid_params(Child, request.form))
        return create_res_obj(status="FAILURE", description=f"Invalid params {error_msg}")
    return create_res_obj(status="FAILURE", description="No such parametrs")


@api.put("/child/<int:id>")
def put_child(id):
    child = Child.query.filter_by(childId=id).first()
    if child:
        if validate_request(Child, request.form):
            Child.query.filter_by(childId=id).update(dict(request.form))
            db.session.commit()
            update_child = SerializeTable(Child, childId=id).data()
            return create_res_obj(data=update_child[0])
        error_msg = ', '.join(get_invalid_params(Child, request.form))
        return create_res_obj(status="FAILURE", description=f"Invalid params {error_msg}")
    return create_res_obj(status="FAILURE", description=f"Child id = {id} does not exist")


@api.delete("/child/<int:id>")
def delete_child(id):
    child = Child.query.filter_by(childId=id).first()
    if child:
        child_data = SerializeTable(Child, childId=id).data()
        db.session.delete(child)
        db.session.commit()
        return create_res_obj(data=child_data[0])
    return create_res_obj(status="FAILURE", description=f"Child id = {id} does not exist")
