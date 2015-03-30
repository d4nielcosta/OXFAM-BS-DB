__author__ = 'joshuamarsh'
from django.core.validators import RegexValidator
from django.db import models



class Volunteer(models.Model):
    #public
    forename = models.CharField(max_length=128, default="NO FORENAME ENTERED")
    surname = models.CharField(max_length=128, default="NO SURNAME ENTERED")
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format:'+999999999'. Up to 15 digits allowed.")
    primary_phone = models.CharField(validators=[phone_regex], blank=True, max_length=15) # validators should be a list
    secondary_phone = models.CharField(validators=[phone_regex], blank=True, max_length=15)
    emergency_contact_forename = models.CharField(max_length=128, default="NO FORENAME ENTERED")
    emergency_contact_surname = models.CharField(max_length=128, default="NO SURNAME ENTERED")
    emergency_contact_phone = models.CharField(validators=[phone_regex], blank=True, max_length=15)
    #private
    start_date = models.DateField(blank=True)
    birthday = models.DateField(blank=True)
    #R.A.?
    parental_permission = models.BooleanField(default=False)#do they want a charfield for description/comments?
    permission_to_work = models.BooleanField(default=False)#do they want a charfield for description/comments?
    till = models.BooleanField(default=False)
    open_shop = models.BooleanField(default=False)
    close_shop = models.BooleanField(default=False)

class Reference(models.Model):
    volunteer = models.ForeignKey(Volunteer, related_name='reference')
    forename = models.CharField(max_length=128, default="NO FORENAME ENTERED")
    surname = models.CharField(max_length=128, default="NO SURNAME ENTERED")
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    primary_phone = models.CharField(validators=[phone_regex], blank=True, max_length=15) # validators should be a list
    secondary_phone = models.CharField(validators=[phone_regex], blank=True, max_length=15)
