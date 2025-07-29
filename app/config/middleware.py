from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin

class authMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if not request.user.is_authenticated and request.path != '/user/login/' and request.path != '/user/signup/':
            return HttpResponseRedirect('/user/login/')
        return response
