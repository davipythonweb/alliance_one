from rest_framework import serializers

from .models import Cars

class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ('id', 'name', 'brand','release_date')
        read_only_fields = ('id',)