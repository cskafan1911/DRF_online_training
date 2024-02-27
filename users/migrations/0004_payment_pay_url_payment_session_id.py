# Generated by Django 4.2.7 on 2024-02-27 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='pay_url',
            field=models.URLField(blank=True, max_length=500, null=True, verbose_name='Ссылка для оплаты'),
        ),
        migrations.AddField(
            model_name='payment',
            name='session_id',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Номер сессии'),
        ),
    ]
