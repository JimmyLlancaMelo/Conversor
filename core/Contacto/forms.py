from django import forms

class formContacto(forms.Form):
    nombre = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    mensaje = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
