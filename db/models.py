import sys

try:
    from django.db import models
except Exception:
    print('Exception: Django Not Found, please install it with "pip install django".')
    sys.exit()


# Sample User model
class Test(models.Model):
    question = models.TextField()
    a = models.CharField(max_length=255)
    b = models.CharField(max_length=255)
    c = models.CharField(max_length=255)
    d = models.CharField(max_length=255)

    def __str__(self):
        return self.question


class Users(models.Model):
    username = models.CharField(max_length=255)
    test_name = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

