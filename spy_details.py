# This file consist of all the details of spy, chats, friends
from datetime import datetime
class Spy:
    def __init__(self,name,salutation,rating,age):
        self.name=name
        self.salutation=salutation
        self.rating=rating
        self.age=age
        self.is_online=True
        self.chats=[]
        self.current_status_msg=None

class chat_msg:
    def __init__(self,message,sent_by_me):
        self.message=message
        self.time=datetime.now()
        self.sent_by_me=sent_by_me
spy=Spy('','',0.0,0)
friends = []