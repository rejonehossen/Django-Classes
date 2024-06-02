# Generated by Django 5.0.4 on 2024-05-02 05:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_recruiterprofile_seekerprofile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recruiterprofile',
            old_name='company',
            new_name='company_description',
        ),
        migrations.RenameField(
            model_name='recruiterprofile',
            old_name='required_employee',
            new_name='company_name',
        ),
        migrations.AlterField(
            model_name='recruiterprofile',
            name='myuser',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='RecruiterProfile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='seekerprofile',
            name='myuser',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='SeekerProfile', to=settings.AUTH_USER_MODEL),
        ),
    ]
