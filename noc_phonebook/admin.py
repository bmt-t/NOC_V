from django.contrib import admin
from .models import Department, Technical, Issue

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    ordering = ('name',)

class TechnicalAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'phone', 'email', 'department')
    search_fields = ('firstname', 'lastname', 'email')
    list_filter = ('department',)
    ordering = ('lastname',)

class IssueAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    ordering = ('name',)

admin.site.register(Department, DepartmentAdmin)
admin.site.register(Technical, TechnicalAdmin)
admin.site.register(Issue, IssueAdmin)