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
    
