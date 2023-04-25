from django import forms
from .models import UserProfile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):

    password = forms.CharField(required=False, widget=forms.PasswordInput(), label='Senha')
    password_confirm = forms.CharField(required=False, widget=forms.PasswordInput(), label='Cofirmar Senha')


    def __init__(self, user=None, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.user = user


    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password', 'password_confirm',    'email')

    def clean(self, *args, **kwargs):
        # data = self.data
        cleaned_data = self.cleaned_data
        validation_error_messages = {}

        user = User.objects.filter(username=cleaned_data.get('username')).first()
      

        if user.username == cleaned_data.get('username'):
            validation_error_messages['username'] = 'Esse usuaŕio já existe'
        
        if user.email == cleaned_data.get('email'):
            validation_error_messages['email'] = 'Esse email já existe'

        if len(cleaned_data.get('password')) <8:
            validation_error_messages['password'] = 'A senha deve ter mais que 8 caracteres'

        if len(cleaned_data.get('password_confirm')) <8:
            validation_error_messages['password_confirm'] = 'A senha deve ter mais que 8 caracteres'    

        else:
            pass

        if validation_error_messages:
            raise forms.ValidationError(validation_error_messages)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']


