import json
from flask import Blueprint, Response

from honoluluserver.use_cases import request_objects as req
from honoluluserver.repositories import memrepo as mr
from honoluluserver.use_cases import station_use_case as uc
from honoluluserver.serializers import station_serializer as ser

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

@blueprint.route('/stations', methods=['GET'])
def stations():
    request_object = req.StationListRequestObject.from_dict({})

    repo = mr.MemRepo([station1_dict, station2_dict, station3_dict])
    use_case = uc.StationListUseCase(repo)

    response = use_case.execute(request_object)

    return Response(json.dumps(response.value, cls=ser.StationEncoder),
                    mimetype='application/json',
                    status=200)