from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import User
from django import forms
from django.core.mail import send_mail
from django.conf import settings


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    def save(self, commit=True):
        """Смена у пользователя флага на неактивный и отправка на почту пользователя
        письма в виде ссылки на активацию"""

        user = super().save()
        send_mail(subject='Активация',
                  message=f'Для активации профиля пройдите по ссылке - http://127.0.0.1:8000/usersactivate/{user.id}/',
                  from_email=settings.EMAIL_HOST_USER,
                  recipient_list=[user.email])
        user.is_active = False
        user.save()
        return user


class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'avatar', 'country')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()
