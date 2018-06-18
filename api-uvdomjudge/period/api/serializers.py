from rest_framework import serializers
from ..models import AcademicPeriod


class AcademicPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicPeriod
        fields = '__all__'
