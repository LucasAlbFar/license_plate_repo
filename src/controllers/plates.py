"""
License Plates requests controlls
"""

from flask import request
from flask_restplus import Resource, fields

from models.license_plate import LicensePlateModel
from schemas.license_plate import LicensePlateSchema
from controllers.constants import (
    NOT_FOUND_LICENSE_PLATES,
    NOT_VALID_PLATE_DE,
    INVALID_REQUEST,
)
from controllers.operations import PlateOperations, SearchOperations
from server.instance import server

license_plate_ns = server.license_plate_ns
license_plate = LicensePlateSchema()
license_plate_list_schema = LicensePlateSchema(many=True)

item = license_plate_ns.model('Plate', {
    'plate': fields.String(),
})


class LicensePlateList(Resource):
    """
    Manage GET request for route api/get/plate
    """

    @license_plate_ns.doc('Retrieve all license plate')
    def get(self, ):
        license_plate_data = LicensePlateModel.find_all()

        if license_plate_data:
            return license_plate_list_schema.dump(license_plate_data), 200

        return {'message': NOT_FOUND_LICENSE_PLATES}, 404


class LicensePlateListSearch(Resource):
    """
    Manage GET request for route api/get/search-plate
    """

    @license_plate_ns.doc('Levenshtein license plate distance')
    def get(self, ):
        license_plate_data = LicensePlateModel.find_all()
        search = SearchOperations()
        results = search.check_distance(
            request=request.args.to_dict(),
            plate_db=license_plate_data,
            )

        if not results:
            return {'message': INVALID_REQUEST}, 400

        return results, 200


class LicensePlate(Resource):
    """
    Manage POST request for route api/post/plate
    """

    @license_plate_ns.expect(item)
    @license_plate_ns.doc('Include a German License Plate')
    def post(self, ):
        plate_json = request.get_json()
        license_plate_data = license_plate.load(plate_json)

        plate_operations = PlateOperations(license_plate_data.plate)

        if not license_plate_data.plate:
            return {'message': INVALID_REQUEST}, 400

        is_valid, license_plate_data.plate = plate_operations.check_plate_de()

        if is_valid:
            license_plate_data.save_to_db()
            return license_plate.dump(license_plate_data), 200

        return {'message': NOT_VALID_PLATE_DE}, 422
