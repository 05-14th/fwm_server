# middleware.py

from django.conf import settings

def cors_middleware(get_response):
    def middleware(request):
        response = get_response(request)
        response['Access-Control-Allow-Origin'] = '*'  # Allow requests from any origin
        response['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept'
        return response
    return middleware
