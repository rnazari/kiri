# Generated by Django 2.0.2 on 2018-02-22 21:05

import api.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='APIToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.UUIDField(default=uuid.uuid4, help_text='Token value', unique=True, verbose_name='Token value')),
                ('expires_on', models.DateTimeField(default=api.models.one_year_away, help_text='Expiration datetime', verbose_name='Expiration datetime')),
                ('application', models.CharField(help_text='App name', max_length=128, verbose_name='App name')),
                ('owner', models.ForeignKey(help_text='Owner', on_delete=django.db.models.deletion.CASCADE, related_name='users_set', to=settings.AUTH_USER_MODEL, verbose_name='Owner')),
            ],
        ),
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name', max_length=64, verbose_name='Name')),
                ('surname', models.CharField(help_text='Surname', max_length=64, verbose_name='Surname')),
                ('birth_date', models.DateField(help_text='Birth date', verbose_name='Birth date')),
                ('birth_place', models.CharField(help_text='Birth place', max_length=64, verbose_name='Birth place')),
                ('address', models.TextField(help_text='Address', max_length=256, verbose_name='Address')),
                ('email', models.EmailField(help_text='Email address', max_length=254, verbose_name='Email address')),
                ('telephone', models.CharField(help_text='Phone number', max_length=32, verbose_name='Phone number')),
                ('website', models.URLField(blank=True, help_text='Website URL', null=True, verbose_name='Website URL')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cvs_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='School name', max_length=64, verbose_name='School name')),
                ('kind', models.CharField(choices=[('Elementary school', 'Elementary school'), ('Middle school', 'Middle school'), ('High school', 'High school'), ('University/College', 'University/College'), ('Ph.D./Master', 'Ph.D./Master')], default='High school', help_text='School kind', max_length=64, verbose_name='School kind')),
                ('address', models.TextField(help_text='School address', max_length=256, verbose_name='School address')),
                ('start_date', models.DateField(help_text='Start date', verbose_name='Start date')),
                ('end_date', models.DateField(blank=True, help_text='End date', null=True, verbose_name='End date')),
                ('final_mark', models.TextField(blank=True, help_text='School assessment', max_length=512, null=True, verbose_name='School final assessment')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(help_text='Skill', max_length=128, verbose_name='Skill')),
                ('level', models.IntegerField(default=3, help_text='Level of expertise', validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)], verbose_name='Level of expertise')),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.TextField(help_text='Company name', max_length=128, verbose_name='Company name')),
                ('headline', models.TextField(help_text='Job headline', max_length=128, null=True, verbose_name='Job headline')),
                ('start_date', models.DateField(help_text='Start date', verbose_name='Start date')),
                ('end_date', models.DateField(blank=True, help_text='End date', null=True, verbose_name='End date')),
                ('description', models.TextField(help_text='Job description', max_length=1024, verbose_name='Job description')),
            ],
        ),
        migrations.AddField(
            model_name='curriculum',
            name='schools',
            field=models.ManyToManyField(blank=True, related_name='attended_schools', to='api.School', verbose_name='Attended schools'),
        ),
        migrations.AddField(
            model_name='curriculum',
            name='skills',
            field=models.ManyToManyField(blank=True, related_name='skills_owned', to='api.Skill', verbose_name='Skills owned'),
        ),
        migrations.AddField(
            model_name='curriculum',
            name='work_experiences',
            field=models.ManyToManyField(blank=True, related_name='previous_work_experiences', to='api.WorkExperience', verbose_name='Previous work experiences'),
        ),
    ]
