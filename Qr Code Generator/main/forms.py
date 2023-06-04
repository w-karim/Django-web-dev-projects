from django import forms


class QR_generator(forms.Form):
    Text = forms.CharField(widget = forms.TextInput(attrs = {'placeholder' : 'Type here ...', 
                                                            'class':'text-input'
                                                             }))