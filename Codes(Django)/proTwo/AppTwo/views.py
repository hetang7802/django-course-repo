from django.shortcuts import render
from django.http import HttpResponse
# from AppTwo.models import User_details
from AppTwo.forms import NewUserForm

def index(request):
    return HttpResponse("<em>second app<br>go to /user to sign up</em>")
# Create your views here.

def help(request):
    help_dict = {'help_insert':"your help page"}
    return render(request,'AppTwo/help.html',context=help_dict)

# def user(request):
#     user_list=User_details.objects.order_by('f_name')
#     user_dict = {'users':user_list}
#     return render(request,'AppTwo/users.html',context=user_dict)


def user(request):

    form = NewUserForm()

    if request.method=="POST":
        form=NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR: FORM IS INVALID")

    return render(request,'AppTwo/users.html',{'form':form})
