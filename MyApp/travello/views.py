from django.shortcuts import render
from .models import Destination, FacultData
from operator import attrgetter
# Create your views here.


#dests = Destination.objects.all()

dests = FacultData.objects.all()
dests = sorted(dests, key= attrgetter('senior'))
def index(request):
    #return render(request,'index.html',{'dests':dests})
    return render(request,'index.html',{'dests':dests})