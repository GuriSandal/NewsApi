from django.db import models

# Create your models here.

class State(models.Model):
    stateId = models.AutoField(primary_key=True, editable=False)
    stateName = models.CharField(max_length=50)
    imageUlr = models.ImageField(upload_to = "StatesImages/%Y/%m/%d", null=True, blank=True)
    isActive = models.BooleanField(null=True,blank=True,default=False)
    addedOn = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.stateName

class Headline(models.Model):
    headlineId = models.AutoField(primary_key=True, editable=False)
    headlineText = models.CharField(max_length=50)
    isActive = models.BooleanField(default=False)
    addedOn = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.headlineText
 
# class District(models.Model):
#     state_id = models.ForeignKey(State, on_delete=models.CASCADE,blank=True, null=True)
#     name = models.CharField(max_length=50)
#     status = models.BooleanField(null=True,blank=True,default=False)
#     added_on = models.DateTimeField(auto_now=True)
#     def __str__(self):
#         return self.name
#     class Meta:
#         verbose_name_plural = "Districts"

# class Company(models.Model):
#     state_id = models.ForeignKey(State, on_delete=models.CASCADE)
#     district = models.TextField(blank=True, null=True)
#     name = models.CharField(max_length=50)
#     logo_url = models.ImageField(upload_to = "CompaniesLogos/%Y/%m/%d", null=True, blank=True)
#     status = models.BooleanField(null=True,blank=True,default=False)
#     added_on = models.DateTimeField(auto_now=True)
#     def __str__(self):
#         return self.name
#     class Meta:
#         verbose_name_plural = "Companies"

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

# class MagazineCategory(models.Model):
#     name = models.CharField(max_length=50)
#     image_url = models.ImageField(upload_to = "MagazineCategoryImages/%Y/%m/%d", null=True, blank=True)
#     status = models.BooleanField(default=False)
#     added_on = models.DateTimeField(auto_now=True)
#     def __str__(self):
#         return self.name
#     class Meta:
#         verbose_name_plural = 'MagazineCategories'

# class Magazine(models.Model):
#     name = models.CharField(max_length=50)
#     file_url = models.FileField(upload_to='MagazinePDFs/%Y/%m/%d')
#     magazine_category_id = models.ForeignKey(MagazineCategory, on_delete=models.CASCADE, blank=True, null=True)
#     news_date = models.DateField()
#     status = models.BooleanField(default=False)
#     added_on = models.DateTimeField(auto_now=True)
#     def __str__(self):
#         return self.name
#     class Meta:
#         verbose_name_plural = 'Magazines'


