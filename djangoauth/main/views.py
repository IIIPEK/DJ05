from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ProfileForm, CustomUserCreationForm


class HomeView(TemplateView):
    template_name = 'main/home.html'


class RegisterView(CreateView):
    template_name = 'main/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, 'Registration successful. You can now log in.')
        return super().form_valid(form)


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'main/profile.html'

@login_required
def profile_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Редирект на текущую страницу профиля
    else:
        form = ProfileForm(instance=request.user)

    return render(request, 'main/profile.html', {'form': form})