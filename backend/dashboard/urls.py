from django.urls import path
from .views import dashboard_home,dashboard_stats
urlpatterns = [
    path('home/',dashboard_home,name='dashboard-home'),
    path('api/stats/',dashboard_stats,name='dashboard-stats'),
]