from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Detailsserializers
from .models import Details
# Create your views here.
class detailsviewset(viewsets.ModelViewSet):
    queryset = Details.objects.all()
    serializer_class = Detailsserializers
