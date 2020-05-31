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

class Headline(models.Model):
    headlineId = models.AutoField(primary_key=True, editable=False)
    headlineText = models.CharField(max_length=50)
    isActive = models.BooleanField(default=False)
    addedOn = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.headlineText
    class Meta:
        verbose_name_plural = "Headlines"

class Companines(models.Model):
    companyId = models.AutoField(primary_key=True, editable=False)
    stateId = models.ForeignKey(State, on_delete=models.CASCADE)
    companyName = models.CharField(max_length=50)
    companyUrl = models.CharField(max_length=250,null=True,blank=True)
    pdfUlr = models.FileField(upload_to='CompanyPDFs/%Y/%m/%d',null=True)
    imageUlr = models.ImageField(upload_to = "CompaniesImages/%Y/%m/%d", null=True, blank=True)
    newsDate = models.CharField(max_length=20,validators =[date_validate],null=True)
    isActive = models.BooleanField(default=False)
    addedOn = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.companyName
    class Meta:
        verbose_name_plural = "Companies"

class Cities(models.Model):
    cityId = models.AutoField(primary_key=True, editable=False)
    cityName = models.CharField(max_length=50)
    fileName = models.FileField(upload_to='CityPDFs/%Y/%m/%d')
    imageUrl = models.ImageField(upload_to = "CompaniesImages/%Y/%m/%d", null=True, blank=True)
    newsDate = models.CharField(max_length=20,validators =[date_validate],null=True)
    companyName = models.ForeignKey(Companines, on_delete=models.CASCADE, null=True)
    isActive = models.BooleanField(default=False)
    addedOn = models.DateTimeField(auto_now_add=True)
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
    imageUrl = models.ImageField(upload_to = "MagazineImages/%Y/%m/%d", null=True, blank=True)
    categoryName = models.ForeignKey(MagazineCategory, on_delete=models.CASCADE)
    newsDate = models.CharField(max_length=20,validators =[date_validate])
    isActive = models.BooleanField(default=False)
    addedOn = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.magazineName
    class Meta:
        verbose_name_plural = 'Magazines'

class SundayMagazine(models.Model):
    magazineId = models.AutoField(primary_key=True, editable=False)
    magazineName = models.CharField(max_length=50)
    fileName = models.FileField(upload_to='SundayMagazinePDFs/%Y/%m/%d')
    imageUrl = models.ImageField(upload_to = "SundayMagazineImages/%Y/%m/%d", null=True, blank=True)
    newsDate = models.CharField(max_length=20,validators =[date_validate])
    isActive = models.BooleanField(default=False)
    addedOn = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.magazineName
    class Meta:
        verbose_name_plural = 'SundayMagazines'


# class District(models.Model):
#     state_id = models.ForeignKey(State, on_delete=models.CASCADE,blank=True, null=True)
#     name = models.CharField(max_length=50)
#     status = models.BooleanField(null=True,blank=True,default=False)
#     added_on = models.DateTimeField(auto_now=True)
#     def __str__(self):
#         return self.name
#     class Meta:
#         verbose_name_plural = "Districts"



# class PublishNewspaper(models.Model):
#     state_id = models.ForeignKey(State, on_delete=models.CASCADE, blank=True, null=True)
#     company_id = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
#     name = models.CharField(max_length=50)
#     file_url = models.FileField(upload_to='CompanyPDFs/%Y/%m/%d')
#     news_date = models.DateField()
#     status = models.BooleanField(default=False)
#     added_on = models.DateTimeField(auto_now=True)
#     def __str__(self):
#         return self.name
#     class Meta:
#         verbose_name_plural = 'PublishNewspapers'





