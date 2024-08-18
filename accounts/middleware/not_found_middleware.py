from django.shortcuts import redirect

class NotFoundMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 404 and not request.path.startswith('/not_found/'):
            return redirect('not_found_404')
        elif response.status_code == 403 and not request.path.startswith('/forbidden/'):
            return redirect('forbidden_403')

        return response