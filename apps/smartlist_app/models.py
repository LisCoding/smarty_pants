from __future__ import unicode_literals
from django.db import models
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.email

class Todo(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    #user can create many todos
    created_by = models.ForeignKey(User, related_name = "created_todos")

class Resource(models.Model):
    title = models.CharField(max_length=255, default="null")
    link = models.CharField(max_length=255)
    snippet = models.CharField(max_length=255, default="null")

    #add youtube video field
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    #Todo has many resources
    resource_owner = models.ForeignKey(Todo, related_name = "created_resources")
