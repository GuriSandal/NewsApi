from django.db import models
import datetime
from django.core.exceptions import ValidationError 

# Create your models here.
def date_validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%d-%m-%Y')
    except:
        raise ValidationError("Incorrect data format, should be DD-MM-YYYY")

class State(models.Model):
    stateId = models.AutoField(primary_key=True, editable=False)
    stateName = models.CharField(max_length=50)
    imageUlr = models.ImageField(upload_to = "StatesImages/%Y/%m/%d", null=True, blank=True)
    isActive = models.BooleanField(null=True,blank=True,default=False)
    addedOn = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.stateName
    class Meta:
        verbose_name_plural = "States"

class District(models.Model):
    districtId = models.AutoField(primary_key=True, editable=False)
    stateName = models.ForeignKey(State, on_delete=models.CASCADE,blank=True, null=True)
    districtName = models.CharField(max_length=50)
    isActive = models.BooleanField(null=True,blank=True,default=False)
    addedOn = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.districtName
    class Meta:
        verbose_name_plural = "Districts"

class Headline(models.Model):
    headlineId = models.AutoField(primary_key=True, editable=False)
    headlineText = models.CharField(max_length=50)
    isActive = models.BooleanField(default=False)
    addedOn = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.headlineText
    class Meta:
        verbose_name_plural = "Headlines"

class Companines(models.Model):
    companyId = models.AutoField(primary_key=True, editable=False)
    stateId = models.ForeignKey(State, on_delete=models.CASCADE)
    districtNames = models.ManyToManyField(District) 
    companyName = models.CharField(max_length=50)
    companyUrl = models.CharField(max_length=250,null=True,blank=True)
    imageUlr = models.ImageField(upload_to = "CompaniesImages/%Y/%m/%d", null=True, blank=True)
    isActive = models.BooleanField(default=False)
    addedOn = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.companyName
    class Meta:
        verbose_name_plural = "Companies"

class CompaninesPdf(models.Model):
    companyId = models.ForeignKey(Companines,on_delete=models.CASCADE,blank=True, null=True)
    companypdfId = models.AutoField(primary_key=True, editable=False)
    companyName = models.CharField(max_length=50)
    stateId = models.ForeignKey(State,on_delete=models.CASCADE, null=True)
    pdfUlr = models.FileField(upload_to='CompanyPDFs/%Y/%m/%d',null=True,blank=True)
    imageUlr = models.ImageField(upload_to="CompanyNewsImages", null=True)
    newsDate = models.CharField(max_length=20,validators =[date_validate],null=True, blank=True)
    isActive = models.BooleanField(default=False)
    addedOn = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.companyName
    class Meta:
        verbose_name_plural = "CompaninesPdfs"


class Cities(models.Model):
    cityId = models.AutoField(primary_key=True, editable=False)
    cityName = models.CharField(max_length=50)
    fileName = models.FileField(upload_to='CityPDFs/%Y/%m/%d')
    imageUrl = models.ImageField(upload_to='CityNewsImages', null=True)
    newsDate = models.CharField(max_length=20,validators =[date_validate],null=True)
    companyName = models.ForeignKey(Companines, on_delete=models.CASCADE, null=True)
    isActive = models.BooleanField(default=False)
    addedOn = models.DateTimeField(auto_now_add=True)
    stateId = models.ForeignKey(State,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.cityName
    class Meta:
        verbose_name_plural = "Cities"

class MagazineCategory(models.Model):
    categoryId = models.AutoField(primary_key=True, editable=False)
    categoryName = models.CharField(max_length=50)
    imageUlr = models.ImageField(upload_to = "MagazineCategoryImages/%Y/%m/%d", null=True, blank=True)
    isActive = models.BooleanField(default=False)
    addedOn = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.categoryName
    class Meta:
        verbose_name_plural = 'MagazineCategories'

class Magazine(models.Model):
    magazineId = models.AutoField(primary_key=True, editable=False)
    magazineName = models.CharField(max_length=50)
    fileName = models.FileField(upload_to='MagazinePDFs/%Y/%m/%d')
    imageUrl = models.ImageField(upload_to="MagazineImages", null=True)
    categoryName = models.ManyToManyField(MagazineCategory)
    newsDate = models.CharField(max_length=20,validators =[date_validate])
    isActive = models.BooleanField(default=False)
    addedOn = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.magazineName
    class Meta:
        verbose_name_plural = 'Magazines'

class SundayMagazine(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    magazineName = models.CharField(max_length=50)
    fileName = models.FileField(upload_to='SundayMagazinePDFs/%Y/%m/%d')
    imageUrl = models.ImageField(upload_to='SundayMagazineImages', null=True)
    imageName = models.CharField(max_length=200, null=True)
    newsDate = models.CharField(max_length=20,validators =[date_validate])
    isActive = models.BooleanField(default=False)
    addedOn = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.magazineName
    class Meta:
        verbose_name_plural = 'SundayMagazines'










