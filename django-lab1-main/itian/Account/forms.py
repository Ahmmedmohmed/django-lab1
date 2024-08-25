from django import forms

class BaseAccountForm(forms.Form):
    username = forms.CharField(
        required=True,
        max_length=100,
        label="Name",
        widget=forms.TextInput(
            attrs={"placeholder": "Enter your username", "class": "form-control"}
        ),
    )
    email = forms.EmailField(
        required=True,
        label="Email",
        widget=forms.EmailInput(
            attrs={"placeholder": "Enter your email", "class": "form-control"}
        ),
    )
    image = forms.ImageField(
        required=False,
        label="Image",
        widget=forms.FileInput(
            attrs={"class": "form-control-file", "accept": "image/*"}
        ),
    )

class CreateAccount(BaseAccountForm):
    password = forms.CharField(
        required=True,
        max_length=200,
        label="Password",
        widget=forms.PasswordInput(
            attrs={"placeholder": "Enter your password", "class": "form-control"}
        ),
    )

class UpdateAccount(BaseAccountForm):
    password = forms.CharField(
        required=False,
        max_length=200,
        label="Password",
        widget=forms.PasswordInput(
            attrs={"placeholder": "Enter your password", "class": "form-control"}
        ),
    )
