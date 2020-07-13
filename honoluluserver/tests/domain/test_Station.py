from honoluluserver.domain.station import Station


def test_station_model_init():
    measurement = Station(
        "Station1",
        "Station1Name",
        3,
        5,
        55
    )

    assert measurement.station == "Station1"
    assert measurement.name == "Station1Name"
    assert measurement.latitude == 3
    assert measurement.longitude == 5
    assert measurement.elevation == 55
    