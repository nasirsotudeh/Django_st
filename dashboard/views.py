from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserChangeForm
from django.http import JsonResponse ,HttpResponse
from .forms import CustomUserCreationForm ,UserLoginForm , UserRegisterForm
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
from django.http import JsonResponse
from django.shortcuts import render
from .models import Order
from django.core import serializers

################################################################

def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/index')

    context = {
        'form': form,
    }
    return render(request, "registration/login.html", context)

################################################################

def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=user.password)
        login(request, user , backend='django.contrib.auth.backends.ModelBackend')
        # if next:
        #     return redirect()
        log = user.username
        context = {
        'login' : log}
        return render(request,'dashboard/index.html',context)

    else:
        context = {'form': form,}
        return render(request, "registration/register.html", context)
    
    
def logout_view(request):
    logout(request)
    return redirect('/')

###################################################################

def dashboard_with_pivot(request):
    return render(request, 'dashboard_with_pivot.html', {})

def pivot_data(request):
    dataset = Order.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)

def index (request):
    return render(request , 'dashboard/index.html')

# def register(request):
#     if request.method == "GET":
#         return render(
#             request, "registration/register.html",
#             {"form": CustomUserCreationForm}

#         )
#     elif request.method == "POST":
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user, backend='django.contrib.auth.backends.ModelBackend')
#             return  render(request , 'dashboard/index.html')

######################################################################

