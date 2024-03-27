from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from blogapp.models import Profile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        
# Styling username, password1, password2
    def __init__(self, *args, **kwargs):
        super(SignUpForm,self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    last_login = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Login'}))
    is_superuser = forms.CharField(max_length=100,widget=forms.CheckboxInput(attrs={'class': 'form-check', 'placeholder': 'Is Superuser'}))
    is_staff = forms.CharField(max_length=100,widget=forms.CheckboxInput(attrs={'class': 'form-check', 'placeholder': 'Is Staff'}))
    is_active = forms.CharField(max_length=100,widget=forms.CheckboxInput(attrs={'class': 'form-check', 'placeholder': 'Is Active'}))
    date_joined = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Date Joined'}))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email','password','last_login','is_superuser','is_staff','is_active','date_joined')
        
class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type' : 'password' ,'placeholder': 'Old Password'}))
    new_password1 = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class': 'form-control','type' : 'password' ,'placeholder': 'New Password'}))
    new_password2 = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class': 'form-control', 'type' : 'password' ,'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio',  'website_url', 'linkedin_url', 'twitter_url', 'instagram_url', 'facebook_url']

        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Bio'}),
            #'profile_pic': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Profile Pic'}),
            'website_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Website URL'}),
            'linkedin_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'LinkedIn URL'}),
            'twitter_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Twitter URL'}),
            'facebook_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Facebook URL'}),
            'instagram_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Instagram URL'}),
        }