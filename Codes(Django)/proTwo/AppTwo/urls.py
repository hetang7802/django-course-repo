from django.conf.urls import url
from AppTwo import views

urlpatterns = [
    url(r'user/$',views.user,name='users'),
    url(r'help/$',views.help,name='help'),
]
