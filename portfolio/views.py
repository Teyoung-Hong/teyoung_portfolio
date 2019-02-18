from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Post

class MainView(TemplateView):
    template_name = "main.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
          'all' : Post.objects.all(),
          's_p' : Post.objects.filter(section='skills').filter(genre="programming"),
          's_l' : Post.objects.filter(section='skills').filter(genre='languages'),
          'work' : Post.objects.filter(section='works')
        }
        return context
