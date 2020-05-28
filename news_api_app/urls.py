from django.urls import path
from news_api_app import views

urlpatterns = [
    path('state/get-all-states/', views.state_list, name='all-state')
    # path('', views.ApiRoot.as_view(), name='root'),
    # path('state/', views.StateList.as_view(), name='all_states'),
    # path('state/<int:pk>/', views.StateDetail.as_view(), name='single_state'),
    # path('company/', views.CompanyList.as_view(), name='all_companies'),
    # path('company/<int:pk>/', views.CompanyDetail.as_view(), name='single_company'),

]