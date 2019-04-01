from django import forms


# class RegistrationIndividualAccountForm(forms.ModelForm):
# 	class Meta:
# 		model = Account
# 		fields = ('FirstName','LastName','MiddleName','email','PhoneNumber','DeliveryAddress')
	
# 	def __init__(self, *args, **kwargs):
# 		super().__init__(*args, **kwargs)
# 		self.fields['email'].label = 'Email'
# 		self.fields['email'].required=True 
# 		self.fields['FirstName'].widget.attrs.update({'class':'firstName'})
	
# 	def save(self, commit=True):
# 		print('hello')
# 		self.fields['username'] = forms.CharField()
# 		self.fields['AccountType'] = forms.CharField()

# 		self.cleaned_data['username'] =self.cleaned_data['LastName'] + ' ' + \
# 							self.cleaned_data['FirstName'] + ' ' + self.cleaned_data['MiddleName']
# 		self.cleaned_data['AccountType'] = 'individual'
# 		print(self.cleaned_data)
# 		try:
# 			super().save(commit)
# 		except Exception as e:
# 			print('wow!! we have a problem:',e) 