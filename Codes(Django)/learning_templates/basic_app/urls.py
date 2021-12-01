from django.conf.urls import url
from basic_app import views

# TEMPLATE TAGGING
app_name='basic_app' #important point to note for relative urls

urlpatterns=[
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^other/$',views.other,name='other')
]
