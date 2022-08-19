# Generated by Django 4.0.5 on 2022-08-16 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_students_phone1_alter_students_phone2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='cgpi',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='diploma_board',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='email_id2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='perc',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='phone1',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='phone2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='sem3',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='sem4',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='sem5',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='sem6',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='tenth_perc',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='tenth_year',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='twelth_perc',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='twelth_year',
            field=models.IntegerField(null=True),
        ),
    ]
