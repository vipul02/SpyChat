# This file consist of all the details of spy, chats, friends
# from importing this we can use datetime.now()
from datetime import datetime


# class with named as Spy storing all the details of spy
class Spy:
    # constructor with arguments
    def __init__(self, name, salutation, rating, age):
        # assigning the name value to object.name
        self.name = name
        # assigning the salutation value to object.salutation
        self.salutation = salutation
        # assigning the rating value to object.rating
        self.rating = rating
        # assigning the age value to object.age
        self.age = age
        self.is_online = True
        self.chats = []
        # assigning current_status_msg of spy to None
        self.current_status_msg = None

# defining a object spy of class Spy, default user
spy = Spy('Naruto Uzumaki', 'Mr.', 4.0, 18)


# class with named as ChatMsg
class ChatMsg:
    # constructor with arguments
    def __init__(self, message, sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

# friends default
friend_one = Spy('Sasuke Uchiha', 'Mr.', 4.0, 18)
friend_two = Spy('Sakura', 'Ms.', 4.1, 18)
friend_three = Spy('Kakashi', 'Mr.', 4.5, 34)
# friends list having all friends
friends = [friend_one, friend_two, friend_three]