from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegistrationForm


class RegistrationView(CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/registration.html'
