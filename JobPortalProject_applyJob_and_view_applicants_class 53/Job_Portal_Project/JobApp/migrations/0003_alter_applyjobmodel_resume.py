# Generated by Django 5.0.6 on 2024-06-01 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobApp', '0002_applyjobmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applyjobmodel',
            name='resume',
            field=models.FileField(null=True, upload_to='static/resume'),
        ),
    ]