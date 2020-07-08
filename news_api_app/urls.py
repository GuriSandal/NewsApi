from django.urls import path
from news_api_app import views

urlpatterns = [
    # API Paths #
    path('state/get-all-states', views.StateList.as_view(), name='get-all-states'),
    path('company/get-all-companies-from-state', views.CompaninesList.as_view(), name='companies-under-state'),
    path('city/get-city-from-company', views.CitiesList.as_view(), name='cities-under-company'),
    path('search/city-news', views.SearchCityNews.as_view(), name='search-city-news'),
    path('category/get-all-categories', views.MagazineCategoryList.as_view(), name='get-all-categories'),
    path('magazine/get-magazines-from-category', views.MagazineList.as_view(), name='get-magazines-from-category'),
    path('search/magazine-news', views.SearchMagazineList.as_view(), name='search-magazine-news'),
    path('get-all-sunday-magazines', views.SundayMagazineList.as_view(), name='all-sunday-magazines'),
    path('search/company-news',views.CompaninesPdfList.as_view(), name='search-company-news'),
    path('search/single-city',views.SingleCityList.as_view(), name="search-single-city"),

]