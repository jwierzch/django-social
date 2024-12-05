from django import forms
from .models import Dweet, Profile, gimage

class DweetForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Dweet something...",
                "class": "textarea is-success is-medium",
            }
        ),
        label="",
    )

    class Meta:
        model = Dweet
        fiels = ("body", )
        exclude = ("user", )

class ProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    
    class Meta:
        model = Profile
        fields = ['avatar']

class gimageForm(forms.ModelForm):
    gimage = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    class Meta:
        model = gimage
        fields = ('gimage', )
        exclude = ('user', )