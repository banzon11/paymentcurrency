from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import PaymentSerializer, CurrencySerializer

class PaymentView(APIView):
    def get(self, request, reference_code=None, currency=None):
        payments = Payment.objects.all()
        if reference_code is not None:
            payments = payments.filter(reference_code=reference_code)
        if currency is not None:
            payments = payments.filter(currency=currency)
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)

    def post(self, request):
        # request.data["currency"]=Currency.objects.get(pk=request.data["currency"])
        # print(request.data)
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            payment = serializer.save()
        # Check if the amount exceeds the limit
            if payment.amount > 5000:
                return Response({'error': 'The amount exceeds the limit.'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk):
        payment = Payment.objects.get(pk=pk)
        if payment.is_paid:
            return Response({'error': 'The payment is already marked as paid.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            payment.is_paid = True
            payment.save()
            return Response(payment.to_json(), status=status.HTTP_200_OK)

class CurrencyView(APIView):
    def get(self, request):
        currencies = Currency.objects.all()
        serializer = CurrencySerializer(currencies, many=True)
        return Response(serializer.data)