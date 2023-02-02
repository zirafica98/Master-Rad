from django.urls import path
from . import views

app_name = "reportes"

urlpatterns = [
    path('sales-dashboard/', views.SalesDashboard, name='sales_dashboard'),
]