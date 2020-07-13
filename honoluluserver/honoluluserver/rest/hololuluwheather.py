import json
from flask import Blueprint, Response

from honoluluserver.use_cases import request_objects as req
from honoluluserver.repositories import memrepo as mr
from honoluluserver.repositories import sqlAlchenyrepo as sql
from honoluluserver.use_cases import station_use_case as uc
from honoluluserver.use_cases import measurement_use_case as muc
from honoluluserver.use_cases import analitics_use_case as auc
from honoluluserver.serializers import station_serializer as ser
from honoluluserver.serializers import measurement_serializer as mser
from honoluluserver.serializers import analitics_serializer as aser

blueprint = Blueprint('hololuluwheather', __name__)

station1_dict = {
            'id': 125,
            'station': "Station1",
            'name': "Station1Name",
            'longitude': -0.29998975,
            'latitude': 51.77436293,
            'elevation': 123
        }

station2_dict = {
            'id': 126,
            'station': "Station2",
            'name': "Station2Name",
            'longitude': -0.29998975,
            'latitude': 51.77436293,
            'elevation': 124
        }

station3_dict = {
            'id': 127,
            'station': "Station3",
            'name': "Station3Name",
            'longitude': -0.29998975,
            'latitude': 51.77436293,
            'elevation': 125
        }

@blueprint.route('/api/v1.0/<start>', methods=['GET'])
def temp_range_start(start):
    request_object = req.StationListRequestObject.from_dict({})

    repo = sql.SQLiteRepo()
    use_case = auc.AnaliticsListUseCase(repo, start, route="start")

    response = use_case.execute(request_object)

    return Response(json.dumps(response.value, cls=aser.AnaliticsEncoder),
                    mimetype='application/json',
                    status=200)

@blueprint.route('/api/v1.0/<start>/<end>', methods=['GET'])
def temp_range(start, end):
    request_object = req.StationListRequestObject.from_dict({})

    repo = sql.SQLiteRepo()
    use_case = auc.AnaliticsListUseCase(repo, start, end=end, route="range")

    response = use_case.execute(request_object)

    return Response(json.dumps(response.value, cls=aser.AnaliticsEncoder),
                    mimetype='application/json',
                    status=200)

@blueprint.route('/api/v1.0/stations', methods=['GET'])
def stations():
    request_object = req.StationListRequestObject.from_dict({})

    repo = sql.SQLiteRepo()
    use_case = uc.StationListUseCase(repo)

    response = use_case.execute(request_object)

    return Response(json.dumps(response.value, cls=ser.StationEncoder),
                    mimetype='application/json',
                    status=200)

@blueprint.route('/api/v1.0/precipitation', methods=['GET'])
def precipitation():
    request_object = req.StationListRequestObject.from_dict({})

    repo = sql.SQLiteRepo()
    use_case = muc.MeasurementListUseCase(repo, "precipitation")

    response = use_case.execute(request_object)

    return Response(json.dumps(response.value, cls=mser.MeasurementEncoder),
                    mimetype='application/json',
                    status=200)

@blueprint.route('/api/v1.0/tobs', methods=['GET'])
def tobs():
    request_object = req.StationListRequestObject.from_dict({})

    repo = sql.SQLiteRepo()
    use_case = muc.MeasurementListUseCase(repo, "tobs")

    response = use_case.execute(request_object)

    return Response(json.dumps(response.value, cls=mser.MeasurementEncoder),
                    mimetype='application/json',
                    status=200)


@blueprint.route('/', methods=['GET'])
def root():
    response = {
        "/": "Shows all the available routes",
        "/api/v1.0/precipitation": "Shows all the precitation data from measures table last 12 months",
        "/api/v1.0/stations": "Shows all the stations",
        "/api/v1.0/tobs": "Shows all the temperatures for the last 12 months",
    }
    
    return Response(json.dumps(response),
                    mimetype='application/json',
                    status=200)