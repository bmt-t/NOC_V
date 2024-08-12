from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Technical(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)  # Sử dụng CharField cho số điện thoại
    email = models.EmailField(max_length=100)  # Sử dụng EmailField cho địa chỉ email
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='technicals')  # Quan hệ ForeignKey
    description = models.TextField(null=True, blank=True)  # Cho phép để trống

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    

class Issue(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class TechIssue(models.Model):
    technical = models.ForeignKey(Technical, on_delete=models.CASCADE, related_name='tech_issues')
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='tech_issues')

class DpmIssue(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='dpm_issues')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='dpm_issues')
    # Có thể thêm các trường khác như status, created_at, resolved_at nếu cần
