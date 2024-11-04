from rest_framework import mixins, generics, permissions

from .models import Cars
from .serializers import CarsSerializer

class CarsListAPIView(generics.ListAPIView):
    serializer_class = CarsSerializer
    permission_classes = [permissions.Allowany]
    queryset = Customer.objects.all()