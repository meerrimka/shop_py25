from django.core.mail import send_mail

def send_activation_code(email, code):
    send_mail(
        'Py25 shop project', # title
        f'http://localhost:8000/account/activate/{code}', # body
        'chirmasheva07@gmail.com', # from
        [email] # to
    )

def send_reset_password_code(email, code):
    send_mail(
        'Py25 shop project', # title
        f'Привет что бы сбросить пароль тебе нужно знать этот код --> {code}', # body
        'chirmasheva07@gmail.com', # from
        [email] # to
    )
