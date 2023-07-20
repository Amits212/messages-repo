from django.urls import path
from .views import MessageListCreateView, MessageRetrieveUpdateDeleteView, UnreadMessageListView

urlpatterns = [
    path('messages/', MessageListCreateView.as_view(), name='message-list-create'),
    path('messages/<int:pk>/', MessageRetrieveUpdateDeleteView.as_view(), name='message-retrieve-update-delete'),
    path('unread-messages/', UnreadMessageListView.as_view(), name='unread-messages'),
]
