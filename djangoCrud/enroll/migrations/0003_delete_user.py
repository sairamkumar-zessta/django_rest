# Generated by Django 4.1 on 2022-09-24 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0002_remove_user_email_remove_user_password'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
