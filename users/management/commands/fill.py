from django.core.management import BaseCommand

from users.models import Payment


class Command(BaseCommand):
    """
    Класс для заполнения данных о платеже.
    """

    def handle(self, *args, **options):
        payments_list = [
            {'course': 1, 'method': 'Наличные', 'date_of_payment': '2024-02-09T18:34:06.502510Z'},
            {'lesson': 4, 'method': 'Перевод', 'date_of_payment': '2024-02-09T16:34:06.502510Z'},
            {'course': 2, 'method': 'Перевод', 'date_of_payment': '2024-02-08T16:34:06.502510Z'},
            {'lesson': 5, 'method': 'Перевод', 'date_of_payment': '2024-02-08T15:34:06.502510Z'},
            {'course': 2, 'method': 'Наличные', 'date_of_payment': '2024-02-09T15:55:06.502510Z'},
            {'lesson': 7, 'method': 'Наличные', 'date_of_payment': '2024-02-09T20:00:06.502510Z'},
        ]

        payment_for_create = []
        for payment in payments_list:
            payment_for_create.append(
                Payment(**payment)
            )
        print(payment_for_create)
        #Payment.objects.bulk_create(payment_for_create)
