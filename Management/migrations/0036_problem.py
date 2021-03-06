# Generated by Django 2.2.17 on 2021-05-12 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0035_auto_20210512_0554'),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problemNumber', models.CharField(max_length=64, null=True)),
                ('problemCategory', models.CharField(max_length=64, null=True)),
                ('problemTitle', models.CharField(max_length=64, null=True)),
                ('problemContent', models.CharField(max_length=64, null=True)),
                ('problemAnswer', models.CharField(max_length=64, null=True)),
                ('studentFeedback', models.CharField(max_length=64, null=True)),
            ],
        ),
    ]
