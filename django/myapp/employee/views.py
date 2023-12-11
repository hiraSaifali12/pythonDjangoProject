from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import employee,testimonial
from .form import feedbackForm
# Create your views here.
def employee_home(request) : 
    
    emps=employee.objects.all()

    return render(request,"employee/home.html",{
        'emps':emps
    })

def add_employee(request):
    if request.method=="POST" :
        #print("data is coming")
        


        #fetch the data

        emp_name = request.POST.get("emp_name")

        emp_id = request.POST.get("emp_id")

        emp_phone = request.POST.get("emp_phone")

        emp_address = request.POST.get("emp_address")
        emp_working = request.POST.get("emp_working")


        emp_department = request.POST.get("emp_department")


        
        #create model object and set data
        e=employee()
        e.name=emp_name
        e.employee_id=emp_id
        e.phone= emp_phone
        e.address=emp_address
        e.department=emp_department
        
        if emp_working is None :
            e.working = False
        else :
            e.working= True
        
        
        #save objects
        e.save()
        #prep msg

        return redirect("/employee/home/")
    return render(request,"employee/add_employee.html",{})


def delete_employee(request,emp_id):
    emp=employee.objects.get(pk=emp_id)
    emp.delete()
    return redirect("/employee/home/")

def update_employee(request,emp_id):
    emp=employee.objects.get(pk=emp_id)
    
    return render(request,"employee/update_employee.html", {
        'emp': emp
    })

def do_update_employee(request,emp_id):
    if request.method=='POST':
        emp_name = request.POST.get("emp_name")
        emp_id_tmp = request.POST.get("emp_id")
        emp_phone = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        emp_working = request.POST.get("emp_working")
        emp_department = request.POST.get("emp_department")

        e=employee.objects.get(pk=emp_id)

        e.name=emp_name
        e.employee_id=emp_id_tmp
        e.phone= emp_phone
        e.address=emp_address
        e.department=emp_department
        
        if emp_working is None :
            e.working = False
        else :
            e.working= True
        
        e.save()

    return redirect("/employee/home/")

def testimonials(request):
    testi=testimonial.objects.all()
    return render(request,"employee/testimonials.html",{
        'testi':testi
    })

def feedback(request):
    if request.method=='POST':
        form=feedbackForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['email'])
            print(form.cleaned_data['name'])
            print(form.cleaned_data['feedback'])
            
            print("data saved")
        else:
            return render(request,"employee/feedback.html",{'form': form})
           
    else:
       form=feedbackForm()
       return render(request,"employee/feedback.html",{'form': form})