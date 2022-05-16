from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    membersCount = models.IntegerField()
    creator = models.IntegerField()
    image = models.TextField()

    def __str__(self):
        return self.name


class User(models.Model):
    username = models.CharField(max_length=100)
    passwordDigest = models.CharField(max_length=100)
    image = models.TextField()
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.username


class Message(models.Model):
    message = models.TextField()
    groupName = models.CharField(max_length=100)
    senderUsername = models.CharField(max_length=100)
    group = models.IntegerField()
    sender = models.IntegerField()
    time = models.CharField(max_length=100)
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    laughs = models.IntegerField()

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


class Post(models.Model):
    user = models.IntegerField()
    caption = models.TextField(blank=True)
    groupColor = models.CharField(max_length=100)
    likes = models.IntegerField()
    laughs = models.IntegerField()
    comments = models.IntegerField()
    time = models.CharField(max_length=100)


class PostMessage(models.Model):
    post = models.IntegerField()
    message = models.IntegerField()


class Invitation(models.Model):
    user = models.IntegerField()
    group = models.IntegerField()
    sender = models.IntegerField()


class Comment(models.Model):
    post = models.IntegerField()
    comment = models.TextField()
    user = models.IntegerField()
    username = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    laughs = models.IntegerField()


class CommentReaction(models.Model):
    type = models.CharField(max_length=100)
    user = models.IntegerField()
    username = models.CharField(max_length=100)
    comment = models.IntegerField()


class PostReaction(models.Model):
    type = models.CharField(max_length=100)
    user = models.IntegerField()
    username = models.CharField(max_length=100)
    post = models.IntegerField()
