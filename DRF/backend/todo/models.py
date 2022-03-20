from django.db import models


class User(models.Model):
    age = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    user_name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.user_name}'

class Project(models.Model):
    project_users = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=64)
    git_name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.project_name}'

class Todo(models.Model):
    text = models.CharField(max_length=64)
    time =  models.DateTimeField(auto_now=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


