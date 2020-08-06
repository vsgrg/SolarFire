# Generated by Django 3.0.2 on 2020-08-06 08:57

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=30, null=True)),
                ('symbol', models.IntegerField(null=True)),
                ('body1', models.CharField(max_length=30, null=True)),
                ('degree', models.CharField(max_length=10, null=True)),
                ('degree_type', models.CharField(max_length=10, null=True)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='collectdata.UserDetail')),
            ],
        ),
        migrations.CreateModel(
            name='Sextile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=30, null=True)),
                ('symbol', models.IntegerField(null=True)),
                ('body1', models.CharField(max_length=30, null=True)),
                ('degree', models.CharField(max_length=10, null=True)),
                ('degree_type', models.CharField(max_length=10, null=True)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='collectdata.UserDetail')),
            ],
        ),
        migrations.CreateModel(
            name='Opposition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body1', models.CharField(max_length=30, null=True)),
                ('symbol', models.IntegerField(null=True)),
                ('body2', models.CharField(max_length=30, null=True)),
                ('degree', models.CharField(max_length=30, null=True)),
                ('degree_type', models.CharField(max_length=30, null=True)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='collectdata.UserDetail')),
            ],
        ),
        migrations.CreateModel(
            name='MultipleSquare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=30, null=True)),
                ('symbol', models.IntegerField(null=True)),
                ('degree', models.CharField(max_length=30, null=True)),
                ('degree_type', models.CharField(max_length=10, null=True)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='collectdata.UserDetail')),
            ],
        ),
        migrations.CreateModel(
            name='Moon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sym', models.IntegerField(null=True)),
                ('body', models.CharField(max_length=30, null=True)),
                ('degree', models.CharField(max_length=10, null=True)),
                ('degree_type', models.CharField(max_length=10, null=True)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='collectdata.UserDetail')),
            ],
        ),
        migrations.CreateModel(
            name='Irsupport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=10, null=True)),
                ('degree', models.CharField(max_length=10, null=True)),
                ('sym', models.IntegerField(null=True)),
                ('degree_type', models.CharField(max_length=10, null=True)),
                ('body1', models.CharField(max_length=10, null=True)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='collectdata.UserDetail')),
            ],
        ),
        migrations.CreateModel(
            name='Gasgiant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gas', models.CharField(max_length=10, null=True)),
                ('symbol', models.IntegerField(null=True)),
                ('body', models.CharField(max_length=10, null=True)),
                ('degree', models.CharField(max_length=10, null=True)),
                ('degree_type', models.CharField(max_length=10, null=True)),
                ('energy', models.CharField(max_length=10, null=True)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='collectdata.UserDetail')),
            ],
        ),
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conditionbody', models.CharField(max_length=10, null=True)),
                ('first_condition', models.CharField(max_length=10, null=True)),
                ('degree', models.CharField(max_length=10, null=True)),
                ('degree_type', models.CharField(max_length=10, null=True)),
                ('energy', models.CharField(max_length=10, null=True)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='collectdata.UserDetail')),
            ],
        ),
        migrations.CreateModel(
            name='C',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=30, null=True)),
                ('symbol', models.IntegerField(null=True)),
                ('body1', models.CharField(max_length=30, null=True)),
                ('degree', models.CharField(max_length=10, null=True)),
                ('degree_type', models.CharField(max_length=10, null=True)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='collectdata.UserDetail')),
            ],
        ),
        migrations.CreateModel(
            name='BracketedC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=30, null=True)),
                ('symbol', models.IntegerField(null=True)),
                ('body1', models.CharField(max_length=30, null=True)),
                ('degree', models.CharField(max_length=10, null=True)),
                ('degree_type', models.CharField(max_length=10, null=True)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='collectdata.UserDetail')),
            ],
        ),
        migrations.CreateModel(
            name='Bracketed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bracket', models.CharField(max_length=30, null=True)),
                ('body', models.CharField(max_length=30, null=True)),
                ('degree_type', models.CharField(max_length=10, null=True)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='collectdata.UserDetail')),
            ],
        ),
        migrations.CreateModel(
            name='BoostAngleDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boostanglebody', models.CharField(max_length=10, null=True)),
                ('body', models.CharField(max_length=10, null=True)),
                ('boost_symbol', models.IntegerField(null=True)),
                ('body1', models.CharField(max_length=10, null=True)),
                ('degree', models.CharField(max_length=10, null=True)),
                ('degree_type', models.CharField(max_length=10, null=True)),
                ('energy', models.CharField(max_length=10, null=True)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='collectdata.UserDetail')),
            ],
        ),
        migrations.CreateModel(
            name='BoostAngle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boostanglebody', models.CharField(max_length=10, null=True)),
                ('body', models.CharField(max_length=10, null=True)),
                ('degree', models.CharField(max_length=10, null=True)),
                ('degree_type', models.CharField(max_length=10, null=True)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='collectdata.UserDetail')),
            ],
        ),
        migrations.CreateModel(
            name='Basicdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('start_time', models.TimeField(null=True)),
                ('stop_time', models.TimeField(null=True)),
                ('total_time', models.TimeField(null=True)),
                ('first_perception', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('last_perception', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('total_drawing', models.IntegerField(null=True)),
                ('correct', models.CharField(max_length=30, null=True)),
                ('displaced', models.CharField(max_length=30, null=True)),
                ('total_meld', models.CharField(max_length=30, null=True)),
                ('correct_meld', models.CharField(max_length=30, null=True)),
                ('incorect_meld', models.CharField(max_length=30, null=True)),
                ('type', models.CharField(max_length=30, null=True)),
                ('opp', models.CharField(max_length=10, null=True)),
                ('multiple_opposition', models.CharField(max_length=10, null=True)),
                ('bracketedIROR', models.CharField(max_length=10, null=True)),
                ('giantsquare', models.CharField(max_length=10, null=True)),
                ('house', models.IntegerField(null=True)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='collectdata.UserDetail')),
            ],
        ),
    ]
