from rest_framework import serializers
from .models import State,Company


class CompanySerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='company-detail',read_only=True)
    class Meta:
        model = Company
        fields = ['id','url', 'company_name', 'added_on']

class StateSerializer(serializers.ModelSerializer):
    company = CompanySerializer(many=True, read_only=True, source='company_set')
    url = serializers.HyperlinkedIdentityField(view_name='state-detail',read_only=True)
    class Meta:
        model = State
        fields = ['id', 'url','state_name','company', 'added_on']



