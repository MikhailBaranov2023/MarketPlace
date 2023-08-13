from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from users.models import User
from users.forms import UserRegisterForm, UserProfileForm
from django.urls import reverse_lazy, reverse
from django.core.mail import send_mail
import random
from django.conf import settings
from django.contrib.auth import get_user_model


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        send_mail(subject='Активация',
                  message=f'Для активации профиля пройдите по ссылке - http://127.0.0.1:8000/users/activate/{user.id}/',
                  from_email=settings.EMAIL_HOST_USER,
                  recipient_list=[user.email])
        return super().form_valid(form)


def activate_new_user(request, pk):
    user = get_user_model()
    user_for_activate = user.objects.get(id=pk)
    user_for_activate.is_active = True
    user_for_activate.save()
    return render(request, 'users/email_verification.html')


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def generate_new_password(request):
    new_password = ''.join([str(random.randint(0, 9)) for _ in range(6)])
    send_mail(
        subject='Вы сменили пароль',
        message=f'Ваш новый пароль - {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('users:login'))
