from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404
from .serializers import LocationSerializer, StationSerializer, StationListSerializer
from .models import Location, Station, Car

# Create your views here.
@api_view(['GET', 'POST'])
def location_create(request):
    if request.method == 'GET':
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# station 전체목록 조회
@api_view(['GET'])
def station_list(request):
    if request.method == 'GET':
        stations = Station.objects.all()
        serializer = StationListSerializer(stations, many=True)
        return Response(serializer.data)

# 각 지역의 station 정보 조회 or 생성
@api_view(['GET', 'POST'])
def station_create(request, location_pk):
    location = Location.objects.get(pk=location_pk)
    if request.method == 'GET':
        stations = Station.objects.filter(pk=location_pk)
        serializer = StationListSerializer(stations, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(address=location)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def station_detail(request, station_pk):
    if request.method == 'GET':
        station = get_object_or_404(Station, pk=station_pk)
        serializer = StationSerializer(station)
        return Response(serializer.data)