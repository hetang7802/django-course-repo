from django.shortcuts import render
from basicapp import forms
# Create your views here.

def index(request):
    return render(request,'basicapp/index.html')

def form_view(request):
    form = forms.FormName()
    if request.method == "POST":
        form=forms.FormName(request.POST)
        if form.is_valid():
            # do something
            print("validations success!")
            print("name is " +form.cleaned_data['name'])
            print ("email is " + form.cleaned_data['email'])
            print("text is " +form.cleaned_data['text'])
    return render(request,'basicapp/forms.html',{'form':form})
