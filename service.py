import row as row
import json
from models import *
from config import db


def insert_data_user(input_data):
    for row in input_data:
        db.session.add(
            User(
                id=row.get("id"),
                first_name=row.get("first_name"),
                last_name=row.get("last_name"),
                age=row.get("age"),
                email=row.get("email"),
                role=row.get("role"),
                phone=row.get("phone")
            )
        )

    db.session.commit()


def insert_data_order(input_data):
    for row in input_data:
        db.session.add(
            Order(
                id=row.get("id"),
                name=row.get("name"),
                description=row.get("description"),
                start_date=row.get("start_date"),
                end_date=row.get("end_date"),
                address=row.get("address"),
                price=row.get("price"),
                customer_id=row.get("customer_id"),
                executor_id=row.get("executor_id")
            )
        )

    db.session.commit()


def insert_data_offer(input_data):
    for row in input_data:
        db.session.add(
            Offer(
                id=row.get("id"),
                order_id=row.get("order_id"),
                executor_id=row.get("executor_id")
            )
        )

    db.session.commit()


def get_all(model):
    result = []
    for row in db.session.query(model).all():
        result.append(row.to_dict())

    return result

def update(model, user_id, values):
    data = db.session.query(model).get(user_id)
    data.id = values.get('id')
    data.first_name = values.get('first_name')
    data.last_name = values.get('last_name')

    db.session.commit()


def update_v2(model, user_id, values):
    db.session.query(model).filter(model.id == user_id).update().values(values)
    db.session.commit()


def delete(model, user_id):
    db.session.query(model).filter(model.id == user_id).delete()
    db.session.commit()


def init_db():
    db.drop_all()
    db.create_all()

    with open("data/user.json", encoding="utf-8") as file:
        insert_data_user(json.load(file))

    with open("data/offers.json", encoding="utf-8") as file:
        insert_data_offer(json.load(file))

    with open("data/orders.json", encoding="utf-8") as file:
        insert_data_order(json.load(file))
