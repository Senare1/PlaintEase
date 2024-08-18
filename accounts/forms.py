from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .constants import STATUT
from .models import CommonUser
from django.contrib.auth import authenticate

class SignupForm(UserCreationForm):
    full_name = forms.CharField(
        max_length=128,
        required=True,
        widget=forms.TextInput(attrs={'id': 'id_full_name','class':'form-control'})
    )
    phone = forms.CharField(
        max_length=8,
        required=True,
        widget=forms.TextInput(attrs={'id': 'id_phone','type':'tel','name':'phone','class':'form-control'})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'id': 'id_email','name':'email','class':'w-100 form-control'})
    )
    status = forms.ChoiceField(
        choices=STATUT,
        required=True,
        help_text="Votre status",
        widget=forms.Select(attrs={'id': 'id_status','class':'form-control'})
    )
    address = forms.CharField(
        required=True,
        help_text="Votre addresse",
        widget=forms.TextInput(attrs={'id': 'id_address','class':'form-control'})
    )
    password1 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'id': 'id_password1','class':'form-control'})
    )
    password2 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'id': 'id_password2','class':'form-control'})
    )

    class Meta:
        model = CommonUser
        fields = ('full_name', 'phone','address', 'email', 'status','password1', 'password2')

class VerifyForm(forms.Form):
    code = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class' : 'form-control rounded','placeholder':'Exemple:885436','aria-label':'Exemple:885436','aria-describedby':"button-addon2"})
    )

class LoginEmailForm(forms.Form):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'id': 'id_email','type':'email','name':'email','class':'w-100 form-control'})
    )
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'id': 'id_password','class':'form-control'})
    )

class LoginPhoneForm(forms.Form):
    phone = forms.CharField(
        max_length=15,
        required=True,
        widget=forms.TextInput(attrs={'id': 'id_phone','type':'tel','name':'phone','class':'form-control'})
    )
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'id': 'id_password','class':'form-control'})
    )

class ActionForm(forms.Form):

    status = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class':"form-check-input", 'type':"checkbox" ,'role':"switch", 'id':"flexSwitchCheckDefault"
        })
    )
    reject = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class':"form-check-input", 'type':"checkbox" ,'role':"switch", 'id':"flexSwitchCheckReject"
        })
    )
    msg = forms.CharField(
        required=True,
        help_text="Votre addresse",
        widget=forms.Textarea(attrs={'id': 'id_msg','class':'form-control'})
    )

class ReceiveEmail(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'type':"email", 'class':"form-control",'name':"email" ,'id':"email", 'placeholder':"name@example.com"
            }
        )
    )

class ChangePasswordForm(forms.Form):
    password1 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'id': 'id_password1','type':"password",'name':"id_password1",'class':'w-100 form-control'})
    )
    password2 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'id': 'id_password2','type':"password",'name':"id_password2",'class':'w-100 form-control'})
    )