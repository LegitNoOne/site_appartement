from django import forms
class Formulaire_Reservation(forms.Form):
	nom = forms.CharField(max_length=30)
	prenom = forms.CharField(max_length=30)
	email = forms.EmailField(label="e-mail")
	nettoyage = forms.BooleanField(help_text="", required=False)
