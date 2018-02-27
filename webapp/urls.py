from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from webapp import views

urlpatterns=[
    url(r'^$', views.get_list),
    url(r'^(?P<emp_id>\d+)+/$', views.employeedetail),
]