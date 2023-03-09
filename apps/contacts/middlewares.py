from contacts.models import RequestResponseLog
from time import time


class RequestResponseTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time()
        response = self.get_response(request)
        end = time()
        time_result = str(end - start)
        # print(f'Total time: {end - start}')
        RequestResponseLog.objects.create(path=request.path,
                                          request_method=request.method,
                                          time=time_result)
        return response
