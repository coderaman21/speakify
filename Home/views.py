from django.shortcuts import render,redirect
from utils.globalFunctions import searchUser,create_room_name
from .models import ChatRoom

def home(request):
   user = request.user
   if not user.is_authenticated :
      return redirect('login')
   user.is_online = True
   user.save()
   anotherUser = searchUser(user)
   if anotherUser.exists():
      roomName = create_room_name()
      if not ChatRoom.objects.filter(user2 = user):
         ChatRoom.objects.create(
            user1 = user , 
            user2 = anotherUser[0],
            room_name = roomName
         )

   return render(request,'index.html')