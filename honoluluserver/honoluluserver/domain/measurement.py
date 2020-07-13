from honoluluserver.shared.domain_model import DomainModel

def select_field(field, dictionary):
        if field in dictionary:
            return dictionary[field]
        else:
            return None

class Measurement():
    """
    Domain Model for measurement table
    """

    def __init__(self, station: str, date: str, prcp: float, tobs: float, id: int = None):
        """Creates an instance of Measurement Model

        Args:
            station (str): Station of the measurement
            date (str): Date of the measurement
            prcp (float): Precipitation Value
            tobs (float): Temperature value
        """
        self.id = id
        self.station = station
        self.date = date
        self.prcp = prcp
        self.tobs = tobs

    def to_dict(self):
        return {
            'id': self.id,
            'station': self.station,
            'date': self.date,
            'prcp': self.prcp,
            'tobs': self.tobs,
        }
    
    @classmethod
    def from_dict(cls, adict):
        measurement = Measurement(
            id = select_field('id', adict),
            station= select_field('station', adict),
            date= select_field('date', adict),
            prcp= select_field('prcp', adict),
            tobs= select_field('tobs', adict),
        )

        return measurement

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()

DomainModel.register(Measurement)