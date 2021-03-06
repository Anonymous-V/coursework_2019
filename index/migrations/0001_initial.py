# Generated by Django 2.1.3 on 2018-12-20 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Socials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vk', models.URLField(blank=True, verbose_name='Vkontakte')),
                ('instagram', models.URLField(blank=True, verbose_name='Instagram')),
                ('facebook', models.URLField(blank=True, verbose_name='Facebook')),
                ('twitter', models.URLField(blank=True, verbose_name='Twitter')),
                ('google_plus', models.URLField(blank=True, verbose_name='Google+')),
                ('youtube', models.URLField(blank=True, verbose_name='Youtube')),
                ('whatsapp', models.URLField(blank=True, verbose_name='WhatsApp')),
            ],
            options={
                'verbose_name': 'Социальные сети',
                'db_table': 'socials',
            },
        ),
    ]
