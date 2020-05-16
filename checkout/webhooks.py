

def webhook(request):
    """ Listen for WB from Stripe """
    # Setup
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # gET THE WEBHOOK DATA AND VERIFY ITS SIGNATURE
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)
    except Exception as e:
        return HttpResponse(content=e, status=400)

    # # Handle the event
    # if event.type == 'payment_intent.succeeded':
    #     payment_intent = event.data.object  # contains a stripe.PaymentIntent
    #     print('PaymentIntent was successful!')
    # elif event.type == 'payment_method.attached':
    #     payment_method = event.data.object  # contains a stripe.PaymentMethod
    #     print('PaymentMethod was attached to a Customer!')
    # # ... handle other event types
    # else:
    #     # Unexpected event type
    #     return HttpResponse(status=400)

    # return HttpResponse(status=200)