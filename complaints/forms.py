from django import forms
from .models import Complaint,Proof
from django.utils import timezone
from datetime import date
from django.core.exceptions import ValidationError

class ComplaintForm(forms.ModelForm):
    motif = forms.CharField(
        widget=forms.TextInput(
            attrs={'placehoder' : 'Motif plainte' ,'class':'form-control','id': 'id_motif'}
        )
    )
    incident_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'id': 'id_incident_date',
                'type': 'date',
                'max':timezone.now().date(),
            },
            format='%Y-%m-%d'
        ),
    )

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={'placehoder' : 'Motif plainte' ,'class':'form-control','rows':2,'id': 'id_description'}
        )
    )

    def clean_incident_date(self):
        incident_date = self.cleaned_data.get('incident_date')
        if incident_date > date.today():
            raise ValidationError("Date non future non autorise")
        return incident_date

    class Meta:
        model = Complaint
        fields = ['motif', 'incident_date', 'description']

class ProofForm(forms.ModelForm):
    image = forms.FileField(
        required=False,
        widget=forms.ClearableFileInput(
            attrs={'placehoder' : 'image plainte' ,'class':'form-control','id': 'id_image'}
        )
    )
    audio = forms.FileField(
        required=False,
        widget=forms.ClearableFileInput(
            attrs={'placehoder' : 'audio plainte' ,'class':'form-control','id': 'id_audio'}
        )
    )
    video = forms.FileField(
        required=False,
        widget=forms.ClearableFileInput(
            attrs={'placehoder' : 'video plainte' ,'class':'form-control','id': 'id_video'}
        )
    )
    document = forms.FileField(
        required=False,
        widget=forms.ClearableFileInput(
            attrs={'placehoder' : 'document plainte' ,'class':'form-control','id': 'id_file'}
        )
    )
    class Meta:
        model = Proof
        fields = ['image', 'video', 'audio', 'document']




