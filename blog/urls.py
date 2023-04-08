from django.urls import path

from . import views


urlpatterns =[
    path('', views.index, name='index'),
    path("index/",views.index, name="index"),
    path("search",views.search,),
    path("about/",views.about, name='about'),
    path("details/",views.course_details,name='course_details'),
    path("trainers/",views.trainers, name='trainers'),
    path("courses/",views.courses, name='courses'),
    path("contact/",views.contact, name='contact'),
    path("pricing/",views.pricing, name='pricing')
]   