from django.shortcuts import render
from basic_app.forms import UserForm,UserProfileInfoForm

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')

@login_required # this ensures that the user is already logged in before logging out
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("You are logged in, nice!")

def register(request):

    registered=False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user # this line creates a one-one relationship between actual user form and additional form

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered=True

        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'basic_app/register.html',
                                    {'user_form':user_form,
                                      'profile_form':profile_form,
                                      'registered':registered})
    # all this above info passed in render is used in the register.html file



def user_login(request):

    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        print('user is ',user)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Account not active!")
        else:
            print("someone tried to login and failed")
            print("username: {}, password: {}".format(username,password))

            return HttpResponse("invalid login details supplied!")

    else:
        return render(request,'basic_app/login.html',{})
