from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from news_api_app.models import State, Headline, Companines,Cities, MagazineCategory, Magazine, SundayMagazine, District, CompaninesPdf
from news_api_app.serializers import StateSerializer, HeadlineSerializer, CompaninesSerializer, CitiesSerializer, CompanyInfoSerializer, SearchCompanyInfoSerializer, MagazineCategorySerializer, MagazineSerializer, SundayMagazineSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from django.contrib.auth import login, logout, authenticate
import os
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


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
        data['companyInfo'] = CompanyInfoSerializer(CompaninesPdf.objects.filter(companyId=company), context={"request": request}, many=True).data
        data['cityList'] = CitiesSerializer(Cities.objects.filter(companyName=company).order_by("cityName"), context={"request": request}, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)


class SearchCityNews(APIView):
    def get(self, request):
        data = {}
        company_id = request.GET['company_id']
        search_date = request.GET['search_date']
        company = get_object_or_404(Companines,companyId=company_id)
        data["status"] = True
        data['companyInfo'] = SearchCompanyInfoSerializer(CompaninesPdf.objects.filter(companyId=company,newsDate=search_date), context={"request": request}, many=True).data
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
    context = {}
    headline = Headline.objects.get(headlineId=2)
    context["headline"] = headline

    if request.method == "POST":
        headlineText = request.POST["headlineText"]

        if "updateActive" in request.POST:
            headline.headlineText = headlineText
            headline.isActive = True
            headline.save()
        else:
            headline.headlineText = headlineText
            headline.isActive = False
            headline.save()
        context["status"] = "Headline Update Successfully!"

    return render(request,'headline.html', context)

import fitz
def magzine(request):
    context = {}
    magazines = Magazine.objects.order_by("magazineName")
    context["magazines"] = magazines

    categories = MagazineCategory.objects.filter(isActive=True).order_by("categoryName")
    context["categories"] = categories


    if request.method == "POST":
        if "add" in request.POST:
            name = request.POST["magazineName"]
            date = request.POST["date"]
            categorieIds_list = request.POST.getlist('catagoryIds')
            
            categorie_list = [get_object_or_404(MagazineCategory, categoryId=i) for i in categorieIds_list]
            
            if "addActive" in request.POST:
                if "fileName" in request.FILES:
                    fileName = request.FILES["fileName"]
                    image = "MagazineImages/"+str(fileName).split(".")[0]+".png"
                    magazine = Magazine(magazineName=name,fileName=fileName,imageUrl=image,newsDate=date,isActive=True)
                    magazine.save()
                    
                    pdffile = settings.MEDIA_ROOT+"/"+str(magazine.fileName)
                    doc = fitz.open(pdffile)
                    page = doc.loadPage(0) #number of page
                    pix = page.getPixmap()
                    output = str(fileName).split(".")
                    output = output[0]+".png"
                    pix.writePNG(settings.MEDIA_ROOT+"/MagazineImages/"+output)
                    
                    for i in categorie_list:
                        magazine.categoryName.add(i)
            else:
                if "fileName" in request.FILES:
                    fileName = request.FILES["fileName"]
                    image = "MagazineImages/"+str(fileName).split(".")[0]+".png"
                    magazine = Magazine(magazineName=name,fileName=fileName,imageUrl=image,newsDate=date,isActive=False)
                    magazine.save()
                    
                    pdffile = settings.MEDIA_ROOT+"/"+str(magazine.fileName)
                    doc = fitz.open(pdffile)
                    page = doc.loadPage(0) #number of page
                    pix = page.getPixmap()
                    output = str(fileName).split(".")
                    output = output[0]+".png"
                    pix.writePNG(settings.MEDIA_ROOT+"/MagazineImages/"+output)

                    for i in categorie_list:
                        magazine.categoryName.add(i)

            context["status"] = "{} added successfully!".format(name)

        if "update" in request.POST:
            name = request.POST["magazineName"]
            date = request.POST["date"]
          
            Id = request.POST['id']

            categorieIds_list = request.POST.getlist('catagoryIds')
            
            categorie_list = [get_object_or_404(MagazineCategory, categoryId=i) for i in categorieIds_list]

            magazine = Magazine.objects.get(magazineId=Id)
            if "updateActive" in request.POST:    
                if "fileName" in request.FILES:
                    fileName = request.FILES["fileName"]
                    image = "MagazineImages/"+str(fileName).split(".")[0]+".png"
                    magazine.magazineName=name
                    magazine.fileName=fileName
                    magazine.imageUrl=image
                    magazine.newsDate=date
                    magazine.isActive=True
                    magazine.save()

                    pdffile = settings.MEDIA_ROOT+"/"+str(magazine.fileName)
                    doc = fitz.open(pdffile)
                    page = doc.loadPage(0) #number of page
                    pix = page.getPixmap()
                    output = str(fileName).split(".")
                    output = output[0]+".png"
                    pix.writePNG(settings.MEDIA_ROOT+"/MagazineImages/"+output)

                    for i in categorie_list:
                        magazine.categoryName.add(i)
                else:
                    magazine.magazineName=name
                    magazine.newsDate=date
                    magazine.isActive=True
                    magazine.save()
                    for i in categorie_list:
                        magazine.categoryName.add(i)

            else:
                if "fileName" in request.FILES:
                    fileName = request.FILES["fileName"]
                    image = "MagazineImages/"+str(fileName).split(".")[0]+".png"
                    magazine.magazineName=name
                    magazine.fileName=fileName
                    magazine.imageUrl=image
                    magazine.newsDate=date
                    magazine.isActive=False
                    magazine.save()

                    pdffile = settings.MEDIA_ROOT+"/"+str(magazine.fileName)
                    doc = fitz.open(pdffile)
                    page = doc.loadPage(0) #number of page
                    pix = page.getPixmap()
                    output = str(fileName).split(".")
                    output = output[0]+".png"
                    pix.writePNG(settings.MEDIA_ROOT+"/MagazineImages/"+output)
                    for i in categorie_list:
                        magazine.categoryName.add(i)
                else:
                    magazine.magazineName=name
                    magazine.newsDate=date
                    magazine.isActive=False
                    magazine.save()
                    for i in categorie_list:
                        magazine.categoryName.add(i)

            context["status"] = "{} Update successfully!".format(name)

        if "delete" in request.POST:
            magazineId = request.POST["magazineId"]
            magazine = get_object_or_404(Magazine, magazineId=magazineId)
            magazine.delete()
            context["status"] = "{} Deleted Sucessfully!".format(magazine.magazineName)
    return render(request,'magzine.html', context)

def magzine_catagory(request):
    context = {}
    categories = MagazineCategory.objects.order_by("categoryName")
    context["categories"] = categories

    if request.method == "POST":
        if 'add' in request.POST:
            categoryName = request.POST['categoryName']
            if "isActive" in request.POST:
                if "categoryImage" in request.FILES:
                    categoryImage = request.FILES["categoryImage"]
                    category = MagazineCategory(categoryName=categoryName, isActive=True, imageUlr=categoryImage)
                    category.save()
                else:
                    category = MagazineCategory(categoryName=categoryName, isActive=True)
                    category.save()
            else:
                if "categoryImage" in request.FILES:
                    categoryImage = request.FILES["categoryImage"]
                    category = MagazineCategory(categoryName=categoryName, isActive=False, imageUlr=categoryImage)
                    category.save()
                else:
                    category = MagazineCategory(categoryName=categoryName, isActive=False)
                    category.save()

            context["status"] = "New Category Added!"
        
        if "update" in request.POST:
            categoryId = request.POST["categoryId"]
            categoryName = request.POST['categoryName']
            
            category = MagazineCategory.objects.get(categoryId=categoryId)
            
            if "isActive" in request.POST:
                category.categoryName = categoryName
                category.isActive = True
                category.save()
                if "categoryImage" in request.FILES:
                    try:
                        os.remove(settings.MEDIA_ROOT+"/"+str(category.imageUlr))
                    except:
                        pass
                    categoryImage = request.FILES["categoryImage"]
                    category.imageUlr = categoryImage
                    category.save()
            else:
                category.categoryName = categoryName
                category.isActive = False
                category.save()
                if "categoryImage" in request.FILES:
                    try:
                        os.remove(settings.MEDIA_ROOT+"/"+str(category.imageUlr))
                    except:
                        pass
                    categoryImage = request.FILES["categoryImage"]
                    category.imageUlr = categoryImage
                    category.save()
            context["status"] = "Update {} Sucessfully!".format(category.categoryName)
        
        if "delete" in request.POST:
            categoryId = request.POST["categoryId"]
            category = get_object_or_404(MagazineCategory, categoryId=categoryId)
            try:
                os.remove(settings.MEDIA_ROOT+"/"+str(category.imageUlr))
            except:
                pass
            category.delete()
            context["status"] = "{} Deleted Sucessfully!".format(category.categoryName)

    return render(request,"magzine_catagory.html", context)

def sunday_magzine(request):
    context = {}
    magazines = SundayMagazine.objects.order_by("magazineName")
    context["magazines"] = magazines

    if request.method == "POST":
        if "add" in request.POST:
            name = request.POST["magazineName"]
            date = request.POST["date"]
          
            if "addActive" in request.POST:    
                if "fileName" in request.FILES:
                    fileName = request.FILES["fileName"]
                    imageUrl = "SundayMagazineImages/"+str(fileName).split(".")[0]+".png"
                    magazine = SundayMagazine(magazineName=name,fileName=fileName,imageUrl=imageUrl,newsDate=date,isActive=True)
                    magazine.save()
                    pdffile = settings.MEDIA_ROOT+"/"+str(magazine.fileName)
                    doc = fitz.open(pdffile)
                    page = doc.loadPage(0) #number of page
                    pix = page.getPixmap()
                    output = str(fileName).split(".")
                    output = output[0]+".png"
                    pix.writePNG(settings.MEDIA_ROOT+"/SundayMagazineImages/"+output)
            else:
                if "fileName" in request.FILES:
                    fileName = request.FILES["fileName"]
                    imageUrl = "SundayMagazineImages/"+str(fileName).split(".")[0]+".png"
                    magazine = SundayMagazine(magazineName=name,fileName=fileName,imageUrl=imageUrl,newsDate=date,isActive=False)
                    magazine.save()
                    pdffile = settings.MEDIA_ROOT+"/"+str(magazine.fileName)
                    doc = fitz.open(pdffile)
                    page = doc.loadPage(0) #number of page
                    pix = page.getPixmap()
                    output = str(fileName).split(".")
                    output = output[0]+".png"
                    pix.writePNG(settings.MEDIA_ROOT+"/SundayMagazineImages/"+output)
            context["status"] = "{} added successfully!".format(name)
        
        if "update" in request.POST:
            name = request.POST["magazineName"]
            date = request.POST["date"]
          
            Id = request.POST['id']
            magazine = SundayMagazine.objects.get(magazineId=Id)
            if "updateActive" in request.POST:    
                if "fileName" in request.FILES:
                    fileName = request.FILES["fileName"]
                    imageUrl = "SundayMagazineImages/"+str(fileName).split(".")[0]+".png"
                    magazine.magazineName=name
                    magazine.fileName=fileName
                    magazine.imageUrl=imageUrl
                    magazine.newsDate=date
                    magazine.isActive=True
                    magazine.save()
                    pdffile = settings.MEDIA_ROOT+"/"+str(magazine.fileName)
                    doc = fitz.open(pdffile)
                    page = doc.loadPage(0) #number of page
                    pix = page.getPixmap()
                    output = str(fileName).split(".")
                    output = output[0]+".png"
                    pix.writePNG(settings.MEDIA_ROOT+"/SundayMagazineImages/"+output)
                else:
                    magazine.magazineName=name
                    magazine.newsDate=date
                    magazine.isActive=True
                    magazine.save()

            else:
                if "fileName" in request.FILES:
                    fileName = request.FILES["fileName"]
                    imageUrl = "SundayMagazineImages/"+str(fileName).split(".")[0]+".png"
                    magazine.magazineName=name
                    magazine.fileName=fileName
                    magazine.imageUrl=imageUrl
                    magazine.newsDate=date
                    magazine.isActive=False
                    magazine.save()
                    pdffile = settings.MEDIA_ROOT+"/"+str(magazine.fileName)
                    doc = fitz.open(pdffile)
                    page = doc.loadPage(0) #number of page
                    pix = page.getPixmap()
                    output = str(fileName).split(".")
                    output = output[0]+".png"
                    pix.writePNG(settings.MEDIA_ROOT+"/SundayMagazineImages/"+output)
                else:
                    magazine.magazineName=name
                    magazine.newsDate=date
                    magazine.isActive=False
                    magazine.save()

            context["status"] = "{} Update successfully!".format(name)

        if "delete" in request.POST:
            magazineId = request.POST["magazineId"]
            magazine = get_object_or_404(SundayMagazine, magazineId=magazineId)
            magazine.delete()
            context["status"] = "{} Deleted Sucessfully!".format(magazine.magazineName)
    return render(request,"sunday_magzine.html", context)



def publish_newspaper(request):
    from datetime import date
    context = {}
    cities = Cities.objects.order_by("-newsDate")
    context["cities"] = cities

    states = State.objects.filter(isActive=True).order_by("stateName")
    context["states"] = states

    companies = Companines.objects.filter(isActive=True).order_by("companyName")
    context["companies"] = companies

    today = date.today()
    today_date = today.strftime("%d-%m-%Y")
    context["today_date"] = today_date

    if request.method == "POST":
        if "update" in request.POST:
            cityName = request.POST["cityName"]
            date = request.POST["date"]

            companyId = request.POST["companyId"]
            company = get_object_or_404(Companines, companyId=companyId)
            
            cityId = request.POST["id"]
            city = get_object_or_404(Cities, cityId=cityId)
            
            if "updateActive" in request.POST:
                if "file" in request.FILES:
                    fileName = request.FILES["file"]
                    imageUrl = "CityNewsImages/"+str(fileName).split(".")[0]+".png"
                    city.cityName = cityName
                    city.fileName = fileName
                    city.imageUrl = imageUrl
                    city.newsDate = date
                    city.companyName = company
                    city.isActive = True
                    city.save()
                    pdffile = settings.MEDIA_ROOT+"/"+str(city.fileName)
                    doc = fitz.open(pdffile)
                    page = doc.loadPage(0) #number of page
                    pix = page.getPixmap()
                    output = str(fileName).split(".")
                    output = output[0]+".png"
                    pix.writePNG(settings.MEDIA_ROOT+"/CityNewsImages/"+output)
                else:
                    city.cityName = cityName
                    city.newsDate = date
                    city.companyName = company
                    city.isActive = True
                    city.save()
            else:
                if "file" in request.FILES:
                    fileName = request.FILES["file"]
                    imageUrl = "CityNewsImages/"+str(fileName).split(".")[0]+".png"
                    city.cityName = cityName
                    city.fileName = fileName
                    city.imageUrl = imageUrl
                    city.newsDate = date
                    city.companyName = company
                    city.isActive = False
                    city.save()
                    pdffile = settings.MEDIA_ROOT+"/"+str(city.fileName)
                    doc = fitz.open(pdffile)
                    page = doc.loadPage(0) #number of page
                    pix = page.getPixmap()
                    output = str(fileName).split(".")
                    output = output[0]+".png"
                    pix.writePNG(settings.MEDIA_ROOT+"/CityNewsImages/"+output)
                else:
                    city.cityName = cityName
                    city.newsDate = date
                    city.companyName = company
                    city.isActive = False
                    city.save()
            context["status"] = "{} Update successfully!".format(city.cityName)  

        if "search" in request.POST:
            stateId = request.POST["stateId"] 
            companyId = request.POST["companyId"] 
            print(companyId)
            date = request.POST["date"] 
            
            if len(date)>0 and len(companyId)>0:
                state = State.objects.get(stateId=stateId)
                company = Companines.objects.get(companyId=companyId)
                cities = Cities.objects.filter(stateId=state,companyName=company,newsDate=date).order_by("-newsDate")
                context["cities"] = cities
            elif len(date)>0:
                cities = Cities.objects.filter(newsDate=date).order_by("-newsDate")
                context["cities"] = cities
            elif len(companyId)>0:
                state = State.objects.get(stateId=stateId)
                company = Companines.objects.get(companyId=companyId)
                cities = Cities.objects.filter(stateId=state,companyName=company).order_by("-newsDate")
                context["cities"] = cities 
            elif len(stateId)>0:
                state = State.objects.get(stateId=stateId)
                cities = Cities.objects.filter(stateId=state).order_by("-newsDate")
                context["cities"] = cities

            
                

    
    return render(request,"publish_newspaper.html", context)

def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/")



def Add_pubshnews(request):
    from datetime import date
    context = {}
    today = date.today()
    today_date = today.strftime("%d-%m-%Y")
    context["today_date"] = today_date

    states = State.objects.filter(isActive=True).order_by("stateName")
    context["states"] = states
    return render(request,"Add_Publishnewspaper.html", context)

def get_companies(request):
    state_id = request.GET["state_id"]
    state = get_object_or_404(State, stateId=state_id)
    companines = Companines.objects.filter(stateId=state,isActive=True).order_by("companyName")
    companyInfo = []
    
    for company in companines:
        context = {}
        context["companyId"] = company.companyId
        context["companyName"] = company.companyName
        companyInfo.append(context)
    return JsonResponse({"companies":companyInfo})

def get_cities(request):
    context = {}
    company_id = request.GET["company_id"]
    date = request.GET["date"]
    company = get_object_or_404(Companines, companyId=company_id)
    district_list = [district.districtName for district in company.districtNames.all()]
    context["district_list"] = district_list
    try:
        cities = Cities.objects.filter(newsDate=date, companyName=company)
        added_city = [city.cityName for city in cities]    
        companypdf = CompaninesPdf.objects.get(companyId=company_id, newsDate=date)
        companyId = companypdf.companyId.companyId
        context["added_city"] = added_city
        context["companyId"] = companyId
        context["date"] = date
    except:
        context["added_city"] = ""
        context["companyId"] = ""
        context["date"] = ""

    return JsonResponse(context)

@csrf_exempt
def upload_main(request):
    if request.method == "POST":
        if len(request.POST["companyId"]) > 0:
            if "main_file" in request.FILES:
                main_file = request.FILES["main_file"]
                if str(main_file).split(".")[-1] == "pdf":
                    companyId = request.POST["companyId"]
                    stateId = request.POST["stateId"]
                    date = request.POST["date"]
                    imageUlr = "MianNewsImages/"+str(main_file).split(".")[0]+".png"
                    company = get_object_or_404(Companines, companyId=companyId)
                    state = get_object_or_404(State, stateId=stateId)
                    pdf = CompaninesPdf(companyId=company,stateId=state, companyName=company.companyName, pdfUlr=main_file, newsDate=date, imageUlr=imageUlr, isActive=True)
                    pdf.save()
                    pdffile = settings.MEDIA_ROOT+"/"+str(pdf.pdfUlr)
                    doc = fitz.open(pdffile)
                    page = doc.loadPage(0) #number of page
                    pix = page.getPixmap()
                    output = str(main_file).split(".")
                    output = output[0]+".png"
                    pix.writePNG(settings.MEDIA_ROOT+"/MianNewsImages/"+output)
                    return JsonResponse({"status":"success","msg":date,"color":"text-success"})
                else:
                    return JsonResponse({"status":"success","msg":"File should be in pdf format!!"})
            else:
                return JsonResponse({"status":"error","msg":"Uploading Error!!"})
        else:
            return JsonResponse({"status":"error","msg":"Select Company First!!"})
    
@csrf_exempt
def city_upload(request):
    if request.method == "POST":
        if "city_file" in request.FILES:
            city_file = request.FILES["city_file"]
            if str(city_file).split(".")[-1] == "pdf":
                cityName = request.POST["cityName"]
                stateId = request.POST["stateId"]
                date = request.POST["date"]
                companyId = request.POST["companyId"]
                imageUrl = "CityNewsImages/"+str(city_file).split(".")[0]+".png"
                company = get_object_or_404(Companines, companyId=companyId)
                state = get_object_or_404(State, stateId=stateId)
                pdf = Cities(companyName=company, stateId=state, cityName=cityName, fileName=city_file, newsDate=date, imageUrl=imageUrl, isActive=True)
                pdf.save()
                pdffile = settings.MEDIA_ROOT+"/"+str(pdf.fileName)
                doc = fitz.open(pdffile)
                page = doc.loadPage(0) #number of page
                pix = page.getPixmap()
                output = str(city_file).split(".")
                output = output[0]+".png"
                pix.writePNG(settings.MEDIA_ROOT+"/CityNewsImages/"+output)
                return JsonResponse({"status":"success","msg":date}) 
            else:
                return JsonResponse({"status":"error","msg":"File should be in pdf format!!"})
        else:
            return JsonResponse({"status":"error","msg":"Uploading Error!!"})   
          