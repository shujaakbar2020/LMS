# Generated by Django 2.2.17 on 2021-05-11 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0031_auto_20210511_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='birthDate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='emailAddress',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='homeAddress',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='mobilePhone',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='postCode',
            field=models.CharField(max_length=64, null=True),
        ),
    ]