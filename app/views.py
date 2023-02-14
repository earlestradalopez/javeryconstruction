from django.shortcuts import render

# Create your views here.
def index(request):
     return render(request, 'index.html')

def personnel(request):
    return render(request, 'personnel.html')

def c_projects(request):
    return render(request, 'c-projects.html')

def p_projects(request):
    return render(request, 'p-projects.html')

def products(request):
    return render(request, 'products.html')