from django import forms

class HakuForm(forms.Form):
    print("kutsuttu")
    tapahtuma = forms.CharField(max_length=100)
    class meta:
        fields = ("tapahtuma")
