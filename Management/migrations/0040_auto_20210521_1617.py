# Generated by Django 2.2.17 on 2021-05-21 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0039_auto_20210521_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elective',
            name='courseNumber',
            field=models.ManyToManyField(to='Management.Course'),
        ),
        migrations.AlterField(
            model_name='elective',
            name='studentNumber',
            field=models.ManyToManyField(to='Management.Student'),
        ),
        migrations.AlterField(
            model_name='teach',
            name='courseNumber',
            field=models.ManyToManyField(to='Management.Course'),
        ),
        migrations.AlterField(
            model_name='teach',
            name='teacherNumber',
            field=models.ManyToManyField(to='Management.Teacher'),
        ),
    ]