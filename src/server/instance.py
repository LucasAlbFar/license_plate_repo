"""
License Plate app instance.
"""

from flask import Flask, Blueprint
from flask_restplus import Api


class Server:
    def __init__(self) -> None:
        self.app = Flask(__name__)
        self.blueprint = Blueprint(
            'api',
            __name__,
            url_prefix='/api'
        )
        self.api = Api(
            self.blueprint,
            doc='/doc',
            title='License Plate Repository'
        )

        self.app.register_blueprint(self.blueprint)

        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
        self.app.config['PROPAGATE_EXPECTIONS'] = True
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        self.license_plate_ns = self.license_plate_ns()

    def license_plate_ns(self, ):
        """
        License plate app namespace.
        """

        return self.api.namespace(
            name='License Plate Repository',
            description='License plate repository operations',
            path='/'
        )

    def run(self, ):
        """
        Run function.
        """

        self.app.run(
            port=5000,
            debug=True,
            host='0.0.0.0',
        )


server = Server()
