from django.contrib import admin
from . import models
# Register your models here.

# the below class allows us to directly edit/view members in the Group tab in the
# admin page and we do not have to register GroupMember separately
class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember

admin.site.register(models.Group)
