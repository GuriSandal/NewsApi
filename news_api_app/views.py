from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from news_api_app.models import State, Company
from news_api_app.serializers import StateSerializer, CompanySerializer
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework import viewsets

# @csrf_exempt
# def state_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         states = State.objects.all()
#         serializer = StateSerializer(states, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = StateSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def state_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         state = State.objects.get(pk=pk)
#     except State.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = StateSerializer(state)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = StateSerializer(state, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         state.delete()
#         return HttpResponse(status=204)


class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer


# class StateDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = State.objects.all()
#     serializer_class = StateSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

# class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer

# class ApiRoot(APIView):
#     def get(self, request, format=None):
#         return Response({
#         'states': reverse('all_states', request=request, format=format),
#         'companies': reverse('all_companies', request=request, format=format)
#     })