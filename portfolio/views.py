from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Post
from django.views.generic.edit import FormView
from .forms import ContactForm

class MainView(FormView):
    template_name = "main.html"
    form_class = ContactForm
    success_url = '/portfolio/main/'

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
