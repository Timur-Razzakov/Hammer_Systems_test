from accounts.models import User
from django import forms
import re

from django.core.validators import RegexValidator


def validate_phone_number(phone_number):
    # Паттерн для валидации номера телефона
    pattern = r'^\+7\d{9}$'
    if not re.match(pattern, phone_number):
        raise forms.ValidationError("Формат номера: +7XXXXXXXXXX (X - от 0 до 9)")


class UserLoginForm(forms.Form):
    phone_number = forms.CharField(
        max_length=11,
        label='Введите номер телефона ',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        ),
        validators=[validate_phone_number]  # Подключение кастомного валидатора
    )


class InviteCodeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['activate_code']
        widgets = {
            'activate_code': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'phone_number': 'Введите код активации:',
        }


class UserForm(forms.Form):
    invite_code = forms.CharField(
        max_length=6,
        min_length=6,
        label='Введите invite_code, который хотите активировать',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
