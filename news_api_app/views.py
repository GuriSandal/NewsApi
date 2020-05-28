
from news_api_app.models import State, Headline
from news_api_app.serializers import StateSerializer, HeadlineSerializer
from rest_framework.decorators  import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def state_list(request):
    response_data = {}
    response_data["headlineText"] = Headline.objects.get(headlineId=2).headlineText
    response_data["stateList"] = StateSerializer(State.objects.all(), many=True).data

    return Response(response_data, status=status.HTTP_200_OK)