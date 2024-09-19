from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_form, name='insert'),
    path('<uuid:id>/', views.employee_form, name='employee_update'),
    path('delete/<uuid:id>/', views.employee_delete, name='employee_delete'),
    path('list/', views.employee_list, name='employee_list'),
]