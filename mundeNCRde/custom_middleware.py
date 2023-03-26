def custom_middleware(get_request):
    def middleware(request):
        print(f'Request performed for {request.user}')
        r = get_request(request)
        print(f'Request performed after {request.user}')
        return r
    return middleware