from django.test import TestCase
from django.http import HttpRequest
from .views import PaymentView
from .models import *
class PaymentViewTestCase(TestCase):
    def test_post_with_valid_data(self):
        # Create a valid payment request
        request = HttpRequest()
        request.method = 'POST'
        request.POST = {
    'reference_code': '123456',
    'amount': 100.00,
    'currency': 'USD',
}
        # Call the post() method
        response = PaymentView.as_view()(request)

        # Check that the response is a 201 Created response
        self.assertEqual(response.status_code, 201)

        # Check that the payment was created correctly
        payment = Payment.objects.get(reference_code='123456')
        self.assertEqual(payment.amount, 1000)
        self.assertEqual(payment.currency, 'USD')

#     def test_post_with_invalid_data(self):
#         # Create an invalid payment request
#         request = HttpRequest()
#         request.method = 'POST'
#         request.POST = {
#     'reference_code': '123456',
#     'amount': 100.00,
#     'currency': 'USD',
# }

#         # Call the post() method
#         response = PaymentView.as_view()(request)

#         # Check that the response is a 400 Bad Request response
#         self.assertEqual(response.status_code, 400)

#         # Check that the error message is correct
#         self.assertEqual(response.data['error'], 'The amount exceeds the limit.')