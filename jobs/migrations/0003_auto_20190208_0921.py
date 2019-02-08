# Generated by Django 2.1.5 on 2019-02-08 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20190208_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='completion_date',
            field=models.DateTimeField(null=True, verbose_name='completion date'),
        ),
        migrations.AlterField(
            model_name='job',
            name='rejection_date',
            field=models.DateTimeField(null=True, verbose_name='rejection date'),
        ),
        migrations.AlterField(
            model_name='job',
            name='start_date',
            field=models.DateTimeField(null=True, verbose_name='start date'),
        ),
    ]
