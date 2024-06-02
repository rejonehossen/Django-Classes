# Generated by Django 5.0.6 on 2024-06-01 05:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='applyjobmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills', models.CharField(max_length=100, null=True)),
                ('resume', models.FileField(null=True, upload_to='static/jobapply')),
                ('applied_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('apply_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='JobApp.addjob')),
            ],
        ),
    ]