# Generated by Django 4.2.5 on 2024-04-29 07:02

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


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
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=100, null=True)),
                ('usertype', models.CharField(choices=[('chef', 'Chef'), ('viewer', 'viewer'), ('owner', 'Owner')], max_length=100, null=True)),
                ('Age', models.CharField(max_length=100, null=True)),
                ('City', models.CharField(max_length=100, null=True)),
                ('Country', models.CharField(max_length=100, null=True)),
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
            name='viewerprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest', models.CharField(max_length=100, null=True)),
                ('profilepicture', models.ImageField(null=True, upload_to='static/picture/profile/viewer')),
                ('myuser', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='recipemodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RecipeTitle', models.CharField(max_length=100, null=True)),
                ('Ingredients', models.CharField(max_length=100, null=True)),
                ('Instructions', models.CharField(max_length=100, null=True)),
                ('PreparationTime', models.CharField(max_length=100, null=True)),
                ('CookingTime', models.CharField(max_length=100, null=True)),
                ('TotalTime', models.CharField(max_length=100, null=True)),
                ('NutritionlaInformation', models.CharField(max_length=100, null=True)),
                ('SampleRecipeImage', models.ImageField(null=True, upload_to='static/pic/recipepicture')),
                ('RecipeCategory', models.CharField(choices=[('break_fast', 'Break_Fast'), ('lunch', 'Lunch'), ('dinner', 'Dinner')], max_length=100, null=True)),
                ('DifficultyLevel', models.CharField(choices=[('ealy_', 'Easy_'), ('medium_', 'Medium_'), ('hard_', 'Hard_')], max_length=100, null=True)),
                ('Tags', models.CharField(choices=[('vegetarian', 'Vegetarian'), ('nonvegetarian', 'Non_Vegetarian')], max_length=100, null=True)),
                ('TotalCalorie', models.CharField(max_length=100, null=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='chefprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience', models.CharField(max_length=100, null=True)),
                ('skills', models.CharField(max_length=100, null=True)),
                ('resumelatter', models.CharField(max_length=100, null=True)),
                ('profilepicture', models.ImageField(null=True, upload_to='static/picture/profile/chef')),
                ('myuser', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
