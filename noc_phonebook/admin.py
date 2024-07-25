from django.contrib import admin
from .models import department_tbl,so_tbl

# Register your models here.
admin.site.register(department_tbl)
admin.site.register(so_tbl)