from django.shortcuts import get_object_or_404
from news_api_app.models import State, Headline, Companines,Cities, MagazineCategory, Magazine, SundayMagazine
from news_api_app.serializers import StateSerializer, HeadlineSerializer, CompaninesSerializer, CitiesSerializer, CompanyInfoSerializer, SearchCompanyInfoSerializer, MagazineCategorySerializer, MagazineSerializer, SundayMagazineSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class StateList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request):
        response_data = {}
        response_data["headlineText"] = Headline.objects.get(headlineId=2).headlineText
        response_data["stateList"] = StateSerializer(State.objects.order_by("stateName"), context={"request": request}, many=True).data
        return Response(response_data, status=status.HTTP_200_OK)

class CompaninesList(APIView):
    def get(self, request):
        state_id = request.GET['state_id']
        state = get_object_or_404(State,stateId=state_id)
        data = {}
        data["status"] = True
        data['companyList'] = CompaninesSerializer(Companines.objects.filter(stateId=state).order_by("companyName"), context={"request": request}, many=True).data
        return Response(data, status=status.HTTP_200_OK)

class CitiesList(APIView):
    def get(self, request):
        data = {}
        company_id = request.GET['company_id']
        company = get_object_or_404(Companines,companyId=company_id)
        data["status"] = True
        data['companyInfo'] = CompanyInfoSerializer(Companines.objects.filter(companyId=company_id), context={"request": request}, many=True).data
        data['cityList'] = CitiesSerializer(Cities.objects.filter(companyName=company).order_by("cityName"), context={"request": request}, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)


class SearchCityNews(APIView):
    def get(self, request):
        data = {}
        company_id = request.GET['company_id']
        search_date = request.GET['search_date']
        company = get_object_or_404(Companines,companyId=company_id)
        data["status"] = True
        data['companyInfo'] = SearchCompanyInfoSerializer(Companines.objects.filter(companyId=company_id,newsDate=search_date), context={"request": request}, many=True).data
        data['cityList'] = CitiesSerializer(Cities.objects.filter(companyName=company,newsDate=search_date).order_by("cityName"), context={"request": request}, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)

class MagazineCategoryList(APIView):
    def get(self, request):
        data = {}
        data["categoryList"] = MagazineCategorySerializer(MagazineCategory.objects.order_by("categoryName"), context={"request": request}, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)

class MagazineList(APIView):
    def get(self, request):
        data = {}
        category_id = request.GET['category_id']
        category = get_object_or_404(MagazineCategory, categoryId=category_id)
        data["status"] = True
        data["magazineList"] = MagazineSerializer(Magazine.objects.filter(categoryName=category).order_by("magazineName"), context={"request": request}, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)

class SearchMagazineList(APIView):
    def get(self, request):
        data = {}
        category_id = request.GET['category_id']
        search_date = request.GET['search_date']
        category = get_object_or_404(MagazineCategory, categoryId=category_id)
        data["status"] = True
        data["magazineList"] = MagazineSerializer(Magazine.objects.filter(categoryName=category,newsDate=search_date).order_by("magazineName"), context={"request": request}, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)

class SundayMagazineList(APIView):
    def get(self, request):
        data = {}
        data["status"] = True
        data['sundayMagazineList'] = SundayMagazineSerializer(SundayMagazine.objects.order_by("magazineName"),context={"request": request}, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)