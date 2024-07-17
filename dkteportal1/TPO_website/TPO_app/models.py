from django.db import models

# Create your models here.
class StudentInfo(models.Model):
    uname = models.CharField(max_length=200, default='')
    email = models.CharField(max_length=200)
    phoneno = models.CharField(max_length=200)
    event = models.CharField(max_length=20)
    
    def __str__(self):
        return self.uname


class JobInfo(models.Model):
    uname = models.CharField(max_length=200, default='')
    email = models.CharField(max_length=200)
    phoneno = models.CharField(max_length=200)
    college = models.CharField(max_length=20)
    graduation = models.DecimalField(max_digits=19, decimal_places=2)
    company = models.CharField(max_length=200)
    profile = models.CharField(max_length=200)

    def __str__(self):
        return self.company
        
class EventInfo(models.Model):
    eventname = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    eventdate = models.CharField(max_length=200)
    
    def __str__(self):
        return self.eventname

class CompanyInfo(models.Model):
    cname = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    salary = models.CharField(max_length=200)
    
    def __str__(self):
        return self.cname



class Student(models.Model):
    name = models.CharField(max_length=100)
    prn = models.CharField(max_length=100,null=True)
    branch =models.CharField(max_length=100,null=True)
    year = models.IntegerField()
    cgpa = models.FloatField()
    skills = models.CharField(max_length=255)  # Comma-separated list or use ManyToManyField for individual skills
    is_placed = models.BooleanField(default=False)  # Optional to exclude placed students
    
    def __str__(self):
        return f"{self.name} {self.prn} {self.cgpa} {self.branch} {self.is_placed} {self.skills} "

class EligibilityCriteria(models.Model):
    minimum_cgpa = models.FloatField()
    required_skills = models.CharField(max_length=255)  # Comma-separated list or use ManyToManyField for individual skills
    def is_student_eligible(self, student):  # New method within the model class
        if student.is_placed:
            return False  # Exclude already placed students (optional)
        if student.cgpa < self.minimum_cgpa:
            return False
        required_skills = self.required_skills.split(',')
        for skill in required_skills:
            if skill.lower() not in student.skills.lower():
                return False
        return True

class Company(models.Model):
  name = models.CharField(max_length=100)
  eligibility_criteria = models.ForeignKey(EligibilityCriteria, on_delete=models.CASCADE)  # One-to-Many relationship