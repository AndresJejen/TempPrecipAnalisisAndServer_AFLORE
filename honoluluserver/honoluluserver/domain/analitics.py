from honoluluserver.shared.domain_model import DomainModel

def select_field(field, dictionary):
        if field in dictionary:
            return dictionary[field]['tobs']
        else:
            return None

class Analitics():
    """
    Domain Model for analitics result
    """

    def __init__(self, maxima: float, minima: float, average: float):
        """Creates an instance of analitics Model

        Args:
            maxima (float): Max value in range
            minima (float): Min Value in range
            average (float): Average value in range
        """
        self.maxima = maxima
        self.minima = minima
        self.average = average

    def to_dict(self):
        return {
            'maxima': self.maxima,
            'minima': self.minima,
            'average': self.average,
        }
    
    @classmethod
    def from_dict(cls, adict):
        analitic = Analitics(
            maxima = select_field('max', adict),
            minima= select_field('min', adict),
            average= select_field('mean', adict),
        )

        return analitic

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()

DomainModel.register(Analitics)