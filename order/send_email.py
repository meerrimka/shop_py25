from django.core.mail import send_mail


def send_order_confirmations_code(email, code, name, price):
    full_link = f'Привет , подтверди заказ на продукт {name} на сумму {price}\n\n hhtp://localhost:8000/api/v1/order/confirm/{code}'
    send_mail('Order from shop py25',
    full_link,
    'chirmasheva07@gmail.com',
    [email])