from config import app
import json
from models import Order, User, Offer
from service import init_db, get_all, insert_data_user, update, update_v2, insert_data_order, insert_data_offer, delete
from flask import request


@app.route("/users/", methods=["GET", "POST"])
def get_users():
    if request.method == "GET":
        return app.response_class(
            response=json.dumps(get_all(User), indent=4),
            status=200,
            mimetype="application/json"
        )
    elif request.method == "POST":
        if isinstance(request.json, list):
            insert_data_user(request.json)
        elif isinstance(request.json, dict):
            insert_data_user([request.json])


@app.route("/user/<int:user_id>", methods=["GET", "PUT", "DELETE"])
def get_user_by_id(user_id):
    data = get_all(User)
    if request.method == "GET":
        for row in data:
            if row.get("id") == user_id:
                return app.response_class(
                    response=json.dumps(row, indent=4),
                    status=200,
                    mimetype="application/json"
                )
    elif request.method == "PUT":
        update_v2(User, user_id, request.json)
        return app.response_class(
            response=json.dumps(["OK"], indent=4),
            status=200,
            mimetype="application/json"
        )
    elif request.method == "DELETE":
        delete(User, user_id)
        return app.response_class(
            response=json.dumps(["OK"], indent=4),
            status=200,
            mimetype="application/json"
        )

@app.route("/orders/", methods=["GET", "POST"])
def get_orders():
    if request.method == "GET":
        return app.response_class(
            response=json.dumps(get_all(Order), indent=4),
            status=200,
            mimetype="application/json"
        )
    elif request.method == "POST":
        if isinstance(request.json, list):
            insert_data_order(request.json)
        elif isinstance(request.json, dict):
            insert_data_order([request.json])


@app.route("/order/<int:order_id>", methods=["GET", "PUT", "DELETE"])
def get_order_by_id(order_id):
    data = get_all(Order)
    if request.method == "GET":
        for row in data:
            if row.get("id") == order_id:
                return app.response_class(
                    response=json.dumps(row, indent=4),
                    status=200,
                    mimetype="application/json"
                )
    elif request.method == "PUT":
        update_v2(User, order_id, request.json)
        return app.response_class(
            response=json.dumps(["OK"], indent=4),
            status=200,
            mimetype="application/json"
        )
    elif request.method == "DELETE":
        delete(User, order_id)
        return app.response_class(
            response=json.dumps(["OK"], indent=4),
            status=200,
            mimetype="application/json"
        )


@app.route("/offers/", methods=["GET", "POST"])
def get_offers():
    if request.method == "GET":
        return app.response_class(
            response=json.dumps(get_all(Offer), indent=4),
            status=200,
            mimetype="application/json"
        )
    elif request.method == "POST":
        if isinstance(request.json, list):
            insert_data_offer(request.json)
        elif isinstance(request.json, dict):
            insert_data_offer([request.json])


@app.route("/offer/<int:offer_id>", methods=["GET", "PUT", "DELETE"])
def get_offer_by_id(offer_id):
    data = get_all(Offer)
    if request.method == "GET":
        for row in data:
            if row.get("id") == offer_id:
                return app.response_class(
                    response=json.dumps(row, indent=4),
                    status=200,
                    mimetype="application/json"
                )
    elif request.method == "PUT":
        update_v2(User, offer_id, request.json)
        return app.response_class(
            response=json.dumps(["OK"], indent=4),
            status=200,
            mimetype="application/json"
        )
    elif request.method == "DELETE":
        delete(User, offer_id)
        return app.response_class(
            response=json.dumps(["OK"], indent=4),
            status=200,
            mimetype="application/json"
        )


if __name__ == '__main__':
    init_db()
    app.run(host='127.0.0.1', port=8080, debug=True)
