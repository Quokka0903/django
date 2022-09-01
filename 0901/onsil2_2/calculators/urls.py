from django.urls import path
from . import views

urlpatterns = [
    path('calculator/<int:val1>/<int:val2>/', views.calculator, name='calculator'),
]
