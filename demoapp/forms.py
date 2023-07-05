from django import forms
from .models import MyModel2,MyModel3

class MyForm(forms.ModelForm):
  class Meta:
    model = MyModel2
    fields = ["fullname", "mobile_number",]
    labels = {'fullname': "Name", "mobile_number": "Mobile Number",}

class MyForm1(forms.ModelForm):
  class Meta:
    model = MyModel3
    fields = ["phone_number", "message","type_your_message",]
    labels = {'phone_number': "Phone", "message": "Message","type_your_message":"Enter your text",}
