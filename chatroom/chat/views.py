from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Room, Message
from django.views.generic import ListView

class MessageView(ListView):
    model = Message
    paginate_by = 50


    def get_queryset(self):
        room = Room.objects.get(pk=self.kwargs['pk'])
        return Message.objects.filter(room=room)


class MessageCreate(LoginRequiredMixin, CreateView):
    model = Message
    fields = ['content', 'room']

    def form_valid(self, form):

        form.instance.user = self.request.user
        return super().form_valid(form)


class RoomView(ListView):
    model = Room

class RoomCreate(LoginRequiredMixin, CreateView):
    model = Room
    fields = ['name']
