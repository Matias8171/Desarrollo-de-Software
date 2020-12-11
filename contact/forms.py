from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre",min_length=3, max_length=80,required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingresar Nombre'}))
    email = forms.EmailField(label="Email",min_length=5, max_length=100, required=True, widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Ingresar Correo Electrónico'}))
    message = forms.CharField(label="Mensaje",min_length=5, max_length=400, required=True, widget=forms.Textarea(attrs={'class':'form-control','placeholder':'introduzca su Mensaje','rows':10}))
    