from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teams/', views.team_list, name='team_list'),
    path('teams/<int:team_id>/', views.team_detail, name='team_detail'),
    path('fixtures/', views.generate_fixtures, name='generate_fixtures'),
    path('points/', views.points_table, name='points_table'),
]
