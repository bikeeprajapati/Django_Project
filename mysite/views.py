from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import userForm
from service.models import Features


def evenodd(request):
    if request.POST.get('num1')=="":
          return render(request,"evenodd.html",{'error':True})

        
    c=''
    if request.method == 'POST':
      n1=eval(request.POST.get('num1'))
      if n1%2==0:
          c='Even'
      else:
          c='Odd'
    return render(request,"evenodd.html",{'c':c})

def marksheet(request):
    if request.method=="POST":
        s1=eval(request.POST.get('sub1'))
        s2=eval(request.POST.get('sub2'))
        s3=eval(request.POST.get('sub3'))
        s4=eval(request.POST.get('sub4'))
        s5=eval(request.POST.get('sub5'))
        t=s1+s2+s3+s4+s5
        p=t*100/500
        data={
            'total':t,
            'per':p
        }
        return render(request,'marksheet.html',data)  

    return render(request,'marksheet.html')  

def aboutUS(request):
    return HttpResponse("Welcome to Django Learning!")

def myskills(request):
    return HttpResponse("I am a good developer")
def calculator(request):
     c=''
     try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            op=request.POST.get('opr')
            if op=="+":
                c=n1+n2
            elif op=="-":
                c=n1-n2
            elif op=="*":
                c=n1*n2
            else:
                c=n1/n2
                
       
            
     except:
         c="Invalid Operation"
     print(c)
    
     return render(request,"calculator.html",{'c':c})

def Hobbies(request):
    return HttpResponse("Playing,Singing")
def submitform(request):
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
            return HttpResponse(res)
        except ValueError:
           pass
    

def myDetails(request,detailsid):
    return HttpResponse(detailsid)

def HomePage(request):
    FeaturesData=Features.objects.all().order_by('-id')[:4]
    
    data={
        
            'FeaturesData':FeaturesData
        
    }
        
    return render(request,'index.html',data)
def userform(request):
    # Initialize result as None to handle cases where the form is not submitted
    res = None
    fn=userForm
    data={'form':fn}

    # Check if the request method is GET and parameters are present
    if 'value1' in request.POST and 'value2' in request.POST:
        try:
            n1 = int(request.POST.get('value1'))
            n2 = int(request.POST.get('value2'))
            res = n1 + n2
            data={
                'form':fn,
                'result': res
            }
        
        except ValueError:
            res = "Invalid input. Please enter numbers."

    return render(request, "userform.html",  data)

    
