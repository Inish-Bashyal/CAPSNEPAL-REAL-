# Generated by Django 4.0.5 on 2022-07-24 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caps', '0005_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.FloatField(),
        ),
    ]
