from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'dreams/$', views.ApiDreams.as_view()),
    url(r'dreams/status/(?P<status>[\w-]+)/$', views.ApiDreams.as_view()),
    url(r'dreams/(?P<id>[\d+])/$', views.ApiDreams.as_view()),
    url(r'volunteers/$', views.ApiVolunteers.as_view()),
    url(r'volunteers/(?P<id>[\d+])/$', views.ApiVolunteers.as_view()),
    url(r'partners/$', views.ApiPartners.as_view()),
    url(r'partners/(?P<id>[\d+])/$', views.ApiPartners.as_view())
]