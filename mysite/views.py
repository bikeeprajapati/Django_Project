from django.http import HttpResponse
from django.shortcuts import render

def aboutUS(request):
    return HttpResponse("Welcome to Django Learning!")

def myskills(request):
    return HttpResponse("I am a good developer")

def Hobbies(request):
    return HttpResponse("Playing,Singing")

def myDetails(request,detailsid):
    return HttpResponse(detailsid)

def HomePage(request):
    data={
        'title':'Hello World',
        'Clist':['php','python','java'],
        'Numbers':[13,56,84,67],
        'StudentDetails': [
        {'name':'Rahul','age':20},
        {'name':'Mohan','age':23},
        
     ]
        
    }
        
    return render(request,'index.html',data)
def userform(request):
    # Initialize result as None to handle cases where the form is not submitted
    res = None
    data={}

    # Check if the request method is GET and parameters are present
    if 'value1' in request.POST and 'value2' in request.POST:
        try:
            n1 = int(request.POST.get('value1'))
            n2 = int(request.POST.get('value2'))
            res = n1 + n2
            data={
                'n1':n1,
                'n2':n2,
                'result': res
            }
        except ValueError:
            res = "Invalid input. Please enter numbers."

    return render(request, "userform.html",  data)

    
