from rest_framework import generics
from .serializers import UserSerializer, GroupSerializer, MessageSerializer, MembershipSerializer, ReactionSerializer
from .models import User, Group, Message, Membership, Reaction


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupList(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class MessageList(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MembershipList(generics.ListCreateAPIView):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer


class ReactionList(generics.ListCreateAPIView):
    queryset = Reaction.objects.all()
    serializer_class = ReactionSerializer


class ReactionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reaction.objects.all()
    serializer_class = ReactionSerializer
