# Generated by Django 3.0.7 on 2021-11-04 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='inStock',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
