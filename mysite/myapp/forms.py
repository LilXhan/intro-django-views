from django import forms 

class PersonForm(forms.Form):

    choices = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('0', 'Otros')
    )

    name = forms.CharField(max_length=200, label='Nombre')
    address = forms.CharField(max_length=200, label='Address')
    address_two = forms.CharField(max_length=200, label='Second Address')
    reference = forms.CharField(max_length=200, label='Reference')
    salary = forms.FloatField(label='Salary')
    email = forms.EmailField(label='Email')
    password = forms.PasswordInput()
    phone_number = forms.CharField(max_length=200, label='Phone Number')
    username = forms.CharField(max_length=200, label='Username')
    gender = forms.ChoiceField(choices=choices)
