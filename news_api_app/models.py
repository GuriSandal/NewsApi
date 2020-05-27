from django.db import models

# Create your models here.

class State(models.Model):
    state_name = models.CharField(max_length=50)
    added_on = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.state_name
    class Meta:
        verbose_name_plural = "States"

class Company(models.Model):
    state_id = models.ForeignKey(State, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=50)
    added_on = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.company_name
    class Meta:
        verbose_name_plural = "Companies"

# class Company(models.Model):
#     state_id = models.ForeignKey(State, on_delete=models.CASCADE)
#     company_name = models.CharField(max_length=50)
#     added_on = models.DateTimeField(auto_now=True)
#     def __str__(self):
#         return self.company_name
#     class Meta:
#         verbose_name_plural = "Companies"


    