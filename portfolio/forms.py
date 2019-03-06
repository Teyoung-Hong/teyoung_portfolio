from django import forms
from django.core.mail import send_mail
from django.conf import settings

class ContactForm(forms.Form):
    
    name = forms.CharField(label='お名前', required=True, widget=forms.TextInput(attrs={'class': 'form-control reset-border-radius',}))
    email = forms.EmailField(label='メールアドレス', required=True, widget=forms.TextInput(attrs={'class': 'form-control reset-border-radius',}))
    message = forms.CharField(label='お問い合わせ内容', widget=forms.Textarea(attrs={'class': 'form-control reset-border-radius',}), required=True)
    
    # メール送信処理
    def send_email(self):
        # send email using the self.cleaned_data dictionary
        subject = self.cleaned_data['name']
        message = self.cleaned_data['email']
        from_email = settings.EMAIL_HOST_USER
        to = [settings.EMAIL_HOST_USER]

        send_mail(subject, message, from_email, to)
