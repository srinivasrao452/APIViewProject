

from django.urls import path
from APIViewApp import views

urlpatterns = [
    path('emp/', views.EmpListView.as_view()),
    path('emp/<int:id>/', views.EmpDetailView.as_view()),
]