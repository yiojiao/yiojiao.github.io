from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    if 'user' not in request.COOKIES:
        response = render(request, 'myapp/index.html', {'message': 'Hi U1243054'})
        response.set_cookie("user", "U1243054")
        return response
    else:
        return render(request, 'myapp/index.html', {'message': '歡迎回來, U1243054'})
