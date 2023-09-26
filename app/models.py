from django.db import models
from django.contrib.auth.models import User

# Define the TODO model
class TODO(models.Model):
    # Define choices for the 'status' field
    status_choices = [
        ('C', 'COMPLETED'),  # Choice for completed status
        ('P', 'PENDING'),    # Choice for pending status
    ]

    # Define choices for the 'priority' field
    priority_choices = [
        ('1', '1️⃣'),   # Choice for priority level 1
        ('2', '2️⃣'),   # Choice for priority level 2
        ('3', '3️⃣'),   # Choice for priority level 3
        ('4', '4️⃣'),   # Choice for priority level 4
        ('5', '5️⃣'),   # Choice for priority level 5
        ('6', '6️⃣'),   # Choice for priority level 6
        ('7', '7️⃣'),   # Choice for priority level 7
        ('8', '8️⃣'),   # Choice for priority level 8
        ('9', '9️⃣'),   # Choice for priority level 9
        ('10', '🔟'),    # Choice for priority level 10
    ]

    title = models.CharField(max_length=50)  # Field for the title of the TODO item
    status = models.CharField(max_length=2, choices=status_choices)  # Field for status with choices
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Field for the associated user
    date = models.DateTimeField(auto_now_add=True)  # Field for the creation date
    priority = models.CharField(max_length=2, choices=priority_choices)  # Field for priority with choices

