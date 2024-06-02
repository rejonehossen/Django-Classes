# Generated by Django 5.0.3 on 2024-04-02 02:46

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
                ('FirstName', models.CharField(max_length=100)),
                ('LastName', models.CharField(max_length=100)),
                ('Age', models.CharField(max_length=100)),
                ('City', models.CharField(max_length=100)),
                ('Image', models.ImageField(upload_to='student_pic')),
            ],
        ),
        migrations.CreateModel(
            name='teachermodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=100)),
                ('LastName', models.CharField(max_length=100)),
                ('Age', models.CharField(max_length=100)),
                ('City', models.CharField(max_length=100)),
                ('Image', models.ImageField(upload_to='teacher_pic')),
            ],
        ),
    ]