# Generated by Django 2.2.17 on 2021-04-24 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0014_auto_20210424_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='students',
            field=models.ManyToManyField(help_text='Select students for this class', to='Management.Student'),
        ),
    ]
