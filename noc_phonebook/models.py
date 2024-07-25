from django.db import models

# Create your models here.
class so_tbl(models.Model):
    so_firstname = models.CharField(max_length=255)
    so_lastname = models.CharField(max_length=255)
    so_phone = models.IntegerField()
    so_department = models.CharField(max_length=255,null=True)
    so_description = models.TextField(null=True)


class department_tbl(models.Model):
    de_name=models.CharField(max_length=255)
    de_description=models.TextField(null=True)


class issui_tbl(models.Model):
    issui_name=models.CharField(max_length=255)
    issui_description = models.TextField(null=True)

