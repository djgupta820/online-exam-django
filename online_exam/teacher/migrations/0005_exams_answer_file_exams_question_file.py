# Generated by Django 4.0.4 on 2022-06-02 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0004_t_profile_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='exams',
            name='answer_file',
            field=models.FileField(default='file', upload_to=''),
        ),
        migrations.AddField(
            model_name='exams',
            name='question_file',
            field=models.FileField(default='file', upload_to=''),
        ),
    ]