import uuid

import pytest
from unittest import mock

from honoluluserver.domain.station import Station
from honoluluserver.shared import response_object as res
from honoluluserver.use_cases import request_objects as req
from honoluluserver.use_cases import station_use_case as uc


@pytest.fixture
def domain_station():
    station_1 = Station(
        "Station1",
        "Station1Name",
        3,
        5,
        55
    )

    station_2 = Station(
        "Station2",
        "Station2Name",
        33,
        54,
        551
    )

    station_3 = Station(
        "Station3",
        "Station3Name",
        34,
        55,
        552
    )

    station_4 = Station(
        "Station4",
        "Station4Name",
        35,
        56,
        553
    )

    return [station_1, station_2, station_2, station_3]


def test_station_list_without_parameters(domain_station):
    repo = mock.Mock()
    repo.list.return_value = domain_station

    station_list_use_case = uc.StationListUseCase(repo)
    request_object = req.StationListRequestObject.from_dict({})

    response_object = station_list_use_case.execute(request_object)

    assert bool(response_object) is True
    repo.list.assert_called_with(filters=None)

    assert response_object.value == domain_station

def test_station_list_with_filters(domain_station):
    repo = mock.Mock()
    repo.list.return_value = domain_station

    station_list_use_case = uc.StationListUseCase(repo)
    qry_filters = {'a': 5}
    request_object = req.StationListRequestObject.from_dict({'filters': qry_filters})

    response_object = station_list_use_case.execute(request_object)

    assert bool(response_object) is True
    repo.list.assert_called_with(filters=qry_filters)
    assert response_object.value == domain_station

def test_station_list_handles_generic_error():
    repo = mock.Mock()
    repo.list.side_effect = Exception('Just an error message')

    station_list_use_case = uc.StationListUseCase(repo)
    request_object = req.StationListRequestObject.from_dict({})

    response_object = station_list_use_case.execute(request_object)

    assert bool(response_object) is False
    assert response_object.value == {
        'type': res.ResponseFailure.SYSTEM_ERROR,
        'message': "Exception: Just an error message"
    }

def test_station_list_handles_bad_request():
    repo = mock.Mock()

    station_list_use_case = uc.StationListUseCase(repo)
    request_object = req.StationListRequestObject.from_dict({'filters': 5})

    response_object = station_list_use_case.execute(request_object)

    assert bool(response_object) is False
    assert response_object.value == {
        'type': res.ResponseFailure.PARAMETERS_ERROR,
        'message': "filters: Is not iterable"
    }