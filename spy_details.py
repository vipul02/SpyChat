# This file consist of all the details of spy, chats, friends
from datetime import datetime


class Spy:
    def __init__(self, name, salutation, rating, age):
        self.name = name
        self.salutation = salutation
        self.rating = rating
        self.age = age
        self.is_online = True
        self.chats = []
        self.current_status_msg = None

spy = Spy('Naruto Uzumaki', 'Mr.', 4.0, 18)


class ChatMsg:
    def __init__(self, message, sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

friend_one = Spy('Sasuke Uchiha', 'Mr.', 4.0, 18)
friend_two = Spy('Sakura', 'Ms.', 4.1, 18)
friend_three = Spy('Kakashi', 'Mr.', 4.5, 34)
friends = [friend_one, friend_two, friend_three]