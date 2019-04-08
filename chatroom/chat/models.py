from django.db import models
from django.conf import settings


# Create your models here.

class Room(models.Model):
    """
    Room
    """

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Message(models.Model):
    """
    Message
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='messages', on_delete=models.CASCADE,)
    content = models.TextField(null=True, blank=True)
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    def save(self, *args, **kwargs):
        from chatroom.taskapp.celery import get_stock
        # Checks for commands
        if self.content.startswith('/stock='):
            get_stock.delay(self.content[7:], self.user.id, self.room.id)
            return

        super(Message, self).save(*args, **kwargs)
