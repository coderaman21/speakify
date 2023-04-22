import json
from channels.generic.websocket import AsyncWebsocketConsumer
from utils.globalFunctions import get_room_name

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        currentUser = self.scope['user']
        if currentUser.is_anonymous:
            # Reject the connection
            await self.close()        
   
        roomName = await get_room_name(currentUser)
        if roomName is not None :
            self.roomGroupName = roomName
            
            await self.channel_layer.group_add(
                self.roomGroupName ,
                self.channel_name
            )
            await self.accept()

        
    async def disconnect(self , close_code):
        await self.channel_layer.group_discard(
            self.roomGroupName ,
            self.channel_name
        )
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json["username"]


        await self.channel_layer.group_send(
            self.roomGroupName,{
                "type" : "sendMessage" ,
                "message" : message ,
                "username" : username ,
            })
    async def sendMessage(self , event) :
        message = event["message"]
        username = event["username"]
        await self.send(text_data = json.dumps({"message":message ,"username":username}))
    
    