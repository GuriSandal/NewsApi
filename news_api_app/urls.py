from django.urls import path
from news_api_app import views

urlpatterns = [
    path('state/', views.StateList.as_view()),
    path('state/<int:pk>/', views.StateDetail.as_view()),
    path('company/', views.CompanyList.as_view()),
    path('company/<int:pk>/', views.CompanyDetail.as_view()),

]