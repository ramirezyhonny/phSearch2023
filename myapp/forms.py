from django import forms
from django.contrib.auth.forms import UserCreationForm
from user.models import User
#extender formulario de django que solo cubria el username y el password.
class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required. Enter your first name.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required. Enter your last name.')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')
    country= forms.CharField(max_length=100, required=True, help_text='Required. Enter your country.')
    provinces=forms.CharField(max_length=100, required=True, help_text='Required. Enter your country')
    usertype=forms.ChoiceField(
        choices=(('client','Client'), ('photographer','Photographer')),
        widget=forms.RadioSelect
    )
    picture = forms.ImageField(required=False)
    class Meta:
        model = User
        fields=('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'country', 'provinces','usertype','picture')
        
class editProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'country', 'provinces', 'picture')

    def __init__(self, *args, **kwargs):
        super(editProfile, self).__init__(*args, **kwargs)
        self.fields['picture'].required = False  # Para permitir la omisión del campo de imagen
