# Program for secret chat
from spy_details import spy, Spy, chat_msg, friends
from steganography.steganography import Steganography
from datetime import datetime

print 'Welcome to EphemeralSpyChat'

status_msg=['Hey there!I started using SpyChat', 'Busy...', 'Driving', 'Hacking', 'Sleeping']

def new_status():
    new_status_msg = raw_input('Enter your thoughtful status')
    return new_status_msg

def add_status():
    new_status_msg=None
    if spy.current_status_msg != None:
        print 'Your current status message is ' + spy.current_status_msg
    else:
        print 'You don\'t have any status message'
    status=raw_input('Do you want to select status message from the older(y/n)')
    if status.upper() == 'Y':
        item_position = 1
        for msg in status_msg:
            print '%d %s' % (item_position, msg)
            item_position += 1
        status_choice = int(raw_input("Enter the choice of your status message"))
         if len(status_msg)>=status_choice:
            new_status_msg = status_msg[status_choice-1]
        else:
             print 'Not in option'
    elif status.upper() == 'N':
        new_status_msg = new_status()
    else:
        print 'You might have entered the wrong choice, enter y or n'
    if new_status_msg:
        print 'New/Updated status message is %s' % (new_status_msg)
    else:
        print 'You don\'t have new/updated status message'
    return new_status_msg

def add_friend():
    new_friend = Spy('','',0.0,0)

    new_friend.name = raw_input('Please tell your friends name:')
    new_friend.salutation = raw_input('What should we call you Mr. or Ms.:')
    new_friend.rating = float(raw_input('Please tell your friends rating:'))
    new_friend.age = int(raw_input('Please tell your friends name:'))

    if new_friend.age>12 and new_friend.age<50 and len(new_friend.name)>0 and new_friend.rating>=spy.rating:
        friends.append(new_friend)
        print 'Friend added'
    else:
        print 'Sorry we can\'t enter spy with that invalid details'
    return len(friends)

def select_a_frnd():
    position=0
    for friend in friends:
        print '%d. %s %s aged %d having spy rating %.2f is online' % (position+1, friend.salutation, friend.name, friend.age, friend.rating)
        position+=1
    frnd_choice=int(raw_input('Select one of your friend:'))
    if len(friends)>=frnd_choice:
        pass
    else:
        print 'Wrong choice :_D'
    return frnd_choice-1

def send_msg():
    frnd_choice = select_a_frnd()

    original_image = raw_input("Enter the name of your image with extension(like .jpg or .png")
    output_path = 'output.png'
    text = raw_input('What you wanna say to your comrade')
    Steganography.encode(original_image, output_path, text)

    new_chat = chat_msg(text,True)
    friends[frnd_choice].chats.append(new_chat)
    print 'Your secret image is ready!'

def read_msg():
    sender = select_a_frnd()

    output_path = raw_input('What is the name of file(with ext)?')
    hidden_text=Steganography.decode(output_path)
    new_chat = chat_msg(hidden_text, False)
    friends[sender].chats.append(new_chat)
    print 'Your secret message have been saved'

def read_chat_history():

    read_for = select_a_frnd()

    print '\n'

    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            print '[%s] %s: %s' % (chat.time.strftime("%d %B %Y"), 'You said:', chat.message)
        else:
            print '[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"), friends[read_for].name, chat.message)



def start_chat(spy):
    spy.name=spy.salutation + ' ' + spy.name

    if spy.age>12 and spy.age<50:
        print 'Authentication complete! Welcome ' + spy.name + '\nAge:'\
            + spy.age + '\nRating:' + spy.rating + 'Thanks for being with us.'
        while show_menu:
            menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"
            menu_choice = int(raw_input(menu_choices))

            if menu_choice>0:
                if menu_choice==1:
                    spy.current_status_msg=add_status()
                elif menu_choice==2:
                    no_of_friends=add_friend()
                    print 'You have %d friends' %(no_of_friends)
                elif menu_choice==3:
                    send_msg()
                elif menu_choice==4:
                    read_msg()
                elif menu_choice==5:
                    read_chat_history()
                else:
                    show_menu=False
    else:
        print 'You are foreign to this group perhaps due to your age'

def login():
    spy.name=raw_input('Enter your name:')
    if(len(spy.name)>0):
        spy.salutation=raw_input('What should we call you Mr. or Ms.?:')
        spy.age=int(raw_input('Enter your age:'))
        spy.rating=float(raw_input('Enter your rating:'))
        start_chat(spy)
    else:
        print 'Enter a valid name'

if spy.name=='':
    login()
else:
    existing=raw_input('Do you want to continue as ' + spy.salutation + ' ' + spy.name + ' (y/n)')
    if existing.upper() == "Y":
        start_chat(spy)
    else:

        spy = Spy('', '', 0, 0.0)
        login()
