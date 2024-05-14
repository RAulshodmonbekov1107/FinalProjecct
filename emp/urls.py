from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path("home/",emp_home),
    path("add-emp/",add_emp),
    path("delete-emp/<int:emp_id>",delete_emp),
    path("update-emp/<int:emp_id>",update_emp),
    path("do-update-emp/<int:emp_id>",do_update_emp),
    path('create/', create_performance_evaluation, name='create_performance_evaluation'),
    path('list/', list_performance_evaluations, name='list_performance_evaluations'),
    path('add/', add_payroll, name='add_payroll'),
    path('payroll-list/', payroll_list, name='payroll_list'),
]



