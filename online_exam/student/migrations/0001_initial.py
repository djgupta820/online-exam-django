# Generated by Django 4.0.4 on 2022-05-29 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='all_students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('roll_number', models.BigIntegerField()),
                ('course', models.CharField(max_length=100)),
                ('semester', models.IntegerField()),
                ('joined', models.DateField()),
                ('registered_at', models.DateTimeField()),
            ],
        ),
    ]
