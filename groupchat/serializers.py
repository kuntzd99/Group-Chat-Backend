from rest_framework import serializers
from .models import User, Group, Message, Membership, Reaction, Post, PostMessage, Invitation, Comment, CommentReaction, PostReaction


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'passwordDigest', 'image', 'bio')


class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'name', 'color', 'membersCount', 'creator', 'image')


class MessageSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Message
        fields = ('id', 'group', 'sender', 'groupName',
                  'senderUsername', 'message', 'time', 'likes',
                  'dislikes', 'laughs')


class MembershipSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Membership
        fields = ('id', 'group', 'user')


class ReactionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Reaction
        fields = ('id', 'type', 'user', 'username', 'message')


class CommentReactionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CommentReaction
        fields = ('id', 'type', 'user', 'username',
                  'comment')


class PostSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'user', 'caption', 'groupColor',
                  'likes', 'laughs', 'comments', 'time')


class PostMessageSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PostMessage
        fields = ('id', 'post', 'message')


class InvitationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Invitation
        fields = ('id', 'user', 'group', 'sender')


class CommentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'post', 'user', 'comment', 'username',
                  'time', 'likes', 'dislikes', 'laughs')


class PostReactionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PostReaction
        fields = ('id', 'type', 'user', 'username', 'post')
