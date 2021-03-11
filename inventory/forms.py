from django import forms
from .models import Management, Question, Takeout

class ReagentForm(forms.ModelForm):
    class Meta:
        model = Management
        fields = '__all__'

class ConsumableForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'        

class ControlForm(forms.ModelForm):
    class Meta:
        model = Takeout
        fields = '__all__'            