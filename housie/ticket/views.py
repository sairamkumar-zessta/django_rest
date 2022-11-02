from django.shortcuts import render

# Create your views here.

def display_ticket(request):
    return render(request,'ticket.html')
