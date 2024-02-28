import stripe
import os

stripe.api_key = os.getenv('STRIPE_API_KEY')


def create_product_price(amount, product_name):
    """
    Функция для получения цены продукта.
    """
    product = stripe.Product.create(name=product_name)

    stripe_price = stripe.Price.create(
        currency='rub',
        unit_amount=amount * 100,
        product_data={'name': product},
    )
    return stripe_price


def create_session(price):
    """
    Функция для создания сессии покупки.
    """
    stripe_session = stripe.checkout.Session.create(
        success_url='http://localhost:8000/materials/',
        line_items=[{
            'price': price, 'quantity': 1
        }],
        mode='payment',
    )

    return stripe_session
