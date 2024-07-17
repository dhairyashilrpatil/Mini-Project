from django.contrib import admin
from .models import Company, EligibilityCriteria, Student, StudentInfo, JobInfo, EventInfo, CompanyInfo

# Register your models here.
admin.site.register(StudentInfo)
admin.site.register(JobInfo)
admin.site.register(EventInfo)
admin.site.register(CompanyInfo)
admin.site.register(Student)
admin.site.register(Company)
admin.site.register(EligibilityCriteria)
