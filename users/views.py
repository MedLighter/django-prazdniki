from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from main.models import Orders


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()
    context={
        'form': form,
        'title': 'Login'
    }
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {
        'form': form,
        'title': 'Registration'
    }
    return render(request, 'users/registration.html', context)

def profile(request):
    if request.method == 'POST':
        print(request.POST)
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)

    orders = Orders.objects.filter(user_id = request.user.id)
    context = {
        'form': form,
        'title': 'Profile',
        'orders': orders
    }
    return render(request, 'users/profile.html', context)


def delete_order(request, order_id):
    order = Orders.objects.get(id=order_id)
    if order.user_id == request.user:
        order.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))