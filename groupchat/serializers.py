from rest_framework import serializers
from .models import User, Group, Message, Membership, Reaction, Post, PostMessage


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'passwordDigest')


class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'name', 'color', 'membersCount', 'creator')


class MessageSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Message
        fields = ('id', 'group', 'sender', 'groupName',
                  'senderUsername', 'message', 'time')


class MembershipSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Membership
        fields = ('id', 'group', 'user')


class ReactionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Reaction
        fields = ('id', 'type', 'user', 'username', 'message')


class PostSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'user', 'caption')


class PostMessageSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PostMessage
        fields = ('id', 'post', 'message')
