# Generated by Django 5.0.4 on 2024-04-20 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(max_length=50, null=True)),
                ('Address', models.CharField(max_length=50, null=True)),
                ('PhoneNumber', models.CharField(max_length=50, null=True)),
                ('Email', models.CharField(max_length=50, null=True)),
                ('ProfilePicture', models.CharField(max_length=50, null=True)),
                ('CareerObject', models.TextField()),
                ('Degree', models.CharField(max_length=50, null=True)),
                ('Instituiton', models.CharField(max_length=50, null=True)),
                ('GraduationYear', models.CharField(max_length=50, null=True)),
                ('Company', models.CharField(max_length=50, null=True)),
                ('Position', models.CharField(max_length=50, null=True)),
                ('StartDate', models.CharField(max_length=50, null=True)),
                ('EndDate', models.CharField(max_length=50, null=True)),
                ('HardSkills', models.CharField(max_length=50, null=True)),
                ('SoftSkills', models.CharField(max_length=50, null=True)),
                ('Certifications', models.CharField(max_length=50, null=True)),
                ('Projects', models.CharField(max_length=50, null=True)),
                ('Reference', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
