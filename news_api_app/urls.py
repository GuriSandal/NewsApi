from django.urls import path, include
from news_api_app import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'states', views.StateViewSet)
router.register(r'companies', views.CompanyViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('', views.ApiRoot.as_view(), name='root'),
    # path('state/', views.StateList.as_view(), name='all_states'),
    # path('state/<int:pk>/', views.StateDetail.as_view(), name='single_state'),
    # path('company/', views.CompanyList.as_view(), name='all_companies'),
    # path('company/<int:pk>/', views.CompanyDetail.as_view(), name='single_company'),

]