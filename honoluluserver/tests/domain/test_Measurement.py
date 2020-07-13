from honoluluserver.domain.measurement import Measurement


def test_measurement_model_init():
    measurement = Measurement(
        "Station1",
        "2020-10-02",
        3,
        5
    )

    assert measurement.station == "Station1"
    assert measurement.date == "2020-10-02"
    assert measurement.prcp == 3
    assert measurement.tobs == 5
    