import json


class StationEncoder(json.JSONEncoder):
    """Encode Station Data to JSON

    Args:
        json ([type]): [description]
    """

    def default(self, o):
        try:
            to_serialize = {
                'id': o.id,
                'station': o.station,
                'name': o.name,
                "latitude": o.latitude,
                "longitude": o.longitude,
                "elevation": o.elevation,
            }
            return to_serialize
        except AttributeError:
            return super().default(o)