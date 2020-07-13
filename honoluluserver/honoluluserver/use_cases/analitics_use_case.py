from honoluluserver.shared import response_object as res


class AnaliticsListUseCase(object):

    def __init__(self, repo, start, end= None, route="station"):
        self.repo = repo
        self.route = route
        self.start = start
        self.end = end

    def execute(self, request_object):
        if not request_object:
            return res.ResponseFailure.build_from_invalid_request_object(request_object)

        parameters = {
            "start": self.start,
            "end": self.end
        }

        try:
            response = self.repo.list(filters=parameters, route=self.route)
            return res.ResponseSuccess(response)
        except Exception as exc:
            return res.ResponseFailure.build_system_error(
                "{}: {}".format(exc.__class__.__name__, "{}".format(exc)))