from django import forms
from django.core.exceptions import ValidationError
from rover.models import Environment, RoverDesc,RoverMovement
from django.contrib.auth.models import User


class EnvironmentConfigForm(forms.ModelForm):
    class Meta:
        model = Environment
        fields = ['temperature','humidity', 'solar_flare','storm','terrain' ]
    #     labels = {
    #         'myTopic': 'Choose your topic',
    #         'post_title': 'Your Post title',
    #         'myPost': 'Post here',
    #     }
    #     widgets = {
    #         'myTopic':forms.Select(attrs={'class': 'form-control'}),
    #         #'myTopic': forms.TextInput(attrs={'class': 'form-control'}),
    #         'post_title': forms.TextInput(attrs={'class': 'form-control'}),
    #         'myPost': forms.Textarea(attrs={'cols': 85, 'rows': 10}),
    #     }
    # def as_myp(self):
    #     "Returns this form rendered as HTML <p>s."
    #     return self._html_output(
    #         normal_row='<p%(html_class_attr)s>%(label)s</p> <p>%(field)s%(help_text)s</p>',
    #         error_row='%s',
    #         row_ender='</p>',
    #         help_text_html=' <span class="helptext">%s</span>',
    #         errors_on_separate_row=True)
class RoverDescForm(forms.ModelForm):
    class Meta:
        model = RoverDesc
        fields = '__all__'

class RoverMovementForm(forms.ModelForm):
    class Meta:
        model = RoverMovement
        fields = '__all__'