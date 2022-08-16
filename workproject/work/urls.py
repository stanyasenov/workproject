from django.urls import path

from workproject.work.views import modules_data

urlpatterns = (
    path('', modules_data),
)