from django.shortcuts import redirect, render

# Create your views here.

def contact(request):
    return render(request,'contact.html')
