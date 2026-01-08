from rest_framework import serializers
from .models import KYC

class KYCSerializer(serializers.ModelSerializer):
    class Meta:
        model = KYC
        fields = [

            'aadhaar_number',
            'pan_number',
            'date_of_birth',
            'address',
            'status',
            'rejection_reason'
        ]
        read_only_fields = ['status', 'rejection_reason']
        
