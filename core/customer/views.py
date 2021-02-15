from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from core.customer import forms


# Create your views here.


@login_required()
def home(request):
    return rediret(reverse('customer:profile'))

@login_required(login_url="/sign-in/?next=/customer/")
def profile_page(request):
    user_form = forms.BasicUserForm()

    return render(request, 'customer/profile.html', {
        "user_form": user_form
    })
