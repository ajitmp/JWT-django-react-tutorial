from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.user.username



# [
#     {
#         "username": "user1",
#         "password": "password1",
#         "profile": {
#             "first_name": "Sam",
#             "last_name": "Smith",
#             "email": "sam@smith.com"
#         }
#     },
#     {
#         "username": "user2",
#         "password": "password2",
#         "profile": {
#             "first_name": "Tim",
#             "last_name": "Allen",
#             "email": "tim@allen.com"
#         }
#     }
# ]