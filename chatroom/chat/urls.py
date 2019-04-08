from django.urls import path
from .views import (MessageView,
                    MessageCreate
                    )

app_name = "messages"

urlpatterns = [
    path("", view=MessageView.as_view(), name='message-view'),
    path('add/', MessageCreate.as_view(success_url="/messages/"), name='add'),
]
