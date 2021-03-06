"""news_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import news_api_app.urls
from news_api_app import views
from django.views.static import serve
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('api/customer/', include(news_api_app.urls)),
    path('admin/', admin.site.urls),
    # Frontend Paths #
    path('', views.login_user,name="login_user"),
    path('forgot_password/', views.forgot_password,name="forgot_password"),
    path('state/', views.state,name="state"),
    path('area/', views.district,name="district"),
    path('company/', views.company,name="company"),
    path('headline/', views.headline,name="headline"),
    path('magazine/', views.magzine_catagory,name="magzine_catagory"),
    path('news/', views.magzine,name="magzine"),
    path('sunday-magazine/', views.sunday_magzine,name="sunday_magzine"),
    path('city/', views.publish_newspaper,name="publish_newspaper"),
    path('user-logout/',views.user_logout, name="user_logout"),
    path('city/add/',views.Add_pubshnews,name='city/add'),
    path('get-companies', views.get_companies, name="get_companies"),
    path('get-cities', views.get_cities, name="get_cities"),
    path('company-upload', views.company_upload, name="company_upload"),
    path('city-upload', views.city_upload, name="city_upload"),
    path('multi-upload', views.multi_upload, name="multi_upload"),
    path('delete-all-city-pdf', views.delete_all_city_pdf, name="delete_all_city_pdf"),
    path('delete-all-company-pdf', views.delete_all_company_pdf, name="delete_all_company_pdf"),
    path('main-upload', views.main_upload, name="main_upload"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()



