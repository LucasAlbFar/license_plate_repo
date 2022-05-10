"""
Operations around license plates
"""

from Levenshtein import distance
from re import compile
from typing import Union


class PlateOperations():
    """
    Validate license plate.
    """

    def __init__(self: object, plate: str) -> None:
        self.plate = plate

    def check_plate_de(
        self: object,
    ) -> Union[bool, str]:
        """
        Check through regular expression, the plate format sent.

        :return: Boolean to valid or not license plate;
                 License plate upper case.
        """

        plate_format = compile('^[a-zA-Z]{1,3}(-)[a-zA-z]{1,2}[0-9]{1,4}$')

        if plate_format.match(self.plate) is None:
            return False, self.plate

        return True, self.plate.upper()


class SearchOperations():
    """
    Assembly Levenshtein search results.
    """

    def check_distance(
        self: object,
        request: dict,
        plate_db: object
    ) -> dict:
        """
        Calcule the Levenshtein distance and assembly results.

        :param request: Request data.
        :para plate_db: All data input on database.

        :return: Search result dictionary.
        """

        if not request.get('key') or not request.get('levenshtein'):
            return False

        if not request.get('levenshtein').isdigit():
            return False

        plate = request.get('key').upper()
        lev = int(request.get('levenshtein'))

        list_results = []
        for item in plate_db:
            if (distance(plate, item.plate.replace("-", ""))) <= lev:
                list_results.append({
                    'plate': item.plate,
                    'timestamp': item.timestamp,
                })

        dict_results = {}
        dict_results.update({plate: list_results})

        return dict_results
