import json


class AnaliticsEncoder(json.JSONEncoder):
    """Encode Analitics Data to JSON

    Args:
        json ([type]): [description]
    """

    def default(self, o):
        try:
            to_serialize = {
                'maxima': o.maxima,
                'minima': o.minima,
                'average': o.average,
            }
            return to_serialize
        except AttributeError:
            return super().default(o)