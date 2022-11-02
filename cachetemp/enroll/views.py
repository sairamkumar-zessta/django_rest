from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'enroll/course.html')
def contact(request):
    return HttpResponse('<h1> This is contact page</h1>')