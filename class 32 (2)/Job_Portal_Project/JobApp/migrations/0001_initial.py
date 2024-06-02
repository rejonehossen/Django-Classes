# Generated by Django 5.0.4 on 2024-05-06 03:34

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='customuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('age', models.CharField(max_length=100, null=True)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('other', 'other')], max_length=100, null=True)),
                ('blood', models.CharField(choices=[('a', 'a'), ('ab', 'ab'), ('b', 'b'), ('o', 'o')], max_length=100, null=True)),
                ('usertype', models.CharField(choices=[('jobrecruiter', 'jobrecruiter'), ('jobseeker', 'jobseeker'), ('viewer', 'viewer')], max_length=100, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('country', models.CharField(max_length=100, null=True)),
                ('profile_photo', models.ImageField(upload_to='profilephoto')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='work_experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('start', models.CharField(max_length=100)),
                ('end', models.CharField(max_length=100)),
                ('myuser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Work_Experience', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='seekerprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification', models.CharField(max_length=100, null=True)),
                ('experience', models.CharField(max_length=100, null=True)),
                ('skills', models.CharField(max_length=100, null=True)),
                ('myuser', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='SeekerProfile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='recruiterprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100, null=True)),
                ('company_location', models.CharField(max_length=100, null=True)),
                ('recruiter_name', models.CharField(max_length=100, null=True)),
                ('myuser', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='RecruiterProfile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='educational_qualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=100)),
                ('institution', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
                ('myuser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Educational_Qualification', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=100)),
                ('emergnecy_contact', models.CharField(max_length=100)),
                ('myuser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Contact', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='basicinformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fathername', models.CharField(max_length=100, null=True)),
                ('mothername', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('myuser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='BasicInformation', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='addjob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=100, null=True)),
                ('job_description', models.CharField(max_length=100, null=True)),
                ('job_location', models.CharField(max_length=100, null=True)),
                ('deadline', models.CharField(max_length=100, null=True)),
                ('company_logo', models.ImageField(null=True, upload_to='jobpic')),
                ('requirements', models.CharField(max_length=100, null=True)),
                ('qualifications', models.CharField(max_length=100, null=True)),
                ('job_types', models.CharField(choices=[('fulltime', 'full_time'), ('parttime', 'part_time')], max_length=100, null=True)),
                ('workplace', models.CharField(choices=[('remote', 'remote'), ('onsite', 'on_site')], max_length=100, null=True)),
                ('salary', models.CharField(max_length=100, null=True)),
                ('experience', models.CharField(max_length=100, null=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
