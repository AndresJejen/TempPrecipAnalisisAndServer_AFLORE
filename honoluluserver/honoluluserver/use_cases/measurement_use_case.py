from honoluluserver.shared import response_object as res


class MeasurementListUseCase(object):

    def __init__(self, repo, route="station"):
        self.repo = repo
        self.route = route

    def execute(self, request_object):
        if not request_object:
            return res.ResponseFailure.build_from_invalid_request_object(request_object)

        try:
            response = self.repo.list(filters=request_object.filters, route=self.route)
            return res.ResponseSuccess(response)
        except Exception as exc:
            return res.ResponseFailure.build_system_error(
                "{}: {}".format(exc.__class__.__name__, "{}".format(exc)))