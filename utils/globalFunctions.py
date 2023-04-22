from Home.models import ChatRoom
import random
from Usermgmt.models import User
from asgiref.sync import sync_to_async
from django.db.models import Q

def create_room_name():
    slug = 'Chat' +'-'

    while True :
        slug+= str(random.randint(100000,1000000))
        if not ChatRoom.objects.filter(room_name = slug):
            break
    return slug

def searchUser(user):
    interests = user.interests
    otherUser = User.objects.filter(is_online = True,interests__overlap = interests).exclude(id = user.id)
    if not otherUser.exists():
        otherUser = User.objects.filter(is_online = True).exclude(id = user.id)
    
    return otherUser

@sync_to_async
def get_room_name(user):
    roomName = None
    room = ChatRoom.objects.filter(Q(user1 = user)|Q(user2 = user))
    if room.exists():
        roomName = room[0].room_name

    return roomName
    