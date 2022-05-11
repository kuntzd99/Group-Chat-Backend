# tunr/urls.py
from unicodedata import name
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('users/', views.UserList.as_view(), name='user_list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('groups/', views.GroupList.as_view(), name='group_list'),
    path('groups/<int:pk>', views.GroupDetail.as_view(), name='group_detail'),
    path('messages/', views.MessageList.as_view(), name='message_list'),
    path('messages/<int:pk>', views.MessageDetail.as_view(), name='message_detail'),
    path('memberships/', views.MembershipList.as_view(), name='membership_list'),
    path('memberships/<int:pk>', views.MembershipDetail.as_view(),
         name='membership_detail'),
    path('reactions/', views.ReactionList.as_view(), name='reaction_list'),
    path('reactions/<int:pk>', views.ReactionDetail.as_view(), name='reaction_detail')
]
