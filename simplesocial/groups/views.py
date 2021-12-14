from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from django.contrib.auth.mixins import (
                        LoginRequiredMixin,PermissionRequiredMixin)

from django.urls import reverse
from django.views import generic
from groups.models import Group, GroupMember
from django.shortcuts import get_object_or_404
from django.db import IntegrityError
from . import models

# view to create a new group
class CreateGroup(LoginRequiredMixin,generic.CreateView):
    fields= ('name','description')
    model = Group

# this will show the details(posts, etc) for a certain group
class SingleGroup(generic.DetailView):
    model = Group

# the list of all groups
class ListGroups(generic.ListView):
    model = Group

# note the new CBV used below
class JoinGroup(LoginRequiredMixin,generic.RedirectView):

    def get_redirect_url(self,*args,**kwargs):
        return reverse('groups:single',kwargs={'slug':self.kwargs.get('slug')})

    def get(self,request,*args,**kwargs):
        group = get_object_or_404(Group,slug=self.kwargs.get('slug'))

        try:
            GroupMember.objects.create(user=self.request.user,group=group)
        except IntegrityError:
            messages.warning(self.request,'Warning, already a member!')
        else:
            messages.success(self.request,'You are now a member!')
        return super().get(request,*args,**kwargs)


class LeaveGroup(LoginRequiredMixin,generic.RedirectView):

    def get_redirect_url(self,*args,**kwargs):
        return reverse('groups:single',kwargs={'slug':self.kwargs.get('slug')})

    def get(self,request,*args,**kwargs):

        try:
            membership = models.GroupMember.objects.filter(
                user=self.request.user,
                group__slug=self.kwargs.get('slug')
            ).get()
        except models.GroupMember.DoesNotExist:
            messages.warning(self.request,'Sorry, You are not in this group')
        else:
            membership.delete()
            messages.success(self.request,'Left group successfully')

        return super().get(request,*args,**kwargs)
