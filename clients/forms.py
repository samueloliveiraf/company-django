
from django import forms
from .models import Client


class CustumerForm(forms.ModelForm):
    name = forms.CharField(label='Nome')
    email = forms.EmailField(label='E-mail')
    area_code = forms.RegexField(
        label='*DDD',
        regex = r'^\+?1?[0-9]{2}$',
        error_messages= {'invalid': 'Número de DDD inválido'}
    )
    phone_number = forms.RegexField(
        label='*Telefone',
        regex = r'^\+?1?[0-9]{9,15}$',
        error_messages= {'invalid': 'Número do Telefone é inválido'}
    )
    city = forms.CharField(label='Cidade')
    road = forms.CharField(label='Rua')
    district = forms.CharField(label='Bairro')
  

    class Meta:
        model = Client
        fields = (
            'name', 
            'email', 
            'area_code', 
            'phone_number', 
            'city',
            'road',
            'district'
        )

