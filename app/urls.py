from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('strategies/', views.strategies, name='strategies'),
    path('', views.ActivityListView.as_view(), name='activities'),
    path('activity/<int:pk>/', views.ActivityDetailView.as_view(), name='activity-detail'),  # 👈 هنا
    path('statements/', views.statements, name='statements'),
    path('contact/', views.contact, name='contact'),
]