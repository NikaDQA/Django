from django.urls import path
from .views import view_name
from .views import view_name1
from .views import view_name2
from .views import view_name3

urlpatterns = [
    path('', view_name),
    path('acricles/', view_name1),
    path('acrticles/archive/', view_name2),
    path('users/', view_name3),
]