from django import forms
from django.core import validators

# building validator to check that name starts with z
# def check_for_z(value):
#     if value[0].lower()!='z':
#         raise forms.ValidationError("name need to start with z")


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='enter your email again')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher=forms.CharField(required=False,
                                widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])
    def clean(self):
        all_clean_data=super().clean()
        email=all_clean_data['email']
        vmail=all_clean_data['verify_email']
        if email != vmail:
            raise forms.ValidationError("enter the same email at verification!!")

# the long method below
    # def clean_botcatcher(self):
    #     botcatcher=self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0: #this field was hidden so if someone is not bot it would not fill anything inside it
    #         raise forms.ValidationError("GOTCHA BOT")
    #     return botcatcher
