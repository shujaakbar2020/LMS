# Generated by Django 2.2.17 on 2021-05-12 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0033_auto_20210511_1648'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='first_name',
            new_name='collegeName',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='last_name',
            new_name='finalDegree',
        ),
        migrations.AddField(
            model_name='teacher',
            name='finalEducation',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='graduationSchool',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='graduationTime',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='jobResume',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='teacher',
            name='mobilePhone',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='professionalName',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='teacherName',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='teacherNumber',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='technicalTitle',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
