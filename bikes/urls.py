from django.conf.urls import url
from django.urls import path

from bikes import views
from . import views

app_name = "bikes"
urlpatterns = [
    path('', views.index, name='index'),
    path('ajax/load_models/', views.load_models, name='ajax_load_models'),
    path('brands/', views.brand_list, name='brand_list'),
    path('brands/add', views.add_brand, name='add_brand'),
    path('brands/edit/<int:pk>/', views.edit_brand, name='edit_brand'),
    path('dashboard/', views.BikeChartView.as_view(), name='dashboard'),
    path('models/add/<int:pk>', views.add_bike_model, name='add_bike_model'),
    path('models/edit/<int:pk>/', views.edit_bike_model, name='edit_bike_model'),
    path('labor/', views.labor_list, name='labor_list'),
    path('labor/add', views.add_labor, name='add_labor'),
    path('mybikes/status/<int:status_id>', views.bike_list, name='bike_list'),
    path('mybikes/add', views.add_bike, name='add_bike'),
    path('mybikes/<int:pk>', views.bike_detail, name='bike_detail'),
    path('mybikes/edit/<int:pk>/', views.edit_bike, name='edit_bike'),
    path('mybikes/remove-part/<int:pk>/', views.remove_part_from_bike, name='remove_part_from_bike'),
    path('mybikes/sell/<int:pk>/', views.sell_bike, name='sell_bike'),
    path('mybikes/list/<int:pk>/', views.list_bike_for_sale, name='list_bike_for_sale'),
    path('parts/', views.part_list, name='part_list'),
    path('parts/add', views.add_part, name='add_part'),
    path('parts/<int:pk>', views.part_detail, name='part_detail'),
    path('parts/edit/<int:pk>/', views.edit_part, name='edit_part'),
    path("parts/search", views.part_search, name="part_search"),
    path('parttypes/<int:pk>/', views.parttype_list, name='parttype_list'),
    url(r'^login$', views.login_user, name='login'),
    url(r'^logout$', views.user_logout, name='logout'),
    url(r'^register$', views.register, name='register'),
]