import json
from unittest import mock

from honoluluserver.shared import response_object as res
from honoluluserver.domain.station import Station

station1_dict = {
            'id': 125,
            'station': "Station3",
            'name': "Station3Name",
            'longitude': -0.29998975,
            'latitude': 51.77436293,
            'elevation': 12301
        }

station1_domain_model = Station.from_dict(station1_dict)

stations = [station1_domain_model]


@mock.patch('honoluluserver.use_cases.station_use_case.StationListUseCase')
def test_get(mock_use_case, client):
    mock_use_case().execute.return_value = res.ResponseSuccess(stations)

    http_response = client.get('/stations')

    assert json.loads(http_response.data.decode('UTF-8')) == [station1_dict]
    assert http_response.status_code == 200
    assert http_response.mimetype == 'application/json'