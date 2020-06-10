from django.shortcuts import render
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'index.html')

def shouye(request): # 很混乱 一会儿再看
    return HttpResponseRedirect('/enter_article/')

def pp(request):
    return HttpResponseRedirect('/enter_user/pp')

def zpq(request):
    return HttpResponseRedirect('/enter_photo/zpq')

def passage(request):
    return HttpResponseRedirect('/enter_article/')

def pi(request):
    return HttpResponseRedirect('/enter_user/person_info')