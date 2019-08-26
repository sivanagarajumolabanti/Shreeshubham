from .models import Survey
from rest_framework import serializers


class SurveySerializer(serializers.ModelSerializer):

    class Meta:
        model = Survey
        fields = ('customer',
                  'products',
                  'purchased',
                  'rating',
                  'feedback')
