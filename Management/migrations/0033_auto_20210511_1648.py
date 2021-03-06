# Generated by Django 2.2.17 on 2021-05-11 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0032_auto_20210511_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='courseCredit',
            field=models.DecimalField(decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='courseDescription',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='courseName',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='courseNature',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='experimentHours',
            field=models.SmallIntegerField(max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='theoreticalHours',
            field=models.SmallIntegerField(max_length=2, null=True),
        ),
    ]
