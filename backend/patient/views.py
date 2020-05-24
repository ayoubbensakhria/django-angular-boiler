from django.shortcuts import render
from django.contrib.auth.models import User, Group
from .models import Patient
from .serializers import PatientSerializer
from rest_framework import permissions, generics, viewsets, filters
from django_filters.rest_framework.backends import DjangoFilterBackend


# Create your views here.
class PatientViewSet(viewsets.ModelViewSet):
    """ 
    API endpoint that allows Patients to be viewed or edited.
    """
    queryset = Patient.objects.all().order_by('-sampling_date')
    serializer_class = PatientSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'qr', 'barcode', 'sampling_date']

    #permission_classes = [permissions.IsAuthenticated]