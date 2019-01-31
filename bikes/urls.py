from django.conf.urls import url
from django.urls import path

from bikes import views
from . import views

app_name = "bikes"
urlpatterns = [
    # path('', views.index, name='index'),
    path('brands/', views.brand_list, name='brand_list'),
    path('brands/add', views.add_brand, name='add_brand'),
    path('brands/edit/<int:pk>/', views.edit_brand, name='edit_brand'),
    path('models/add/<int:pk>', views.add_bike_model, name='add_bike_model'),
    path('models/edit/<int:pk>/', views.edit_bike_model, name='edit_bike_model'),
    url(r'^login$', views.login_user, name='login'),
    url(r'^logout$', views.user_logout, name='logout'),
    url(r'^register$', views.register, name='register'),
]