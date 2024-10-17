from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Location, Station, Car
from .serializers import LocationSerializer, StationListSerializer, StationSerializer, CarSerializer, CarUpdateSerializer

# Create your views here.
@api_view(['POST'])
def location_create(request):
    if request.method == 'POST':
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def station_list(request):
    if request.method == 'GET':
        stations = get_list_or_404(Station)
        serializer = StationListSerializer(stations, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def station_create(request, location_pk):
    location = get_object_or_404(Location, pk=location_pk)
    if request.method == 'POST':
        serializer = StationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(address=location)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE'])
def station_detail(request, station_pk):
    station = get_object_or_404(Station, pk=station_pk)
    if request.method == 'GET':
        serializer = StationSerializer(station)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        station.delete()
        data = {
            'delete': f'{station.address}의 등록 번호 {station.pk}번 충전소 정보를 삭제하였습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
    
@api_view(['POST'])
def car_create(request, station_pk):
    station = get_object_or_404(Station, pk=station_pk)
    if request.method == 'POST':
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(station=station)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT'])
def car_detail(request, car_pk):
    car = get_object_or_404(Car, pk=car_pk)
    if request.method == 'GET':
        serializer = CarSerializer(car)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = CarUpdateSerializer(car, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            serializer = CarSerializer(car) 
            return Response(serializer.data)
