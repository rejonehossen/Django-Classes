# Generated by Django 5.0.3 on 2024-04-01 03:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentmodel',
            old_name='Address',
            new_name='Department',
        ),
        migrations.RenameField(
            model_name='teachermodel',
            old_name='Address',
            new_name='Department',
        ),
        migrations.RemoveField(
            model_name='studentmodel',
            name='Age',
        ),
        migrations.RemoveField(
            model_name='studentmodel',
            name='Country',
        ),
        migrations.RemoveField(
            model_name='studentmodel',
            name='District',
        ),
        migrations.RemoveField(
            model_name='teachermodel',
            name='Age',
        ),
        migrations.RemoveField(
            model_name='teachermodel',
            name='Country',
        ),
        migrations.RemoveField(
            model_name='teachermodel',
            name='District',
        ),
    ]
