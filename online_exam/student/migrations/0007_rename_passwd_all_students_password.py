# Generated by Django 4.0.4 on 2022-06-03 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_all_students_passwd'),
    ]

    operations = [
        migrations.RenameField(
            model_name='all_students',
            old_name='passwd',
            new_name='password',
        ),
    ]
