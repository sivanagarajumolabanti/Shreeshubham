from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Survey
from .serializers import SurveySerializer
from customers.models import Customer
from customers.serializers import CustomerSerializer


class SurveyView(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        if isinstance(data['customer'], dict):
            cus_obj = Customer.objects.filter(mobile=data['customer']['mobile'])
            if not cus_obj:
                customer = CustomerSerializer(data=data['customer'])
                if customer.is_valid():
                   data['customer'] = customer.save().id
            else:
                data['customer'] = cus_obj[0].id
        surv = SurveySerializer(data=data)
        if surv.is_valid():
            surv.save()
            return Response(surv.data, status=status.HTTP_201_CREATED)
        return Response(surv.errors, status=status.HTTP_400_BAD_REQUEST)
