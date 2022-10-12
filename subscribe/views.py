
from django.shortcuts import render, redirect
from django.urls import reverse

from subscribe.forms import Subscribe_Form
from subscribe.models import Subscribe

# Create your views here.

def subscribe(request):
    # email_is_empty_error = False
    subscribe_form = Subscribe_Form()
    if request.POST:
        subscribe_form = Subscribe_Form(request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save()
            # print(subscribe_form.cleaned_data)
            # first_name = subscribe_form.cleaned_data["first_name"]
            # last_name  = subscribe_form.cleaned_data["last_name"]
            # email     = subscribe_form.cleaned_data["email"]
            # print(first_name)
            # subscriber = Subscribe(first_name=first_name, last_name=last_name, email=email)
            # subscriber.save()

            return redirect(reverse('thank_you'))
    context = {'form': subscribe_form, }

    return render(request, 'subscribe/subscribe.html', context)


def thank_you(request):
    context = {}
    return render(request, 'subscribe/thank_you.html', context)