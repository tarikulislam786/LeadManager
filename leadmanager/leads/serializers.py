from rest_framework import serializers
from leads.models import Lead

# Lead Serializer     -- turning the Lead model into Model serializer

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Lead
        fields = '__all__'
