from honoluluserver.domain.station import Station


def test_station_model_init():
    station = Station(
        "Station1",
        "Station1Name",
        3,
        5,
        55
    )

    assert station.station == "Station1"
    assert station.name == "Station1Name"
    assert station.latitude == 3
    assert station.longitude == 5
    assert station.elevation == 55
    