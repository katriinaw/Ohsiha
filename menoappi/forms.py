from django import forms

class HakuForm(forms.Form):
    hakusana = forms.CharField(max_length=100)
    class meta:
        fields = ("hakusana")
