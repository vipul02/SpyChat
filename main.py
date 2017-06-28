# Program for secret chat
from spy_details import spy, Spy, ChatMsg, friends
from steganography.steganography import Steganography

print 'Welcome to EphemeralSpyChat'

status_msg = ['Hey there!I started using SpyChat', 'Busy...', 'Driving', 'Hacking', 'Sleeping']


def new_status():
    new_status_msg = raw_input('Enter your thoughtful status')
    return new_status_msg


def add_status():
    updated_status_msg = None
    if spy.current_status_msg is not None:
        print 'Your current status message is ' + spy.current_status_msg
    else:
        print 'You don\'t have any status message'
    status = raw_input('Do you want to select status message from the older(y/n)')
    if status.upper() == 'Y':
        item_position = 1
        for msg in status_msg:
            print '%d %s' % (item_position, msg)
            item_position += 1
        status_choice = int(raw_input("Enter the choice of your status message"))
        if len(status_msg) >= status_choice:
            updated_status_msg = status_msg[status_choice-1]
        else:
            print 'Not in option'
    elif status.upper() == 'N':
        updated_status_msg = new_status()
    else:
        print 'You might have entered the wrong choice, enter y or n'
    if updated_status_msg:
        print 'New/Updated status message is %s' % updated_status_msg
    else:
        print 'You don\'t have new/updated status message'
    return updated_status_msg


def add_friend():
    new_friend = Spy('', '', 0.0, 0)

    new_friend.name = raw_input('Please tell your friends name:')
    new_friend.salutation = raw_input('What should we call you Mr. or Ms.:')
    new_friend.rating = float(raw_input('Please tell your friends rating:'))
    new_friend.age = int(raw_input('Please tell your friends name:'))

    if 12 < new_friend.age < 50 and len(new_friend.name) > 0 and new_friend.rating >= spy.rating:
        friends.append(new_friend)
        print 'Friend added'
    else:
        print 'Sorry we can\'t enter spy with that invalid details'
    return len(friends)


def select_a_friend():
    position = 0
    for friend in friends:
        print '%d. %s %s aged %d having spy rating %.2f is online' % (position+1, friend.salutation, friend.name, friend.age, friend.rating)
        position += 1
    friend_choice = int(raw_input('Select one of your friend:'))
    if len(friends) >= friend_choice:
        pass
    else:
        print 'Wrong choice :_D'
    return friend_choice-1


def send_msg():
    friend_choice = select_a_friend()

    original_image = raw_input("Enter the name of your image with extension(like .jpg or .png")
    output_path = 'output.png'
    text = raw_input('What you wanna say to your comrade')
    Steganography.encode(original_image, output_path, text)

    new_chat = ChatMsg(text, True)
    friends[friend_choice].chats.append(new_chat)
    print 'Your secret image is ready!'


def read_msg():
    sender = select_a_friend()

    output_path = raw_input('What is the name of file(with ext)?')
    hidden_text = Steganography.decode(output_path)
    new_chat = ChatMsg(hidden_text, False)
    friends[sender].chats.append(new_chat)
    print 'Your secret message have been saved'


def read_chat_history():

    read_for = select_a_friend()

    print '\n'

    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            print '[%s] %s: %s' % (chat.time.strftime("%d %B %Y"), 'You said:', chat.message)
        else:
            print '[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"), friends[read_for].name, chat.message)


def start_chat():
    spy.name = spy.salutation + ' ' + spy.name
    show_menu = True
    if 12 < spy.age < 50:
        print 'Authentication complete! Welcome '\
        + spy.name + '\nAge:' + str(spy.age) + '\nRating:' + str(spy.rating) + 'Thanks for being with us.'
        while show_menu:
            menu_choices = "What do you want to do?\n1. Add a status update\n2. Add a friend\n"\
             + "3. Send a secret message\n4. Read a secret message\n5. Read Chats from a user\n6. Close Application:\n"
            menu_choice = int(raw_input(menu_choices))

            if menu_choice > 0:
                if menu_choice == 1:
                    spy.current_status_msg = add_status()
                elif menu_choice == 2:
                    no_of_friends = add_friend()
                    print 'You have %d friends' % no_of_friends
                elif menu_choice == 3:
                    send_msg()
                elif menu_choice == 4:
                    read_msg()
                elif menu_choice == 5:
                    read_chat_history()
                else:
                    show_menu = False
    else:
        print 'You are foreign to this group perhaps due to your age'


# function for checking if name is valid or not
def name_validation():
    # checks if spy name has some length
    if len(spy.name)>0:
        a = 0
        b = 0
        # loop to navigate over each character in spy.name
        for i in spy.name:
            # checks if character is alphabet
            if i.isalpha():
                # 'pass' just pass the statement
                pass
            # checks if character is digit
            elif i.isdigit():
                a += 1
            # checks if character is space
            elif i.isspace():
                pass
            # now the rest of characters will fall into it
            else:
                b += 1
        # for printing only alphabetical name no digit no special character
        # if the string has spaces before and after then it removes it
        # if statement will only run if there is no digit and no special character
        if a <= 0 and b <= 0:
            return True
        else:
            print "String must have digits or special characters"
            return False
    else:
        print "Your name is too short to be visible"
        return False

# Asks the user if they want to continue as existing user or want to enter a new username
existing=raw_input('Do you want to continue as ' + spy.salutation + ' ' + spy.name + ' (y/n)')
# checks the user input
# we have used upper() coz user can enter small y
if existing.upper() == "Y":
    # call the start_chat func
    start_chat(spy)
# we have used upper() coz user can enter small n
elif existing.upper() == "N":
    # initializing spy details to zero r nothing
    spy = Spy('', '', 0, 0.0)
    # take the input from user in the form of string
    spy.name = raw_input('Enter your name:')
    # call name_validation from validating name
    if name_validation():
        # strip()- strip off the spaces before and after the string
        spy.name = spy.name.strip(" ")
        # asking for the salutation, before name like Mr.Sayam
        spy.salutation = raw_input('What should we call you Mr. or Ms.?:')
        # ask the user to enter age and convert the string to integer
        spy.age = int(raw_input('Enter your age:'))
        # ask the user to enter rating and convert the string to float
        spy.rating = float(raw_input('Enter your rating:'))
        # call the start_chat func
        start_chat(spy)
    else:
        print 'Enter a valid name'
else:
    print 'Wrong choice dude'
