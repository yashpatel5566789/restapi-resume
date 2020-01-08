# Generated by Django 3.0.2 on 2020-01-08 17:13

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_countries.fields
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
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
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(blank=True, max_length=255)),
                ('company', models.CharField(blank=True, max_length=255)),
                ('city', models.CharField(blank=True, max_length=255)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('achievements', tinymce.models.HTMLField(blank=True)),
                ('resume', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='restapi.Resume')),
            ],
            options={
                'verbose_name_plural': 'Work Experience',
                'ordering': ['-end_date'],
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('competency', models.IntegerField(blank=True, null=True)),
                ('resume', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='restapi.Resume')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(blank=True, max_length=255)),
                ('phone_number', models.CharField(blank=True, max_length=255)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('address2', models.CharField(blank=True, max_length=255)),
                ('city', models.CharField(blank=True, max_length=255)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2)),
                ('linked_in', models.CharField(blank=True, max_length=255)),
                ('objective', tinymce.models.HTMLField(blank=True)),
                ('sub_expires_on', models.DateTimeField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('competency', models.IntegerField(blank=True, null=True)),
                ('resume', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='restapi.Resume')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(blank=True, max_length=255)),
                ('degree', models.CharField(blank=True, max_length=255)),
                ('major', models.CharField(blank=True, max_length=255)),
                ('gpa', models.FloatField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=255)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('resume', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='restapi.Resume')),
            ],
            options={
                'verbose_name_plural': 'Education',
                'ordering': ['-end_date'],
            },
        ),
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('date_obtained', models.DateField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=255)),
                ('resume', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='restapi.Resume')),
            ],
            options={
                'ordering': ['-date_obtained'],
            },
        ),
    ]
