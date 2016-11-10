from django import forms
from django.contrib.auth.models import User



class UserRegistrationForm(forms.ModelForm):
	password = forms.CharField(
		label="Password",
		widget=forms.PasswordInput)
	password2 = forms.CharField(
		label="Repite tu password",
		widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = ['username','first_name','email']

	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password'] != cd['password2']:
			forms.ValidationError('Tu password no coincide')
		return cd['password2']
