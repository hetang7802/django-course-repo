from django import template
from django.db import models
from django.utils.text import slugify
from django.urls import reverse
# slugify will take care of non alphanumeric characters in string

import misaka
# Create your models here.

from django.contrib.auth import get_user_model
User = get_user_model()

register = template.Library()


class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False, default='', blank=True)
    members = models.ManyToManyField(User, through='GroupMember')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        # the above line will convert name to lower case letters
        # and insert underscores in place of blanks
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('groups:single', kwargs={'slug': self.slug})

    class Meta():
        ordering = ['name']


class GroupMember(models.Model):
    group = models.ForeignKey(Group, related_name='memberships',on_delete=models.CASCADE)
    # the related_name parameter specifies the other side of the relation
    # for ex it connects User 'model' to Groupmember 'model' using user_groups in the below line
    user = models.ForeignKey(User, related_name='user_groups',on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta():
        unique_together = ('group', 'user')
