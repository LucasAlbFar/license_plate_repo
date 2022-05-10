"""
Routes and app starter
"""

from flask import jsonify
from marshmallow import ValidationError

from ma import ma
from db import db
from controllers.plates import (
    LicensePlate,
    LicensePlateList,
    LicensePlateListSearch,
)

from server.instance import server

api = server.api
app = server.app


@app.before_first_request
def create_tables():
    db.create_all()


@api.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify(error.messages), 400


api.add_resource(LicensePlateList, '/plate')
api.add_resource(LicensePlate, '/plate')
api.add_resource(LicensePlateListSearch, '/search-plate')

if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    server.run()
