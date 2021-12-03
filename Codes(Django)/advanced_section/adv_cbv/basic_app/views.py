from django.shortcuts import render
from django.views.generic import View,TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from basic_app import models
from django.urls import reverse_lazy
# Create your views here.
def index(request):
    return render(request,'index.html')

class CBView(View):
    def get(self,request):
        return HttpResponse("Class based view are cool!")

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme']='BASIC INJECTION!'
        return context

class SchoolListView(ListView):
    context_object_name = 'schools'
    # this(schools) will be the name we will use when we want to use this class
    # if this name was not given default name will be used which is (nameofmodelinlowercase_list) i.e school_list
    model = models.School


class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    # this(school_detail) will be the name we will use when we want to use this class
    # if this name was not given default name will be used which is (nameofmodelinlowercase) i.e school
    model = models.School
    template_name = 'basic_app/school_detail.html'


class SchoolCreateView(CreateView):
    # for this to work it is necessary to create a file inside templates/basic_app folder
    # named school_form.html (here school is the name of model we are using, in lower case)

    model = models.School
    fields = ('name','principal','location') # these are the fields we want the user to edit


class SchoolUpdateView(UpdateView):
    fields = ('name','principal',)
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('basic_app:list')
