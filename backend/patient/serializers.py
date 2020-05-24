from django.contrib.auth.models import User, Group
from .models import Patient
from rest_framework import serializers

class PatientSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Patient
        fields = ['barcode', 'qr', 'name', 'age', 'birthday', 'group', 'sample_status', 
                    'doctor', 'analysis', 'attachments', 'sampling_date', 'rdv', 'image']