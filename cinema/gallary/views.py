from django.shortcuts import render
# Create your views here.

def adventure(request):
    return render(request,'gallary/adventure.html')

def princesses(request):
    return render(request,'gallary/princesses.html')

def magazine(request):
    return render(request,'gallary/magazine.html')
