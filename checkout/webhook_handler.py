from django.http import HttpResponse
from django.core.mail import send_mail 
from django.template.loader import render_to_string
from django.conf import settings


class StripeWH_Handler:
    """ Handle Stripe webhooks """

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self):
        """ Send the customer a confirmation email """
        customer_email = order.email
        subject = render_to_string(
            'checkout/customer_confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/customer_confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [customer_email]
        )

    def handle_event(self, event):
        """ Generic/unknown/unexpected WH """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """ Every time a payment_intent.succeeded webhook """
        intent = event.data.object
        self._send_confirmation_email(order)
        print(intent)

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """ Every time a payment_intent.payment_failed webhook """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
