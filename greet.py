greeting = "Hello {}, it is very nice to meet you and your friend {}!"

name_of_user = input("What is your name? ")
length_of_name = len(name_of_user)
if length_of_name > 0:
    name_of_friend = input("What is your friend's name? ")
    while len(name_of_friend) <= 4:
        name_of_friend = input("What is your friend's name? ")
    print(greeting.format(name_of_user,name_of_friend))
    