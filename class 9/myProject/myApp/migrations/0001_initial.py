# Generated by Django 5.0.3 on 2024-03-25 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='studentmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Roll', models.CharField(max_length=50)),
                ('City', models.CharField(max_length=90)),
            ],
        ),
    ]
