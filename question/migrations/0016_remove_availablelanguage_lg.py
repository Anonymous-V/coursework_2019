# Generated by Django 2.1.3 on 2019-01-06 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0015_auto_20190106_1413'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='availablelanguage',
            name='lg',
        ),
    ]
