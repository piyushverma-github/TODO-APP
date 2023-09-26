from django.contrib import admin
from django.urls import path
from app.views import home, login, signup, add_todo, signout, delete_todo, change_todo

# Define URL patterns for the app
urlpatterns = [
    path('', home, name='home'),  # URL for the home page, mapped to the 'home' view
    path('login/', login, name='login'),  # URL for the login page, mapped to the 'login' view
    path('signup/', signup),  # URL for the signup page, mapped to the 'signup' view
    path('add-todo/', add_todo),  # URL for adding a new TODO item, mapped to the 'add_todo' view
    path('delete-todo/<int:id>', delete_todo),  # URL for deleting a TODO item, mapped to the 'delete_todo' view
    path('change-status/<int:id>/<str:status>', change_todo),  # URL for changing the status of a TODO item, mapped to the 'change_todo' view
    path('logout/', signout),  # URL for logging out, mapped to the 'signout' view
]
