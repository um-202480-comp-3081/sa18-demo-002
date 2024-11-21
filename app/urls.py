from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path("customers/", views.customer_list, name="customer_list"),
    path("customers/<int:id>", views.customer_detail, name="customer_detail"),
]
