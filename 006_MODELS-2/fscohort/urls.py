from django.urls import path
from .views import fscohort, subfolder
urlpatterns = [
 path("", fscohort), # /fscohort/
 path("subfolder", subfolder), # /fscohort/subfolder
    
]