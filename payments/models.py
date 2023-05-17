from django.db import models

class Payment(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    reference_code = models.CharField(max_length=100, unique=True)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    currency = models.ForeignKey('Currency', on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    paid_date = models.DateField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

class Currency(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)