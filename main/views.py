from django.shortcuts import render

# Create your views here.
def aboutus(request):
    return render(request, 'main/aboutus.html')

def holiday(request):
    return render(request, 'main/holiday.html')

def howto(request):
    return render(request, 'main/howto.html')

def index(request):
    return render(request, 'main/index.html')

def mastets(request):
    return render(request, 'main/mastets.html')

def programs(request):
    return render(request, 'main/programs.html')