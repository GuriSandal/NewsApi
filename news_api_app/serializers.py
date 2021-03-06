from rest_framework import serializers
from .models import State,Headline,Companines, Cities, MagazineCategory, Magazine, SundayMagazine, CompaninesPdf

class HeadlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Headline
        fields = ['headlineText']

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['stateId','stateName', 'imageUlr']

class CompaninesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Companines
        fields = ['companyId','companyName','companyUrl','imageUlr']

class CompanyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompaninesPdf
        fields = ['companyId','companyName','pdfUlr','imageUlr']

class CitiesSerializer(serializers.ModelSerializer):
    companyName = serializers.StringRelatedField()
    class Meta:
        model = Cities
        fields = ['cityId','cityName','fileName','imageUrl','newsDate','companyName']

class SearchCompanyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompaninesPdf
        fields = ['companyId','companyName','newsDate','pdfUlr','imageUlr']

class MagazineCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MagazineCategory
        fields = ['categoryId','categoryName','imageUlr']

class MagazineSerializer(serializers.ModelSerializer):
    categoryName = serializers.StringRelatedField()
    class Meta:
        model = Magazine
        fields = ['magazineId','magazineName','fileName','imageUrl','newsDate','categoryName']

class SundayMagazineSerializer(serializers.ModelSerializer):
    class Meta:
        model = SundayMagazine
        fields = ['id','fileName','imageUrl','imageName','newsDate']

class CompaninesPdfSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompaninesPdf
        fields = ['companyName', 'pdfUlr', 'imageUlr', 'newsDate']
    
class SingleCitySerializer(serializers.ModelSerializer):
    companyName = serializers.StringRelatedField()
    class Meta:
        model = Cities
        fields = ['cityName',"fileName","imageUrl","newsDate","companyName"]