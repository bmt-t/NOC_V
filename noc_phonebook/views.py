# myapp/views.py
from django.shortcuts import render, get_object_or_404
from .models import Department, Technical, Issue, TechIssue, DpmIssue

def department_list(request):
    abc = Department.objects.all()
    return render(request, 'noc_phonebook/department_list.html', {'departments': abc})

def department_details(request, id):
    abc=Department.objects.all()
    department = get_object_or_404(Department, id=id)
    technicals = Technical.objects.filter(department=department)
    dpm_issues = DpmIssue.objects.filter(department=department)
    return render(request, 'noc_phonebook/department_details.html', {
        'department': department,
        'technicals': technicals,
        'dpm_issues': dpm_issues,
        'abc':abc,
    })

def issue_details(request, id):
    issue = get_object_or_404(Issue, id=id)
    tech_issues = TechIssue.objects.filter(issue=issue)
    return render(request, 'noc_phonebook/issue_details.html', {
        'issue': issue,
        'tech_issues': tech_issues
    })