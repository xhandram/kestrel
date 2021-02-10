from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def customer(request):
    return render(request,'home.html')

def courier(request):
    return render(request,'home.html')