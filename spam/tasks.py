from django.core.mail import send_mail
from celery import shared_task
from spam.models import Contact
@shared_task
def send_spam():
    emails = [i for i in Contact.objects.all()]
    send_mail(
        'Py25 shop project', # title
        f'прримрми', # body
        'chirmasheva07@gmail.com', # from
        [emails] # to
    )
