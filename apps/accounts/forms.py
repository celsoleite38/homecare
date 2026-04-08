from django import forms
from django.core.exceptions import ValidationError
from .models import HomeCare


class HomeCareForm(forms.ModelForm):
    class Meta:
        model = HomeCare
        fields = [
            'nome',
            'cnpj',
            'endereco',
            'telefone_fixo',
            'telefone_celular',
            'whatsapp_celular',
            'logo',
            'descricao',
        ]
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4}),
        }


class HomeCareSignupForm(forms.Form):
    nome = forms.CharField(label='Nome do HomeCare', max_length=200)
    cnpj = forms.CharField(label='CNPJ', max_length=20, required=False)
    endereco = forms.CharField(label='Endereço do HomeCare', widget=forms.Textarea, required=False)
    telefone_fixo = forms.CharField(label='Telefone fixo', max_length=20, required=False)
    telefone_celular = forms.CharField(label='Telefone celular', max_length=20, required=False)
    whatsapp_celular = forms.BooleanField(label='WhatsApp no celular', required=False)
    logo = forms.ImageField(label='Logo do HomeCare', required=False)
    descricao = forms.CharField(label='Descrição do HomeCare', widget=forms.Textarea(attrs={'rows': 4}), required=False)

    username = forms.CharField(label='Usuário', max_length=150)
    email = forms.EmailField(label='E-mail')
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirme a senha', widget=forms.PasswordInput)
    first_name = forms.CharField(label='Nome', max_length=150, required=False)
    last_name = forms.CharField(label='Sobrenome', max_length=150, required=False)
    telefone = forms.CharField(label='Telefone do proprietário', max_length=20, required=False)
    cpf = forms.CharField(label='CPF do proprietário', max_length=14, required=False)
    endereco_usuario = forms.CharField(label='Endereço do proprietário', widget=forms.Textarea, required=False)

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError('As senhas não coincidem.')
        return cleaned_data
