from email.policy import default
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def setsession(request):
    request.session['name'] = 'Sai' 
    request.session['lname'] = 'Alladi' 
    return render(request,'student/setsession.html')
def getsession(request):
    # nm= request.session['name'] 
    nm = request.session.get('name',default = 'Anil')
    ln = request.session.get('lname')
    return render(request,'student/getsession.html',{'name':nm, 'lname':ln})
def delsession(request):
    if 'name' not in request.session:
        return HttpResponse('<h1> the key is not present in session </h1>')
    del request.session['name']
    return render(request,'student/delsession.html')