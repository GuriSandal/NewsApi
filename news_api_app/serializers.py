from rest_framework import serializers
from .models import State,Headline

class HeadlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Headline
        fields = ['headlineText']


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['stateId','stateName', 'imageUlr']


