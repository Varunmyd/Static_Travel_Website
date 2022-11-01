from django.shortcuts import render
from django.http import HttpResponse

from . models import Place
from . models import People
# Create your views here.

def demo(request):
    obj=Place.objects.all()
    obj1=People.objects.all()

    return render(request,"index.html",{'result':obj,'result1':obj1})



















# def demo(request):
#     name='India'
#     return render(request,"in.html",{'key':name})
# def add(request):
#           x =int(request.GET['num1'])
#           y = int(request.GET['num2'])
#           reslt=x+y
#           reslt1= x - y
#           reslt2 = x * y
#           reslt3 = x / y
#           return render(request,"result.html",{'result':reslt,'result1':reslt1,'result2':reslt2,'result3':reslt3})
# def about(request):
#     return render(request,"about.html")
# def contact(request):
#     return HttpResponse("hey everybody")