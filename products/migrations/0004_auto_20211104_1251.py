# Generated by Django 3.0.7 on 2021-11-04 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20211104_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='summary',
            field=models.TextField(),
        ),
    ]