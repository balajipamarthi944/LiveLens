from django.urls import path
from .views import dashboard_home,dashboard_stats
urlpatterns = [
    path('',dashboard_home,name='dashboard_home'),path('api/stats/',dashboard_stats,name='dashboard_stats'),
]