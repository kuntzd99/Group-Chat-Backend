from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    membersCount = models.IntegerField()

    def __str__(self):
        return self.name


class User(models.Model):
    username = models.CharField(max_length=100)
    passwordDigest = models.CharField(max_length=100)
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, related_name='members')

    def __str__(self):
        return self.username


class Message(models.Model):
    message = models.TextField()
    groupName = models.CharField(max_length=100)
    senderUsername = models.CharField(max_length=100)
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='messages')

    def __str__(self):
        return "message in " + self.groupName
