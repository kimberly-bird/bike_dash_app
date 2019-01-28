from django.conf.urls import url
from django.urls import path

from bikes import views
from . import views

app_name = "bikes"
urlpatterns = [
    # path('', views.index, name='index'),
    path('brands/', views.brand_list, name='brand_list'),
    url(r'^login$', views.login_user, name='login'),
    url(r'^logout$', views.user_logout, name='logout'),
    url(r'^register$', views.register, name='register'),
]