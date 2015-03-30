from django.shortcuts import render
from django.http import HttpResponse



def index(request):

    return render(request, 'volunteers/index.html')

def profile(request, username):
    context_dict = {}

    context_dict['user'] = username

    return render (request, 'profile.html', context_dict)

