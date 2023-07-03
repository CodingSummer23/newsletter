from django.shortcuts import render
from .forms import SubscriptionForm
from .models import Subscription
from django.utils.crypto import get_random_string


def home(request): 
    form = SubscriptionForm()
    return render(request, "home.html", {"form": form})


def subscribe(request):
    form = SubscriptionForm()
    error = ''
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            subscription = Subscription.objects.filter(email=form.cleaned_data['email'])
            if not subscription:
                subscription = Subscription()
                subscription.email = form.cleaned_data['email']
                subscription.unsubscribe_hash = get_random_string(length=250)
                subscription.save()

                return render(request, "success.html")
            else:
                error = 'Email already used'
        else:
            error = 'Invalid data'
        
    return render(request, "home.html", {"form": form, "error": error})


def unsubscribe(request, hash):
    subscription = Subscription.objects.filter(unsubscribe_hash=hash).first()
    if subscription:
        subscription.delete()
        return render(request, "unsubscribed.html", {"error": ''})
    else:
        return render(request, "unsubscribed.html", {"error": "Subscription not found"})

