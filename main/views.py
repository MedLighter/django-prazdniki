from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UserCreateApplicationForm
from django.contrib import messages

# Create your views here.
def aboutus(request):
    return render(request, 'main/aboutus.html')

def holiday(request):
    return render(request, 'main/holiday.html')

def howto(request):
    return render(request, 'main/howto.html')

def index(request):
    if request.method == "POST":
        form = UserCreateApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user_id = request.user
            messages.success(request, 'Вы успешно зарегистрировали заявку!')
            form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = UserCreateApplicationForm()


    context = {
        'form': UserCreateApplicationForm
    }
    return render(request, 'main/index.html', context)

def mastets(request):
    return render(request, 'main/mastets.html')

def programs(request):
    return render(request, 'main/programs.html')