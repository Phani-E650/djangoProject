from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
def myfunctioncall(request):
    return HttpResponse(" hello world")
def myaboutfunctioncall(request):
    return HttpResponse(" about hello world")
def add(request,a,b):
    return HttpResponse(a+b)
def intro(request,name,age):
    mydictionary={
        "name": name,
        "age":age
    }
    return JsonResponse(mydictionary)
def myfirstpage(request):
    return render(request,'index.html')
def mysecondpage(request):
    return render(request,'second.html')
def mythirdpage(request):
    var = "hello world"
    greeting = "hey how are you"
    fruits =["apple","mango","banana"]
    num1,num2=3,5
    ans=num1>num2
    # print(ans)
    mydictionary={
        "var":var,
        "msg" : greeting,
        "myfruits":fruits,
        "num1":num1,
        "num2":num2,
        "ans":ans
    }
    return render(request,'third.html', context=mydictionary)
def myimagepage(request):
    return render(request,'imagepage.html')
def myimagepage2(request):
    return render(request,'imagepage2.html')
def myimagepage5(request,imagename):
    myimagename = str(imagename)
    myimagename = myimagename.lower()
    if(myimagename=="horse"):
        var=True
    else:
        var=False
    mydictionary={
        "var":var
    }

    return render(request,'imagepage5.html' , context = mydictionary)
def myform(request):
    return render(request,'myform.html')


