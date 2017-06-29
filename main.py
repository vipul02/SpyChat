# Program for secret chat
# from spy_details.py we are importing some classes and functions
from spy_details import spy, Spy, ChatMsg, friends
# importing Steganography funcntion from steganogarphy for hiding text into the images
from steganography.steganography import Steganography
# welcome message to the user
print 'Welcome to EphemeralSpyChat'
# default status messages like whats app does
status_msg = ['Hey there!I started using SpyChat', 'Busy...', 'Driving', 'Hacking', 'Sleeping']


# function to return new status message
def new_status():
    # storing the new status message in a string variable
    new_status_msg = raw_input('Enter your thoughtful status:\n')
    return new_status_msg


# function to print current status message
def current_status_msg():
    # checking if user had any current status message
    # we use 'is not' here rather tha '!=' coz the former one is more suitable or valid
    if spy.current_status_msg is not None:
        print 'Your current status message is ' + spy.current_status_msg
    else:
        print 'You don\'t have any status message'


# function to add status
def add_status():
    # initially setting updated message to None
    updated_status_msg = None
    # ask the user if they want to set current status message from older ones
    status = raw_input('Do you want to select status message from the older(y/n):\n')
    # we have used upper in case user enter small y
    if status.upper() == 'Y':
        # setting the item position to one
        item_position = 1
        # loop to navigate over all the status messages
        for msg in status_msg:
            print '%d %s' % (item_position, msg)
            # updating the item position
            item_position += 1
        # ask the user to enter status choice and convert it to integer
        status_choice = int(raw_input("Enter the choice of your status message:\n"))
        # checking the index error
        if status_choice <= len(status_msg):
            # updating the message by retrieving it from list of status message
            updated_status_msg = status_msg[status_choice-1]
        else:
            print 'Not in option'
    elif status.upper() == 'N':
        # calling new status function to get new status message
        updated_status_msg = new_status()
    else:
        print 'You might have entered the wrong choice, enter y or n'
    # if there is any updated message then its true
    if updated_status_msg:
        print 'New/Updated status message is %s' % updated_status_msg
    else:
        print 'You don\'t have new/updated status message'
    # function returns updated message to the calling function
    return updated_status_msg


# function to add a new friend to friend list
def add_friend():
    # initially setting details of friend to zero
    new_friend = Spy('', '', 0.0, 0)
    # asking the user to enter name
    new_friend.name = raw_input('Please tell your friend name:')
    # asking the user to enter salutation
    new_friend.salutation = raw_input('What should we call you Mr. or Ms.:')
    # asking the user to enter rating and converting it to float
    new_friend.rating = float(raw_input('Please tell your friends rating:'))
    # asking the user to enter age and converting it to integer
    new_friend.age = int(raw_input('Please tell your friends age:'))

    # checks if user has right age to proceed, valid name and rating greater than user
    if 12 < new_friend.age < 50 and name_validation() and new_friend.rating >= spy.rating:
        # appending the new friend to friends list
        friends.append(new_friend)
        print 'Friend added'
    else:
        print 'Sorry we can\'t enter spy with that invalid details'
    # returning the no. of friends to the calling function
    return len(friends)


# function  to select a friend to start chatting with
def select_a_friend():
    position = 0
    # loop to navigate the list of friends
    for friend in friends:
        # printing the friend detail
        print '%d. %s %s aged %d having spy rating %.2f is online' % (position+1, friend.salutation, friend.name, friend.age, friend.rating)
        # updating the position of list item of friends
        position += 1
    # ask the user to select the friend and convert it into integer
    friend_choice = int(raw_input('Select one of your friend:'))
    # checking the index error
    if len(friends) >= friend_choice:
        # just pass the control flow
        pass
    else:
        print 'Wrong choice :_D'
    # returning the index of friend choice
    return friend_choice-1


# function to send messages
def send_msg():
    # calling function to select a friend and then storing the index of friends list to friend_choice
    friend_choice = select_a_friend()
    # asking the user to enter the name of original image with extension
    original_image = raw_input("Enter the name of your image with extension(like .jpg or .png")
    # setting the path for the image with hidden text message
    output_path = 'output.png'
    # asking the user to enter the text message to be hide
    text = raw_input('What you wanna say to your comrade')
    # by the below code we encode the text message into the original and
    # produce an output image with hidden text message
    Steganography.encode(original_image, output_path, text)
    # declaring a new object of ChatMsg type class taking two arguments,
    # one is text message and another is boolean True stating that message sent ny me
    new_chat = ChatMsg(text, True)
    # appending the text message in chats of a selected friend
    friends[friend_choice].chats.append(new_chat)
    print 'Your secret image is ready!'


# function to read a message
def read_msg():
    # selecting a friend by calling function and storing the index in sender variable
    sender = select_a_friend()
    # asking the user for the name of image with extension
    # to decode the hidden text message from it
    output_path = raw_input('What is the name of file(with ext)?')
    # decoding the hidden text message and storing it
    hidden_text = Steganography.decode(output_path)
    # declaring a new object of ChatMsg type class taking two arguments,
    # one is text message and another is boolean False stating that message was not sent ny me
    new_chat = ChatMsg(hidden_text, False)
    # appending the text message in chats of a selected friend
    friends[sender].chats.append(new_chat)
    print 'Your secret message have been saved'


# function to read chat history with a particular friend
def read_chat_history():
    # function to select a friend with which to want to read chat history
    read_for = select_a_friend()
    # Printing new line
    print '\n'
    # navigating in all chats with a particular friend
    for chat in friends[read_for].chats:
        # checking if the chat message was sent by you
        if chat.sent_by_me:
            # printing the message with time of type
            print '[%s] %s: %s' % (chat.time.strftime("%d %B %Y"), 'You said:', chat.message)
        else:
            print '[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"), friends[read_for].name, chat.message)


# function to start chat with a friend
def start_chat():
    # collabrating the spy name and spy salutation into spy name
    spy.name = spy.salutation + ' ' + spy.name
    # initially setting spy menu to True
    show_menu = True
    # checking if user has valid age
    if 12 < spy.age < 50:
        # printing the authentication message
        # using \ so print multi line
        print 'Authentication complete! Welcome '\
         + spy.name + '\nAge:' + str(spy.age) + '\nRating:' + str(spy.rating) + ' Thanks for being with us.'
        # while loop with condition show_menu to be True and stops as show_menu becomes False
        while show_menu:
            # storing the choices into menu_choice
            menu_choices = "What do you want to do?\n1. Know current status message\n"\
             + "2. Add a status update\n3. Add a friend\n4. Send a secret message\n"\
             + "5. Read a secret message\n6. Read Chats from a user\n7. Close Application:\n"
            # getting the mnu choice from user and converting it to int and storing it to a variable
            menu_choice = int(raw_input(menu_choices))
            # condition to check if user has selected the right menu choice
            if menu_choice > 0:
                # first choice
                if menu_choice == 1:
                    # calling function to check the current status message
                    current_status_msg()
                # second choice
                if menu_choice == 2:
                    # calling add_status function to add status message and returning
                    # the updated status message and storing it to current status message
                    spy.current_status_msg = add_status()
                # third choice
                elif menu_choice == 3:
                    # calling the function add friend and in return get the no. of friends
                    no_of_friends = add_friend()
                    # printing the no. of friends you have
                    print 'You have %d friends' % no_of_friends
                # fourth choice
                elif menu_choice == 4:
                    # calling send_msg function to send messages
                    send_msg()
                # fifth choice
                elif menu_choice == 5:
                    # calling read_msg function to read the messages sent to you
                    read_msg()
                # sixth choice
                elif menu_choice == 6:
                    # read chat history of a friend
                    read_chat_history()
                # in other cases setting show_menu to False and closing the application
                else:
                    show_menu = False
    # if you do not have valid age  then else will run
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
    start_chat()
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
        start_chat()
    else:
        print 'Enter a valid name'
else:
    print 'Wrong choice dude'
