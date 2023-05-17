from rest_framework import serializers
from .models import *
class PaymentSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Payment
        fields = ('id', 'user','reference_code', 'amount', 'currency', 'is_paid', 'paid_date', 'created_date')

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ('id', 'name', 'code', 'created_date')