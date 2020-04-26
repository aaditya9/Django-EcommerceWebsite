from django import forms
from django.contrib.auth import  get_user_model

User = get_user_model()

class ContactForm(forms.Form):
	fullname = forms.CharField(
		widget=forms.TextInput(
				attrs={'class':'form-control',
				'id':'form_full_name',
				'placeholder':'Name'}),
		label='Name')

	email = forms.EmailField(
		widget=forms.EmailInput(
			attrs={
				'class':'form-control',
				'id':'form_full_name',
				'placeholder':'Your email'
				}
			),
		label='Email')

	content =forms.CharField(
		widget=forms.Textarea(
			attrs={
				'class':'form-control',
				'id':'form_content',
				'placeholder':'Content'
				}
			)
	)
	def clean_email(self):
		email=self.cleaned_data.get("email")
		if not "gmail.com" in email:
			raise forms.ValidationError("Email has to be gmail.com")
		return email


class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField()


class RegisterForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(
				attrs={'class':'form-control',
				'placeholder':'Name'}),)
	email 	 = forms.EmailField(widget=forms.TextInput(
				attrs={'class':'form-control',
				'placeholder':'Email'}))
	password = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	password2 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

	def clean_username(self):
		username = self.cleaned_data.get("username")
		qs =User.objects.filter(username=username)
		if(qs.exists()):
			raise forms.ValidationError("User name is taken")
		return username

	def clean_email(self):
		email = self.cleaned_data.get("email")
		qs =User.objects.filter(email=email)
		if(qs.exists()):
			raise forms.ValidationError("Email name is taken")
		return email
