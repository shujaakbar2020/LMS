# Generated by Django 2.2.17 on 2021-04-24 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0023_auto_20210424_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='subject',
            field=models.ManyToManyField(to='Management.Subject'),
        ),
    ]
