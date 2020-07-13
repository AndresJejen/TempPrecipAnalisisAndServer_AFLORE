import pytest
import json
from honoluluserver.serializers import station_serializer as srs
from honoluluserver.domain.station import Station
import datetime

def test_serialize_domain_Station():

    station = Station(
        "Station1",
        "Station1Name",
        3,
        5,
        55,
        id=123
    )

    expected_json = '{ "id": 123, "station": "Station1", "name": "Station1Name", "latitude": 3, "longitude": 5, "elevation": 55 }'

    json_station = json.dumps(station, cls=srs.StationEncoder)

    json1 = json.loads(json_station)
    json2 = json.loads(expected_json)

    assert json1 == json2

def test_serialize_domain_Station_wrong_type():
    with pytest.raises(TypeError):
        json.dumps(datetime.datetime.now(), cls=srs.StationEncoder)