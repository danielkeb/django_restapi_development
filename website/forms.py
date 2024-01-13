from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Record

class CreateUser(UserCreationForm):
    email= forms.EmailField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name=forms.CharField(label='',max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'first name'}))
    last_name=forms.CharField(label='',max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'last name'}))




    class Meta:
        model=User
        fields=('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
    def __init__(self, *args, **kwargs):
        super(CreateUser, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['username'].widget.attrs['placeholder']='user name'
        self.fields['username'].label=''

        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['placeholder']='password'
        self.fields['password1'].label=''
        self.fields['password1'].help_text='<ul class="form-text-muted"><li>characters ,10 digits and @/./+/- only .</li><li>password at least 8 characters </li><li>not used commenly used password</li></ul>'

        self.fields['password2'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['placeholder']='confirm password'
        self.fields['password2'].label=''
        self.fields['password2'].help_text='<span class="form-text-muted">must matched with above password</span>'


class AddCustomer(forms.ModelForm):

    first_name =forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'first name'},),label="")
    last_name =forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'last name'}),label="")
    email =forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'email'}),label="")
    address =forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Adress'}),label="")
    phone =forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Phone'}),label="")
    city =forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'City'}),label="")
    state =forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'State'}),label="")
    zipcode =forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'zipcode'}),label="")


    class Meta:
        model=Record
        exclude=('User',)
