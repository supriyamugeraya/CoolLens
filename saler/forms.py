from .models import SalerDetail, Product
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

class SalerRegisterForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'oninput': 'validateNames()'}),
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z]+$',
                message='First name must contain only alphabets.',
                code='invalid_first_name'
            )
        ]
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'oninput': 'validateNames()'}),
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z]+$',
                message='Last name must contain only alphabets.',
                code='invalid_last_name'
            )
        ]
    )
    username = forms.CharField(label=("Mobile Number/Email"), widget=forms.TextInput(attrs={'oninput': 'validate()'}))
    gst = forms.CharField(label=("GST Number"), widget=forms.TextInput(attrs={}), validators=[RegexValidator(regex=r'^\d{2}[A-Z]{5}\d{4}[A-Z]{1}\d[Z]{1}[A-Z\d]{1}$', message='Invalid GST number.')])
    shop = forms.CharField(label=("Company/Shop Name"), widget=forms.TextInput(attrs={}))
    password1 = forms.CharField(label=("Password"), strip=False, widget=forms.PasswordInput(attrs={}))
    password2 = forms.CharField(label=("Confirm"), strip=False, widget=forms.PasswordInput(attrs={}))
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2', 'gst', 'shop']
class SalerAddressForm(forms.ModelForm):
	shop_Address = forms.CharField(widget=forms.TextInput(attrs={}))
	locality = forms.CharField(required =True)
	city = forms.CharField(required =True)
	alternate_mobile = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Alternate Mobile No(optional)'}), required = False)
	landmark = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Landmark(optional)'}), required = False)
	class Meta:
		model = SalerDetail
		fields = [
			'mobile',
			'shop_Name',
			'alternate_mobile',
			'shop_Address',
			'pincode',
			'landmark',
			'locality',
			'city',
			'state',
		]
class UpdateSalerDetailForm(forms.ModelForm):
	class Meta:
		model = SalerDetail
		fields = [
			'photo',
			'mobile',
			'shop_Name',
			'gst_Number',
			'alternate_mobile',
			'shop_Address',
			'pincode',
			'landmark',
			'locality',
			'city',
			'state',
		]

class UpdateSalerAccountDetailForm(forms.ModelForm):
	class Meta:
		model = SalerDetail
		fields = [
			'account_Holder_Name',
			'account_Number',
			'ifsc_Code',
			]


