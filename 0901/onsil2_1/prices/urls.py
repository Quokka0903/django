from django.urls import path
from . import views

urlpatterns = [
    path('<str:name>/<int:val>/', views.price, name='price'),
]
