from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('delete/<int:id>/', views.delete_item, name='deletedata'),
    path('update/<int:id>/', views.update_item, name='updatedata'),
    path('update_data/<int:id>/', views.update_item_second,
         name='update_item_second'),
]
