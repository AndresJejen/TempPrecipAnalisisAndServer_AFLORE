import pytest

from honoluluserver.domain.station import Station
from honoluluserver.shared.domain_model import DomainModel

from honoluluserver.repositories import memrepo


@pytest.fixture
def station_dicts():
    return [
        {
            'id': 123,
            'station': "Station1",
            'name': "Station1Name",
            'longitude': -0.09998975,
            'latitude': 51.75436293,
            'elevation': 1234
        },
        {
            'id': 124,
            'station': "Station2",
            'name': "Station2Name",
            'longitude': -0.19998975,
            'latitude': 51.76436293,
            'elevation': 12345
        },
        {
            'id': 125,
            'station': "Station3",
            'name': "Station3Name",
            'longitude': -0.29998975,
            'latitude': 51.77436293,
            'elevation': 12301
        },
        {
            'id': 126,
            'station': "Station4",
            'name': "Station4Name",
            'longitude': -0.39998975,
            'latitude': 51.78436293,
            'elevation': 1230
        }
    ]

def _check_results(domain_models_list, data_list):
    assert len(domain_models_list) == len(data_list)
    assert all([isinstance(dm, DomainModel) for dm in domain_models_list])
    assert set([dm.id for dm in domain_models_list]
               ) == set([d['id'] for d in data_list])


def test_repository_list_without_parameters(station_dicts):
    repo = memrepo.MemRepo(station_dicts)

    lista = repo.list()

    _check_results(
        lista,
        station_dicts
    )


def test_repository_list_with_filters_unknown_key(station_dicts):
    repo = memrepo.MemRepo(station_dicts)

    with pytest.raises(KeyError):
        repo.list(filters={'namee': 'aname'})


def test_repository_list_with_filters_unknown_operator(station_dicts):
    repo = memrepo.MemRepo(station_dicts)

    with pytest.raises(ValueError):
        repo.list(filters={'price__in': [20, 30]})


def test_repository_list_with_filters_elevation(station_dicts):
    repo = memrepo.MemRepo(station_dicts)

    lista = repo.list(filters={'elevation': 1230})

    _check_results(
        lista,
        [station_dicts[3]]
    )


def test_repository_list_with_filters_latitude(station_dicts):
    repo = memrepo.MemRepo(station_dicts)

    _check_results(
        repo.list(filters={'latitude__eq': 51.78436293}),
        [station_dicts[3]]
    )


def test_repository_list_with_filters_elevation_lt(station_dicts):
    repo = memrepo.MemRepo(station_dicts)

    _check_results(
        repo.list(filters={'elevation__lt': 1235}),
        [station_dicts[0], station_dicts[3]])


def test_repository_list_with_filters_elevation__gt(station_dicts):
    repo = memrepo.MemRepo(station_dicts)
    _check_results(
        repo.list(filters={'elevation__gt': 12344}),
        [station_dicts[1]]
    )


def test_repository_list_with_filters_id(station_dicts):
    repo = memrepo.MemRepo(station_dicts)

    _check_results(
        repo.list(filters={'id': 125}),
        [station_dicts[2]]
    )