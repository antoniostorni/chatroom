from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Room, Message
from django.views.generic import ListView

class MessageView(ListView):
    model = Message


class MessageCreate(LoginRequiredMixin, CreateView):
    model = Message
    fields = ['content', 'room']

    def form_valid(self, form):

        form.instance.user = self.request.user
        return super().form_valid(form)

