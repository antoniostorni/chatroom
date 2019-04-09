from django.urls import path
from django.urls import path, re_path

from .views import (MessageView,
                    MessageCreate,
                    RoomView,
                    RoomCreate,
                    )

app_name = "chatroom"

urlpatterns = [
    re_path(r"^room/(?P<pk>\d+)/messages/$", view=MessageView.as_view(), name='message-view'),
    path('messages/add/', MessageCreate.as_view(success_url="/chat/rooms/"), name='message-add'),
    path("rooms/", view=RoomView.as_view(), name='room-view'),
    path("rooms/add/", view=RoomCreate.as_view(success_url='/chat/rooms/'), name='room-add')
]
