from rest_framework import serializers
from .models import State,Company


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['id', 'state_name', 'added_on']


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id','state_id', 'company_name', 'added_on']
