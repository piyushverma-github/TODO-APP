from django.forms import ModelForm  # Import the ModelForm class from django.forms.
from app.models import TODO  # Import the TODO model from your app's models.

# Define a new form class named TODOForm that inherits from ModelForm.
class TODOForm(ModelForm):
    class Meta:  # Meta class provides metadata about the form.
        model = TODO  # Specify that this form is associated with the TODO model.
        fields = ['title', 'status', 'priority']  # Include these fields from the TODO model in the form.
