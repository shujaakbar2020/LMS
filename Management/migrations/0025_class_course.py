# Generated by Django 2.2.17 on 2021-04-27 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0024_auto_20210424_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='course',
            field=models.ForeignKey(help_text='Select Course for this class', null=True, on_delete=django.db.models.deletion.CASCADE, to='Management.Course'),
        ),
    ]
