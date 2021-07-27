from django import forms
class VCquery(forms.Form):
    date=forms.DateField()
    pincode=forms.IntegerField()
    fields=('date', 'pincode')