# Generated by Django 4.1.7 on 2023-03-02 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_order_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery',
            field=models.CharField(blank=True, choices=[('Бесплатная доставка', 'Бесплатная доставка'), ('Платная доставка', 'Платная доставка'), ('Самовывоз', 'Самовывоз')], max_length=50, null=True),
        ),
    ]