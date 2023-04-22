from django.db import models
from Usermgmt.models import User

# Create your models here.
class ChatRoom(models.Model):
    user1 = models.ForeignKey(User,on_delete=models.CASCADE,related_name='chat_user1')
    user2 = models.ForeignKey(User,on_delete=models.CASCADE,related_name='chat_user2')
    room_name = models.CharField(max_length=50)

   