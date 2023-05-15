from django.urls import path
from . import views

urlpatterns = [
    path('', views.edit_products_list, name="edit_products_list"),
    path('create/', views.create_product, name="create_product")
]