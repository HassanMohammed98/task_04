# Generated by Django 2.2.13 on 2022-04-18 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Article',
            new_name='Restaurant',
        ),
    ]
