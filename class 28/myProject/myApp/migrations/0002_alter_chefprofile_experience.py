# Generated by Django 4.2.5 on 2024-04-29 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chefprofile',
            name='experience',
            field=models.PositiveBigIntegerField(max_length=100, null=True),
        ),
    ]
