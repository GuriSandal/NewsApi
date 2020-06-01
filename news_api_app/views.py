from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from news_api_app.models import State, Headline, Companines,Cities, MagazineCategory, Magazine, SundayMagazine, District
from news_api_app.serializers import StateSerializer, HeadlineSerializer, CompaninesSerializer, CitiesSerializer, CompanyInfoSerializer, SearchCompanyInfoSerializer, MagazineCategorySerializer, MagazineSerializer, SundayMagazineSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from django.contrib.auth import login, logout, authenticate
import os
from django.conf import settings

# API END #
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



# Front End #

def login_user(request):
    if request.method == "POST":
        uname = request.POST["username"]
        pas = request.POST["password"]
        user = authenticate(username=uname, password=pas)
        if user:
            login(request,user)
            return HttpResponseRedirect("/state/")
        else:
           return render(request, 'login_user.html', {"status":"Invalid Username or Password !"} ) 
    return render(request,'login_user.html')


def forgot_password(request):
    return render(request,'forgot_password.html')


def state(request):
    context = {}
    isActive = ''
    states = State.objects.order_by("stateName")
    context['states'] = states
    if request.method == "POST":
        if 'add' in request.POST:
            stateName = request.POST['stateName']
            try:
                isActive = request.POST['isActive']
            except:
                pass

            if "stateImage" in request.FILES:
                stateImage = request.FILES["stateImage"]
                if isActive == '1':
                    state = State(stateName=stateName, isActive=True, imageUlr=stateImage)
                    state.save()
                else:
                    state = State(stateName=stateName, imageUlr=stateImage)
                    state.save()

            else:
                if isActive == '1':
                    state = State(stateName=stateName, isActive=True)
                    state.save()
                else:
                    state = State(stateName=stateName)
                    state.save()
                
            context["status"] = "New State Added!"
        
        if "update" in request.POST:
            stateId = request.POST["stateId"]
            stateName = request.POST['stateName']
            
            state = State.objects.get(stateId=stateId)
            
            if "isActive" in request.POST:
                state.stateName = stateName
                state.isActive = True
                state.save()
                if "stateImage" in request.FILES:
                    try:
                        os.remove(settings.MEDIA_ROOT+"/"+str(state.imageUlr))
                    except:
                        pass
                    stateImage = request.FILES["stateImage"]
                    state.imageUlr = stateImage
                    state.save()
            else:
                state.stateName = stateName
                state.isActive = False
                state.save()
                if "stateImage" in request.FILES:
                    try:
                        os.remove(settings.MEDIA_ROOT+"/"+str(state.imageUlr))
                    except:
                        pass
                    stateImage = request.FILES["stateImage"]
                    state.imageUlr = stateImage
                    state.save()
            context["status"] = "Update {} Sucessfully!".format(state.stateName)
        
        if "delete" in request.POST:
            stateId = request.POST["stateId"]
            state = get_object_or_404(State, stateId=stateId)
            try:
                os.remove(settings.MEDIA_ROOT+"/"+str(state.imageUlr))
            except:
                pass
            state.delete()
            context["status"] = "{} Deleted Sucessfully!".format(state.stateName)
        
    return render(request,'state.html', context)


def district(request):
    context = {}
    
    districts = District.objects.order_by("districtName")
    context["districts"] = districts

    states = State.objects.filter(isActive=True).order_by("stateName")
    context['states'] = states

    if request.method == "POST":
        if "add" in request.POST:
            districtName = request.POST["districtName"]
            stateId = request.POST["stateId"]
            
            state = get_object_or_404(State, stateId=stateId)
            
            if "addActive" in request.POST:
                district = District(districtName=districtName, stateName=state, isActive=True)
                district.save()
            else:
                district = District(districtName=districtName, stateName=state)
                district.save()

            context["status"] = "{} Added Successfully!".format(districtName)

        if "update" in request.POST:
            districtName = request.POST["districtName"]
            districtId = request.POST["districtId"]
            stateId = request.POST["stateId"]

            state = get_object_or_404(State, stateId=stateId)
            
            district = get_object_or_404(District, districtId=districtId)

            if "updateActive" in request.POST:
                district.districtName = districtName
                district.stateName = state
                district.isActive = True
                district.save()
            else:
                district.districtName = districtName
                district.stateName = state
                district.isActive = False
                district.save()

            context["status"] = "{} update Successfully!".format(district.districtName)

        if "delete" in request.POST:
            districtId = request.POST["districtId"]
            district = get_object_or_404(District, districtId=districtId)
            district.delete()
            context["status"] = "{} Deleted Sucessfully!".format(district.districtName)

    return render(request,'District.html',context)


def company(request):
    context = {}

    companies = Companines.objects.order_by("companyName")
    context["companies"] = companies

    districts = District.objects.filter(isActive=True).order_by("districtName")
    context["districts"] = districts

    states = State.objects.filter(isActive=True).order_by("stateName")
    context['states'] = states

    if request.method == "POST":
        if "add" in request.POST:
            companyName = request.POST["companyName"]
            companyUrl = request.POST["companyUrl"]
            districtIds_list = request.POST.getlist('districtIds')
            stateId = request.POST["stateId"]
            
            state = get_object_or_404(State, stateId=stateId)    

            district_list = [get_object_or_404(District, districtId=i) for i in districtIds_list]

            if "addActive" in request.POST:
                if "imageUrl" in request.FILES:
                    imageUrl = request.FILES["imageUrl"]
                    company = Companines(companyName=companyName)
                    company.companyUrl = companyUrl
                    company.stateId = state
                    print(imageUrl)
                    company.imageUlr = imageUrl
                    company.isActive = True
                    company.save()
                    for i in district_list:
                        company.districtNames.add(i)
                else:
                    company = Companines(companyName=companyName)
                    company.companyUrl = companyUrl
                    company.stateId = state
                    company.isActive = True
                    company.save()
                    for i in district_list:
                        company.districtNames.add(i)
            else:
                if "imageUrl" in request.FILES:
                    imageUrl = request.FILES["imageUrl"]
                    company = Companines(companyName=companyName)
                    company.companyUrl = companyUrl
                    company.stateId = state
                    company.imageUlr = imageUrl
                    company.isActive = False
                    company.save()
                    for i in district_list:
                        company.districtNames.add(i)
                else:
                    company = Companines(companyName=companyName)
                    company.companyUrl = companyUrl
                    company.stateId = state
                    company.isActive = False
                    company.save()
                    for i in district_list:
                        company.districtNames.add(i)
                        
            context["status"] = "{} Added Successfully!".format(companyName)

        if "update" in request.POST:
            companyId = request.POST["companyId"]
            companyName = request.POST["companyName"]
            companyUrl = request.POST["companyUrl"]
            districtIds_list = request.POST.getlist('districtIds')
            stateId = request.POST["stateId"]

            company = get_object_or_404(Companines, companyId=companyId)

            state = get_object_or_404(State, stateId=stateId)    

            district_list = [get_object_or_404(District, districtId=i) for i in districtIds_list]

            if "updateActive" in request.POST:
                if "imageUrl" in request.FILES:
                    try:
                        os.remove(settings.MEDIA_ROOT+"/"+str(company.imageUlr))
                    except:
                        pass
                    imageUrl = request.FILES["imageUrl"]
                    company.companyName=companyName
                    company.companyUrl = companyUrl
                    company.stateId = state
                    company.imageUlr = imageUrl
                    company.isActive = True
                    company.save()
                    for i in district_list:
                        company.districtNames.add(i)
                else:
                    company.companyName=companyName
                    company.companyUrl = companyUrl
                    company.stateId = state
                    company.isActive = True
                    company.save()
                    for i in district_list:
                        company.districtNames.add(i)
            else:
                if "imageUrl" in request.FILES:
                    try:
                        os.remove(settings.MEDIA_ROOT+"/"+str(company.imageUlr))
                    except:
                        pass
                    imageUrl = request.FILES["imageUrl"]
                    company.companyName=companyName
                    company.companyUrl = companyUrl
                    company.stateId = state
                    company.imageUlr = imageUrl
                    company.isActive = False
                    company.save()
                    for i in district_list:
                        company.districtNames.add(i)
                else:
                    company.companyName=companyName
                    company.companyUrl = companyUrl
                    company.stateId = state
                    company.isActive = False
                    company.save()
                    for i in district_list:
                        company.districtNames.add(i)
                        
            context["status"] = "{} Update Successfully!".format(company.companyName)

        if "delete" in request.POST:
            companyId = request.POST["companyId"]
            company = get_object_or_404(Companines, companyId=companyId)
            try:
                os.remove(settings.MEDIA_ROOT+"/"+str(company.imageUlr))
            except:
                pass
            company.delete()
            context["status"] = "{} Deleted Sucessfully!".format(company.companyName)

    return render(request,'Publication_house.html',context)

def headline(request):
    return render(request,'headline.html')
def magzine(request):
    return render(request,'magzine.html')
def magzine_catagory(request):
    return render(request,"magzine_catagory.html")
def sunday_magzine(request):
    return render(request,"sunday_magzine.html")

def publish_newspaper(request):
    return render(request,"publish_newspaper.html")

def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/")
    