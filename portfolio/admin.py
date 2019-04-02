from django.contrib import admin
from .models import Post, Contact

class PostAdmin(admin.ModelAdmin):
    pass
    admin.site.register(Post)

class ContactAdmin(admin.ModelAdmin):
    pass
    admin.site.register(Contact)

