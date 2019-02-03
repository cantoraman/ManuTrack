from django.db import models


class Designer(models.Model):
    designer_name = models.CharField(max_length=100)


class Manufacturer(models.Model):
    manufacturer_name = models.CharField(max_length=100)


class Job(models.Model):
    designer = models.ForeignKey(Designer, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL)
    job_client = models.CharField(max_length=300)
    job_description = models.CharField(max_length=500)
    creation_date = models.DateTimeField('creation date')
    start_date = models.DateTimeField('start date')
    completion_date = models.DateTimeField('completion date')
    rejection_date = models.DateTimeField('rejection date')
    is_flagged = models.BooleanField(default=False)
    in_progress = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    rejection_text = models.TextField(max_length=500)

