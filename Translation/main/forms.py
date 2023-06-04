from django import forms

lang_list = [
    ('','Select target language'),
    ('fr','French'),
    ('ar','Arabic'),
    ('de','Deutch'),
    ('es','Spanish'),
    ('it','Italian'),
    ('ru','Russian'),
    ('ja','Japanese')
]

class text(forms.Form):
    Text = forms.CharField(widget = forms.Textarea(attrs = {'placeholder' : 'Enter your text here ...', 
                                                            'class':'text-input'
                                                             }))
    Languages = forms.ChoiceField(choices = lang_list,
                                  widget = forms.Select(attrs={"class": "lang-input"}))

    