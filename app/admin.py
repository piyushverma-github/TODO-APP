from django.contrib import admin #Imports the admin module from the Django framework, which is used for creating an admin interface.
from app.models import TODO #Imports the TODO model from your Django app's models, representing data structure.
# Register your models here. 
admin.site.register(TODO) #Registers the TODO model with the Django admin interface, enabling admin management for it.
