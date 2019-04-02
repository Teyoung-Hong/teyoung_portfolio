from django import forms
from django.core.mail import send_mail
from django.conf import settings

class ContactForm(forms.Form):
    
    name = forms.CharField(
      label='氏名',
      max_length=50,
      required=True, 
      widget=forms.TextInput(
        attrs={
          'class': 'form-control reset-border-radius',
          'placeholder': '例）胃二 絵酢太',
          'name': 'name'
          }
      )
    )

    message = forms.CharField(
      label='お問い合わせ内容', 
      max_length=5000,
      widget=forms.Textarea(
        attrs={
          'placeholder':'メールアドレスも併せてご記入お願い致します。',
          'class': 'form-control reset-border-radius',
          'name': 'message'
          }
      ), 
      required=True
    )

    email = forms.CharField(
      label="メールアドレス",
      max_length=100,
      widget=forms.TextInput(
        attrs={
          'class':"form-control reset-border-radius email",
          "placeholder":"メールアドレス", 
          "name":"email"
        }
      )
    )
    
    # メール送信処理
    def send_email(self):
        # send email using the self.cleaned_data dictionary
        subject = self.cleaned_data['name']
        message = self.cleaned_data['message']
        from_email = settings.EMAIL_HOST_USER
        to = [settings.EMAIL_HOST_USER]
