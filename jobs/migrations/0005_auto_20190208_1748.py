# Generated by Django 2.1.5 on 2019-02-08 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20190208_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_client',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
