from datetime import datetime, timedelta

from django.shortcuts import render, redirect
from models import Volunteer



def index(request):

    """TODO: Add option to filter by forename or surname and add search. """
    context_dict = {}
    volunteers = Volunteer.objects.filter().order_by('forename')
    context_dict['volunteers'] = volunteers

    return render(request, 'volunteers/index.html', context_dict)

def profile(request, volunteer_id):

    context_dict = {}






    volunteer = Volunteer.objects.get(id=volunteer_id)
    context_dict['forname'] = volunteer.forename
    context_dict['surname'] = volunteer.surname
    context_dict['primary_phone'] = volunteer.primary_phone
    context_dict['secondary_phone'] = volunteer.secondary_phone

    context_dict['emergency_contact_forename'] = volunteer.emergency_contact_forename
    context_dict['emergency_contact_surname'] = volunteer.emergency_contact_surname
    context_dict['emergency_contact_phone'] = volunteer.emergency_contact_phone

    context_dict['reference1_forename'] = volunteer.reference1_forename
    context_dict['reference1_surname'] = volunteer.reference1_surname
    context_dict['reference1_primary_phone'] = volunteer.reference1_primary_phone
    context_dict['reference1_secondary_phone'] = volunteer.reference1_secondary_phone

    context_dict['reference2_forename'] = volunteer.reference2_forename
    context_dict['reference2_surname'] = volunteer.reference2_surname
    context_dict['reference2_primary_phone'] = volunteer.reference2_primary_phone
    context_dict['reference2_secondary_phone'] = volunteer.reference2_secondary_phone

    context_dict['start_date'] = volunteer.start_date
    context_dict['birthday'] = volunteer.birthday

    context_dict['parental_permission'] = volunteer.parental_permission
    context_dict['permission_to_work'] = volunteer.permission_to_work
    context_dict['till'] = volunteer.till
    context_dict['open_shop'] = volunteer.open_shop
    context_dict['close_shop'] = volunteer.close_shop

    context_dict['age'] = datetime.today().year - volunteer.birthday.year




    return render (request, 'volunteers/profile.html', context_dict)
