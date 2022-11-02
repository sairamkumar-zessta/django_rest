from django.shortcuts import render

# Create your views here.

def setcookie(request):
   resp = render(request, 'student/setcookie.html')
   resp.set_cookie('name','anil') 
   return resp 

def getcookie(request):
    # nm = request.COOKIES['name']
    nm = request.COOKIES.get('name','sai')
    return render(request, 'student/getcookie.html' ,{'name' : nm})

def delcookie(request):
    resp = render(request, 'student/delcookie.html')
    resp.delete_cookie('name') 
    return resp 