from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('<str:page_id>/detail/', views.Detail.as_view(), name='detail'),
    path('<str:page_id>/delete/', views.Delete.as_view(), name='delete'),
]