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
    # groups = models.ManyToManyField(
    #     Group,
    #     through='Membership',
    #     through_fields=('user', 'group'),
    #     null=True
    # )

    def __str__(self):
        return self.username


class Message(models.Model):
    message = models.TextField()
    groupName = models.CharField(max_length=100)
    senderUsername = models.CharField(max_length=100)
    group = models.IntegerField()
    sender = models.IntegerField()

    def __str__(self):
        return "message in " + self.groupName


class Membership(models.Model):
    group = models.IntegerField()
    user = models.IntegerField()

    def __str__(self):
        return "user with ID " + self.user + " in group with ID " + self.group


class Reaction(models.Model):
    type = models.CharField(max_length=100)
    user = models.IntegerField()
    username = models.CharField(max_length=100)
    message = models.IntegerField()
