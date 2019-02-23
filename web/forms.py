from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


class RegisterForm(forms.Form):
    #username
    username = forms.CharField()
    #FirstName
    fname  = forms.CharField()
    #LastName
    lname = forms.CharField()
    #Email
    email = forms.CharField()
    #Password1
    pwfield1 = forms.CharField()
    #Password2
    pwfield2 = forms.CharField()

    # Uni-form
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('username', css_class='input-xlarge'),
        Field('fname', css_class='input-xlarge'),
        Field('lname', css_class='input-xlarge'),
        Field('email', css_class='input-xlarge'),
        Field('pwfield1', css_class='input-xlarge'),
        Field('pwfield2', css_class='input-xlarge'),
        FormActions(
            Submit('complete_registration', 'Create Account', css_class="btn-primary"),)
        )
