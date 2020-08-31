# Generated by Django 3.0.2 on 2020-08-27 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collectdata', '0005_auto_20200827_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boostangle',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='boost_angle', to='collectdata.UserDetail'),
        ),
        migrations.AlterField(
            model_name='boostangledetail',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='boost_angle_detail', to='collectdata.UserDetail'),
        ),
        migrations.AlterField(
            model_name='bracketed',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bracketed', to='collectdata.UserDetail'),
        ),
        migrations.AlterField(
            model_name='bracketedc',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bracketedc', to='collectdata.UserDetail'),
        ),
        migrations.AlterField(
            model_name='c',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='c', to='collectdata.UserDetail'),
        ),
        migrations.AlterField(
            model_name='condition',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='condition', to='collectdata.UserDetail'),
        ),
        migrations.AlterField(
            model_name='gasgiant',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gas_giant', to='collectdata.UserDetail'),
        ),
        migrations.AlterField(
            model_name='irsupport',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='irsupport', to='collectdata.UserDetail'),
        ),
        migrations.AlterField(
            model_name='moon',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='moon', to='collectdata.UserDetail'),
        ),
        migrations.AlterField(
            model_name='multiplesquare',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='multiple_square', to='collectdata.UserDetail'),
        ),
        migrations.AlterField(
            model_name='opposition',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='opposition', to='collectdata.UserDetail'),
        ),
        migrations.AlterField(
            model_name='sextile',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sextile', to='collectdata.UserDetail'),
        ),
        migrations.AlterField(
            model_name='trine',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trine', to='collectdata.UserDetail'),
        ),
    ]
