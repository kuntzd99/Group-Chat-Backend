from rest_framework import serializers
from .models import User, Group, Message, Membership, Reaction


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # groups = serializers.HyperlinkedRelatedField(
    #     view_name='group_detail',
    #     many=True,
    #     read_only=True
    # )

    class Meta:
        model = User
        fields = ('id', 'username', 'passwordDigest')


class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'name', 'color', 'membersCount')


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    # group = serializers.HyperlinkedRelatedField(
    #     view_name='group_detail',
    #     read_only=True
    # )
    # sender = serializers.HyperlinkedRelatedField(
    #     view_name='user_detail',
    #     read_only=True
    # )

    class Meta:
        model = Message
        fields = ('id', 'group', 'sender', 'groupName',
                  'senderUsername', 'message')


class MembershipSerializer(serializers.HyperlinkedModelSerializer):
    # group = serializers.HyperlinkedRelatedField(
    #     view_name='group_detail',
    #     read_only=True
    # )
    # user = serializers.HyperlinkedRelatedField(
    #     view_name='user_detial',
    #     read_only=True
    # )

    class Meta:
        model = Membership
        fields = ('id', 'group', 'user')


class ReactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reaction
        fields = ('id', 'type', 'user', 'username', 'message')
