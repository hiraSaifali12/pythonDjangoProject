from django import forms
from .models import employee

class feedbackForm(forms.Form):

    email = forms.EmailField(label="Enter Your Email", max_length=100)
    name = forms.CharField(label="Enter Your Name",max_length=100)
    feedback= forms.CharField(label="Enter Your Feedback",widget=forms.Textarea)


    
    def __init__(self, *args, **kwargs):
        super(feedbackForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class employeeForm(forms.ModelForm) :
    class meta:
        model=employee
        fields=['name','employee_id','phone','address',]           