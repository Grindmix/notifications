from django.urls import path
from notify import views

urlpatterns = [
    path('notifications/', views.notification_list),
    path('notifications/send/<int:pk>/', views.notification_send),
    path('notifications/<int:pk>/', views.notification_detail),
]
