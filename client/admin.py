from django.contrib import admin


from .models import Client , Todolist, Comment

admin.site.register(Client)

admin.site.register(Todolist)

admin.site.register(Comment)