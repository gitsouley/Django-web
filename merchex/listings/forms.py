from django import forms
from listings.models import Band, Listing

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=False)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = '__all__'
        # exclude = ['active'] : pour exclure un champ de notre formulaire, on peut aussi faire ça à la place de fields = '__all__'

