"""
License Plate schema class.
"""

from ma import ma
from models.license_plate import LicensePlateModel


class LicensePlateSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = LicensePlateModel
        load_instance = True
        fields = ['plate','timestamp']
