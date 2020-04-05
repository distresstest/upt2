from django.urls import path
from . views import (
    location_create_view,
    location_detail_view,
    location_delete_view,
    location_list_view,
    location_update_view,
)

app_name = 'locations'
urlpatterns = [
    path('', location_list_view, name='location_list'),
    path('create/', location_create_view, name='location_list'),
    path('<int:id>/', location_detail_view, name='location_detail'),
    path('<int:id>/update/', location_update_view, name='location_update'),
    path('<int:id>/delete/', location_delete_view, name='location_delete'),
]