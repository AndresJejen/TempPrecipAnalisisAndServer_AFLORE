import pytest
import json
from honoluluserver.serializers import measurement_serializer as srs
from honoluluserver.domain.measurement import Measurement
import datetime

def test_serialize_domain_Measurement():

    measurement = Measurement(
        "Station1",
        "2020-10-02",
        3,
        5,
        id=123
    )

    expected_json = '{ "id": 123, "station": "Station1", "date": "2020-10-02", "prcp": 3, "tobs": 5 }'

    json_measurement = json.dumps(measurement, cls=srs.MeasurementEncoder)

    json1 = json.loads(json_measurement)
    json2 = json.loads(expected_json)

    assert json1 == json2

def test_serialize_domain_measurement_wrong_type():
    with pytest.raises(TypeError):
        json.dumps(datetime.datetime.now(), cls=srs.MeasurementEncoder)