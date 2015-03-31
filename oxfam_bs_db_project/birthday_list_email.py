import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oxfam_bs_db_project.settings')

from datetime import datetime, timedelta
import smtplib
from volunteers.models import Volunteer

import django
django.setup()


def send_email():

    birthday_volunteers = Volunteer.objects.filter(birthday__in=[datetime.today() + timedelta(days=i) for i in range(1,8)])
    names = ""

    if birthday_volunteers:
        for vol in birthday_volunteers:
            names += '          ' + vol.forename + ' ' + vol.surname + '\n\n'
    else:
        names = "No birthdays this week."



    content = """SUBJECT:Weekly Birthday List
    \n\nHello from your website,\n\nHere is the list of volunteers whose birthdays are this week:\n\n\n%s\nRegards,\n\n\nYour Website


    """ % (names)

    username = 'crazybioguy'
    password = '12ooottafagvSH'
    from_address = 'crazybioguy@gmail.com'
    to_address = 'crazybioguy@gmail.com'

    try:
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login(username, password)
        mail.sendmail(from_address, to_address, content)
        mail.close()
    except:
        print "**********Exception while trying to send birthday list email on " + datetime.today().isoformat() + "**********"


if __name__ == '__main__':
    print "Starting Oxfam Volunteers email script..."
    send_email()