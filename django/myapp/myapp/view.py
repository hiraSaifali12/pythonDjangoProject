from django.http import HttpResponse 
from django.shortcuts import render
import datetime
def home(request):
    if request.method == 'POST':
        check = request.POST['check']
        print(check)
    date=datetime.datetime.now() 
    isActive= True
    name="hira"
    list_of_program=[

        'write a program to check even or odd',
        'write a program to check prime number',
        'write a program to print pascal triangle',
        'write a program to check prime number 1 to 100'
          
    ]
    
    student={
          'student_name':"rahul",
          'student_college':"XYZ",
          'student_city':"tanakpur"
    }
    data = {
          'date' : date,
          'isActive' : isActive,
          'name' : name,
          'list_of_program': list_of_program,
          'student_data' : student
    }
    #print("test function is called is from view")
    #return HttpResponse("<h1>hello this is index page</h1>" + str(date))
    return render(request,'home.html',data)

def about(request):
    #return HttpResponse("<h1>this is about page</h1>")
    return render(request,'about.html',{})
   
def services(request):
    #return HttpResponse("<h1>this is services page</h1>")
    return render(request,'services.html',{})
    