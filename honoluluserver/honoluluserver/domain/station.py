from honoluluserver.shared.domain_model import DomainModel

class Station():
    """
    Domain Model for station table
    """

    def __init__(self, station: str, name: str, latitude: float, longitude: float, elevation: float, id: int = None):
        """Creates an instance of Station Model

        Args:
            station (str): Station Code
            name (str): Name of the station
            latitude (float): Latitude Value
            longitude (float): Longitude value
        """
        self.id = id
        self.station = station
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.elevation = elevation

    def to_dict(self):
        return {
            'id': self.id,
            'station': self.station,
            'name': self.name,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'elevation': self.elevation,
        }

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()

DomainModel.register(Station)