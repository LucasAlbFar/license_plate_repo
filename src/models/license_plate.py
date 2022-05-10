"""
License Plate Models.
"""

from datetime import datetime
from db import db


class LicensePlateModel(db.Model):
    """
    Models definition.
    """

    __tablename__ = 'license_plate'

    id = db.Column(
        db.Integer,
        primary_key=True,
    )
    plate = db.Column(
        db.String(10),
        nullable=False,
        unique=True,
    )
    timestamp = db.Column(
        db.String(20),
        nullable=True,
    )

    def __init__(self, plate) -> None:
        self.plate = plate
        self.timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')

    def __repr__(self) -> str:
        return f'LicensePlateModel(plate={self.plate},\
             timestamp{self.timestamp})'

    def json(self, ):
        return{
            'plate': self.plate,
            'timestamp': self.timestamp,
        }

    @classmethod
    def find_all(cls: object) -> object:
        """
        Query to retrieve all data from database.

        :return: All data as class objects.
        """

        return cls.query.all()

    def save_to_db(self, ):
        """
        Data base commit.
        """

        db.session.add(self)
        db.session.commit()
