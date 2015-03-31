import datetime
from django.utils.text import slugify
from django.core.validators import RegexValidator
from django.db import models





"""TOTO:

Auto-log out admin after certain amount of time?
Make #modelfield text larger
set up scheduled weekly emails for birthdays
"""





class Volunteer(models.Model):

    """--------public---------"""

    forename = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format:'+999999999'. Up to 15 digits allowed.")
    primary_phone = models.CharField(validators=[phone_regex], blank=True, max_length=15)  # validators should be a list
    secondary_phone = models.CharField(validators=[phone_regex], blank=True, max_length=15)

    #emergency contact
    emergency_contact_forename = models.CharField(max_length=128, default="NO FORENAME ENTERED")
    emergency_contact_surname = models.CharField(max_length=128, default="NO SURNAME ENTERED")
    emergency_contact_phone = models.CharField(validators=[phone_regex], blank=True, max_length=15)

    """--------private---------"""

    address = models.TextField(max_length=300, blank=True, default="")
    # reference1
    reference1_forename = models.CharField(max_length=128, blank=True, default="")
    reference1_surname = models.CharField(max_length=128, blank=True, default="")
    reference1_primary_phone = models.CharField(validators=[phone_regex], blank=True, max_length=15)
    reference1_secondary_phone = models.CharField(validators=[phone_regex], blank=True, max_length=15)
    reference1_email = models.EmailField(blank=True, default="")
    reference1_sent = models.BooleanField(default=False)
    reference1_received = models.BooleanField(default=False)

    # reference2
    reference2_forename = models.CharField(max_length=128, blank=True, default="")
    reference2_surname = models.CharField(max_length=128, blank=True, default="")
    reference2_primary_phone = models.CharField(validators=[phone_regex], blank=True, max_length=15)
    reference2_secondary_phone = models.CharField(validators=[phone_regex], blank=True, max_length=15)
    reference2_email = models.EmailField(blank=True, default="")
    reference2_sent = models.BooleanField(default=False)
    reference2_received = models.BooleanField(default=False)

    start_date = models.DateField(blank=True, default=datetime.date.today())
    birthday = models.DateField()
    risk_assessment = models.BooleanField(default=False)
    health_and_safety = models.BooleanField(default=False)
    parental_permission = models.BooleanField(default=False)  #do they want a charfield for description/comments?
    permission_to_work = models.BooleanField(default=False)  #do they want a charfield for description/comments?
    till = models.BooleanField(default=False)
    open_shop = models.BooleanField(default=False)
    close_shop = models.BooleanField(default=False)


    def save(self, *args, **kwargs):
        super(Volunteer, self).save(*args, **kwargs)


    def __unicode__(self):
        return self.forename + ' ' + self.surname
        #make sure to modify admin so it shows column with birthday and date joined

