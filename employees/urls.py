from django.urls import path
from .views import employees_view, CreateEmployeeView, UpdateEmployeeView, DeleteEmployeeView

urlpatterns = [
    path('employees/', employees_view, name = 'main'),
    path('employees/new/', CreateEmployeeView.as_view(), name = 'new'),
    path('employees/del/<int:pk>', DeleteEmployeeView.as_view(), name = 'del'),
    path('employees/edit/<int:pk>', UpdateEmployeeView.as_view(), name = 'edit'),


]