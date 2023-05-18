from django.urls import path
from . import views

urlpatterns = [
    path('', views.edit_products_list, name="edit_products_list"),
    path('create/', views.create_product, name="create_product"),
    path('edit/', views.edit_product, name="edit_product"),
    path('draft/', views.edit_products_draft, name="edit_draft"),
    path('delete/', views.delete_product, name="delete_product"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout")
]