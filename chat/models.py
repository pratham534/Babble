from django.db import models
from account.models import User
# Create your models here.

class Message(models.Model):
    body = models.TextField()
    sent_by = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f'{self.sent_by}'
    

class Room(models.Model):
    WAITING = 'waiting'
    ACTIVE = 'active'
    CLOSED = 'closed'

    STATUS_CHOICES = [
        (WAITING, 'waiting'),
        (ACTIVE, 'active'),
        (CLOSED, 'closed'),
    ]

    roomid = models.CharField(max_length=150, unique=True)
    client = models.CharField(max_length=150)
    agent = models.ForeignKey(User, max_length=150, related_name='rooms', blank=True, null=True, on_delete=models.SET_NULL)
    messages = models.ManyToManyField(Message, blank=True)
    url = models.CharField(max_length=250, blank=True, null=True)
    status = models.CharField(max_length=150, choices=STATUS_CHOICES, default=WAITING)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f'{self.client} - {self.roomid}'