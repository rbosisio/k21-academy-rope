from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'dreams/$', views.ApiDreams.as_view()),
]