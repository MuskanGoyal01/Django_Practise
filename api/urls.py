from django.urls import path
from . import views

from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('',views.apiOverview),
    path('getData/',views.getData),
    path('getItem/<str:pk>/', views.getItem),
    path('add/',views.addItem),
    path('update/<str:pk>/', views.updateItem),
    path('delete/<str:pk>/', views.deleteItem),

    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

