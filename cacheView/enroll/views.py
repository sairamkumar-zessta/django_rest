from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.cache import cache_page
# Create your views here.
@cache_page(30)
def home(request):
    return render(request,'enroll/course.html') 

def contact(request):
    return HttpResponse('<h1> This is contact page</h1>') 
    