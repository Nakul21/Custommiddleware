from django.utils import timezone
class ProcessTimeMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.process_request(request)
        response = self.get_response(request)
        response = self.process_response(request, response)
        return response

    def process_request(self, request):
        request.start_time = timezone.now()

    def process_response(self, request, response):
        end_time = timezone.now() - request.start_time
        print(f'Execution time {end_time}')
        return response





