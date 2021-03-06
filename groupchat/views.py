from rest_framework import generics
from .serializers import UserSerializer, GroupSerializer, MessageSerializer, MembershipSerializer, ReactionSerializer, PostSerializer, PostMessageSerializer, InvitationSerializer, CommentSerializer, CommentReactionSerializer, PostReactionSerializer
from .models import User, Group, Message, Membership, Reaction, Post, PostMessage, Invitation, Comment, CommentReaction, PostReaction


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


class MembershipDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer


class ReactionList(generics.ListCreateAPIView):
    queryset = Reaction.objects.all()
    serializer_class = ReactionSerializer


class ReactionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reaction.objects.all()
    serializer_class = ReactionSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostMessageList(generics.ListCreateAPIView):
    queryset = PostMessage.objects.all()
    serializer_class = PostMessageSerializer


class PostMessageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostMessage.objects.all()
    serializer_class = PostMessageSerializer


class InvitationList(generics.ListCreateAPIView):
    queryset = Invitation.objects.all()
    serializer_class = InvitationSerializer


class InvitationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Invitation.objects.all()
    serializer_class = InvitationSerializer


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentReactionList(generics.ListCreateAPIView):
    queryset = CommentReaction.objects.all()
    serializer_class = CommentReactionSerializer


class CommentReactionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CommentReaction.objects.all()
    serializer_class = CommentReactionSerializer


class PostReactionList(generics.ListCreateAPIView):
    queryset = PostReaction.objects.all()
    serializer_class = PostReactionSerializer


class PostReactionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostReaction.objects.all()
    serializer_class = PostReactionSerializer
