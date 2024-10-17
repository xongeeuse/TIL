from rest_framework import serializers
from .models import Location, Station, Car


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = '__all__'

class StationSerializer(serializers.ModelSerializer):
    class LocationAddressSerializer(serializers.ModelSerializer):

        class Meta:
            model = Location
            fields = ('address', )
            
    address = LocationAddressSerializer(read_only=True)
    class Meta:
        model = Station
        fields = '__all__'

class StationListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Station
        fields = ('address', 'is_opening',)
        

class CarSerializer(serializers.ModelSerializer):
            
    class Meta:
        model = Car
        fields = '__all__'
        read_only_fields = ('station', )

class CarUpdateSerializer(serializers.ModelSerializer):
            
    class Meta:
        model = Car
        fields = ('is_payment', )
        read_only_fields = ('station', 'start_time', 'model')

        