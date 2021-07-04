from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html',{'name':'Atta', 'last': 'Panhyar'})
def result(request):
    val1 = int(request.POST["num"])
    val2 = int(request.POST ["num2"])
    result = val1+val2
    return render(request,'result.html',{'result':result})