# Generated by Django 3.2 on 2021-04-17 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='app_status',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='cse_dep',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('pro_id', models.IntegerField()),
                ('datefrom', models.DateField()),
                ('dateto', models.DateField()),
                ('num_of_days', models.IntegerField()),
                ('reason', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='cse_hod',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('comm', models.TextField(blank=True)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='cur_running',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('pro_id', models.IntegerField()),
                ('datefrom', models.DateField()),
                ('dateto', models.DateField()),
                ('num_of_days', models.IntegerField()),
                ('reason', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='dean',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('comm', models.TextField(blank=True)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='director',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('comm', models.TextField(blank=True)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ee_dep',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('pro_id', models.IntegerField()),
                ('datefrom', models.DateField()),
                ('dateto', models.DateField()),
                ('num_of_days', models.IntegerField()),
                ('reason', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ee_hod',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('comm', models.TextField(blank=True)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='hod_dean',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('pro_id', models.IntegerField()),
                ('datefrom', models.DateField()),
                ('dateto', models.DateField()),
                ('num_of_days', models.IntegerField()),
                ('reason', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='hoddean',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('pro_id', models.IntegerField()),
                ('datefrom', models.DateField()),
                ('dateto', models.DateField()),
                ('num_of_days', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='login_table',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('dept_name', models.CharField(max_length=6)),
                ('pos', models.CharField(max_length=10)),
                ('curr_pos', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='login_time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_id', models.IntegerField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='mec_dep',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('pro_id', models.IntegerField()),
                ('datefrom', models.DateField()),
                ('dateto', models.DateField()),
                ('num_of_days', models.IntegerField()),
                ('reason', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='mec_hod',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('comm', models.TextField(blank=True)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='num_of_leaves',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_id', models.IntegerField()),
                ('leaves', models.IntegerField()),
            ],
        ),
    ]
