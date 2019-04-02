from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Post, Contact
from django.views.generic.edit import FormView
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

class MainView(FormView):
    template_name = "main.html"
    form_class = ContactForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
          'all' : Post.objects.all(),
          's_p' : Post.objects.filter(genre='programming'),
          's_l' : Post.objects.filter(genre='language'),
          'work' : Post.objects.filter(section='works'),
          'form' : ContactForm(),
        }
        return context

    def form_valid(self, form):
      form.send_email()
      return super().form_valid(form)


    def post(self, request, *args, **kwargs):
      form = self.form_class(request.POST)
      if(form.is_valid()):
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        contact = Contact(
          name = name,
          email = email,
          message = message
        )
        contact.save()

        subject = ("New mail from " + name + " " + email)
        message = ('メールアドレス：' + email + "\n" + message)
        from_email = settings.EMAIL_HOST_USER
        to = [settings.EMAIL_HOST_USER]

        send_mail(subject, message, from_email, to)

      return render(request, 'main.html')
