from email.policy import HTTP
from unittest import loader
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Company, Student, StudentInfo, JobInfo, EventInfo, CompanyInfo
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse



# Create your views here.
def index(request):
    return render(request, 'includes/index.html')

def register_page(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You are successfully registered.')
        return redirect("/")
    else:
        form = RegisterForm()
        
    return render(request, "registration/register.html", {"form":form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect("/")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    form = AuthenticationForm()
    return render(request, "registration/login.html",{"form": form})



def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/")

@login_required(login_url='/login/')
def register_student(request):
    return render(request,'TPO_app/register_student.html')

def register_student_submit(request):
    print("Hello form is submitted")
    print(request.POST['name'])
    print(request.POST['event'])
    name = request.POST['name']
    email = request.POST['email']
    phoneno = request.POST['phoneno']
    event = request.POST['event']
    Student_Info = StudentInfo(uname=name,email=email, phoneno=phoneno,event=event)
    Student_Info.save()
    messages.success(request, 'You have successfully registered.')
    return render(request,'TPO_app/register_student.html')



def companies(request):
    return render(request,'includes/company.html')

@login_required(login_url='/login/')
def register_job(request):
    return render(request,'includes/register_job.html')

def register_job_submit(request):
    print("Hello form is submitted")
    print(request.POST['name'])
    print(request.POST['college'])
    print(request.POST['company'])
    print(request.POST['profile'])
    print(request.POST['graduation'])
    print(request.POST['phoneno'])
    name = request.POST['name']
    email = request.POST['email']
    phoneno = request.POST['phoneno']
    college = request.POST['college']
    graduation = request.POST['graduation']
    company = request.POST['company']
    profile = request.POST['profile']

    Job_Info = JobInfo(uname=name, email=email, phoneno=phoneno, college=college, graduation=graduation, company=company, profile=profile)
    Job_Info.save()
    messages.success(request, 'Your Application is successfully sent.')
    return render(request,'includes/register_job.html')

def upcoming_events(request):
    return render(request,'includes/upcoming_events.html')


def upcoming_events_submit(request):
    print(request.POST['eventname'])
    eventname = request.POST['eventname']
    description = request.POST['description']
    eventdate = request.POST['eventdate']
    Event_Info = EventInfo(eventname=eventname,description=description, eventdate=eventdate)
    Event_Info.save()
    messages.success(request, 'Your Event is successfully saved.')
    return render(request,'includes/upcoming_events.html')


def add_company(request):
    return render(request,'includes/add_company.html')


def add_company_submit(request):
    print(request.POST['cname'])
    cname = request.POST['cname']
    role = request.POST['role']
    salary = request.POST['salary']
    Company_Info = CompanyInfo(cname=cname,role=role,salary=salary)
    Company_Info.save()
    messages.success(request, 'Your Company is successfully saved.')
    return render(request,'includes/add_company.html')


def Statistics(request):
    return render(request,'includes/Statistics.html')
# def home_supply_submit(request):
#     print("Hello form is submitted")
#     companyname = request.POST["companyname"]
#     medicine = request.POST["medicine"]
#     quantity = request.POST["quantity"]
#     Supplier_Info = StudentInfo(medicine=medicine, quantity=quantity, companyname=companyname)
#     Supplier_Info.save()
#     return render(request, "supplier/home_supply.html")




# def list_eligible_students(request):
#        company_id = request.POST.get('company_id')
    #   if company_id:
   #        company = company.objects.get(pk=company_id)
   #         eligible_students = Student.objects.filter(is_placed=False)  # Filter out already placed
   #         eligible_students = eligible_students.filter(companies__eligibility_criteria=company.eligibility_criteria)  # Optimize with prefetch/select_related
   #         context = {'eligible_students': eligible_students, 'company': company}
   #         return render(request, 'eligible_students_list.html', context)
  #     companies = Company.objects.all()  # Optionally, filter for active companies
   ##    context = {'companies': companies}
   #    return HttpResponse(request, 'includes/eligible_students_list.html', context)

def list_eligible_students(request):
    # Fetching eligible students from the database
    eligible_students = Student.objects.filter(is_placed=False,cgpa=7.0)

    # Generating a string representation of eligible students
   # eligible_students_list = "\n".join([student.name for student in eligible_students])
    eligible_students_list = "\n".join([
    f"Name: {student.name} , CGPA: {student.cgpa} , PRN: {student.prn} , Branch: {student.branch} , Batch: {student.year}" 
    for student in eligible_students])
    
    #Constructing the HTTP response with the list of eligible students
    response = HttpResponse(eligible_students_list, content_type='text/plain', status=200)

    return response

