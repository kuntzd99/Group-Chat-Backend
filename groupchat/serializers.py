from rest_framework import serializers
from .models import User, Group, Message


class UserSerializer(serializers.HyperlinkedModelSerializer):
    groups = serializers.HyperlinkedRelatedField(
        view_name='group_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = User
        fields = ('username', 'passwordDigest', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    members = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Group
        fields = ('name', 'color', 'members', 'membersCount')


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    group = serializers.HyperlinkedRelatedField(
        view_name='group_detail',
        read_only=True
    )
    sender = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        read_only=True
    )

    class Meta:
        model = Message
        fields = ('group', 'sender', 'groupName',
                  'senderUsername', 'message')
