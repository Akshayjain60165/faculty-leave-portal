# Generated by Django 3.0.5 on 2021-05-08 06:10

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0004_deanapp_dirapp_hodapp'),
    ]

    operations = [
        migrations.CreateModel(
            name='proffesor',
            fields=[
                ('pro_id', models.IntegerField(primary_key=True, serialize=False)),
                ('dept_name', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('emailid', models.EmailField(max_length=254)),
                ('biography', models.TextField()),
                ('linkedin', models.URLField()),
                ('contactnumber', models.CharField(max_length=12)),
                ('courses', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=10), size=2), size=8)),
                ('qualifications', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=10), size=4), size=8)),
            ],
        ),
        migrations.AlterField(
            model_name='appid',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='login_time',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='num_of_leaves',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
