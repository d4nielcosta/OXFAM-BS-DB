from django.shortcuts import render
from django.http import HttpResponse
from models import Volunteer


def index(request):
    context_dict = {}

    volunteers = Volunteer.objects.filter().order_by('-forename')
    print volunteers
    context_dict['volunteers'] = volunteers

    return render(request, 'volunteers/index.html', context_dict)

def profile(request, username):
    context_dict = {}

    context_dict['user'] = username

    return render (request, 'profile.html', context_dict)

