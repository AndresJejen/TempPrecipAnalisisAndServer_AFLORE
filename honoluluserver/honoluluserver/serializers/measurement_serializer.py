import json


class MeasurementEncoder(json.JSONEncoder):
    """Encode Measurement Data to JSON

    Args:
        json ([type]): [description]
    """

    def default(self, o):
        try:
            to_serialize = {
                'id': o.id,
                'station': o.station,
                'date': o.date,
                "prcp": o.prcp,
                "tobs": o.tobs,
            }
            return to_serialize
        except AttributeError:
            return super().default(o)