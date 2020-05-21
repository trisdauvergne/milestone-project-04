from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .models import Order


class StripeWH_Handler:
    """ Handle Stripe webhooks """

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """ Send the customer a confirmation email """
        customer_email = order.email
        subject = render_to_string(
            'checkout/customer_confirmation_emails/\
            confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/customer_confirmation_emails/\
            confirmation_email_body.txt',
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
        pid = intent.id

        billing_details = intent.charges.data[0].billing_details

        shipping_details = intent.shipping

        grand_total = round(intent.charges.data[0].amount / 100, 2)

        order = Order.objects.get(
            full_name__iexact=shipping_details.name,
            email__iexact=billing_details.email,
            phone_number__iexact=shipping_details.phone,
            street_address_1__iexact=shipping_details.address.line1,
            street_address_2__iexact=shipping_details.address.line2,
            country__iexact=shipping_details.address.country,
            grand_total=grand_total,
            stripe_pid=pid,
            )
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
