# Generated by Django 2.1.3 on 2018-12-29 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0006_auto_20181227_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
