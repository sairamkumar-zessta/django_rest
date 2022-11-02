from django.shortcuts import render,HttpResponseRedirect

from .models import Employee
from .forms import EmployeeRegistration
# Create your views here.

#This Function Will Add New Item and show all Items
def add_show(request):
    if request.method == 'POST':
        em = EmployeeRegistration(request.POST)
        if em.is_valid():
            # em.save()
            e_id = em.cleaned_data['Emp_ID']
            nm = em.cleaned_data['name']
            ds = em.cleaned_data['designation'] 
            ema = em.cleaned_data['email']
            ex = em.cleaned_data['experience']
            reg = Employee(Emp_ID=e_id,name = nm,designation = ds, email = ema, experience = ex )
            reg.save()
            em = EmployeeRegistration()
            return HttpResponseRedirect('/')
    else:
        em = EmployeeRegistration()
    emp = Employee.objects.all()
    return render(request,'enroll/addandshow.html',{'form' : em ,'emp':emp})

def delete_data(request,id):
    if request.method == "POST" :
        pi = Employee.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

def update_data(request,id):
    if request.method == 'POST':
        pi = Employee.objects.get(pk=id)
        fm = EmployeeRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save() 
    else:
        pi = Employee.objects.get(pk=id)
        fm = EmployeeRegistration(instance=pi)
    return render(request,'enroll/update.html',{'form' : fm})