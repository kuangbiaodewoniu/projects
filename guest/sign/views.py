from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required


def index(request):
    # return HttpResponse('Hello django!')
    return render(request, 'index.html')


def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            response = HttpResponseRedirect('/event_manage/')
            request.session['user'] = username
            # response.set_cookie('user', username, 3600)
            return response
            # return HttpResponseRedirect('/event_manage/')
        else:
            return render(request, 'index.html', {'error': '用户名或者密码错误!'})
    else:
        return render(request, 'index.html')


@login_required
def event_manage(request):
    # username = request.COOKIES.get('user', '')
    username = request.session.get('user', '')
    return render(request, 'event_manage.html', {'username': username})