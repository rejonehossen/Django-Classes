# Generated by Django 4.2.5 on 2024-03-25 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_remove_studentmodel_name_remove_studentmodel_roll_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='doctormodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=50, null=True)),
                ('LastName', models.CharField(max_length=50, null=True)),
                ('Age', models.CharField(max_length=50, null=True)),
                ('City', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='table4model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=50, null=True)),
                ('LastName', models.CharField(max_length=50, null=True)),
                ('Department', models.CharField(max_length=50, null=True)),
                ('City', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='table5model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=50, null=True)),
                ('LastName', models.CharField(max_length=50, null=True)),
                ('Department', models.CharField(max_length=50, null=True)),
                ('City', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='teachermodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=50, null=True)),
                ('LastName', models.CharField(max_length=50, null=True)),
                ('Department', models.CharField(max_length=50, null=True)),
                ('City', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
