# Generated by Django 4.2.5 on 2024-04-29 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_alter_chefprofile_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chefprofile',
            name='experience',
            field=models.PositiveIntegerField(null=True),
        ),
    ]