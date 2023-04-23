from django.urls import path
from . import views


app_name='main' 

urlpatterns = [
    path('aboutus/', views.aboutus, name='aboutus'),
    path('holiday/', views.holiday, name='holiday'),
    path('howto/', views.howto, name='howto'),
    path('', views.index, name='index'),
    path('programs/', views.programs, name='programs'),
]
