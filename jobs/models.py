from django.db import models


class Designer(models.Model):
    designer_name = models.CharField(max_length=100)

    def __str__(self):
        return self.designer_name


class Manufacturer(models.Model):
    manufacturer_name = models.CharField(max_length=100)

    def __str__(self):
        return self.manufacturer_name


class Job(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    designer = models.ForeignKey(Designer, on_delete=models.CASCADE)
    job_client = models.CharField(max_length=300)
    job_description = models.CharField(max_length=500)
    creation_date = models.DateTimeField('creation date', null=True, blank=True)
    start_date = models.DateTimeField('start date', null=True, blank=True)
    completion_date = models.DateTimeField('completion date', null=True, blank=True)
    rejection_date = models.DateTimeField('rejection date', null=True, blank=True)
    is_flagged = models.BooleanField(default=False)
    in_progress = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    rejection_text = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.job_description
