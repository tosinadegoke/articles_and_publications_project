# Generated by Django 3.0.7 on 2022-06-10 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_auto_20220608_1824'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='context',
            new_name='content',
        ),
    ]
