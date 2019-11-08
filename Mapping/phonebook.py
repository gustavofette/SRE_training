myPhoneBook = {"Alim": "453-213-4567",
               "Navean": "123-456-7890",
               "Gustavo": "987-654-1230",
               "Veronica": "555-555-1234"
              }

def lookfor():
   looking = input("Name: ")
   found = myPhoneBook.get(looking)
   if found == None:
       print("%s is not in the phonebook" % looking)
   else:
       print(f' {looking} phone is {myPhoneBook[looking]}')

def addone():
   nname = input("New Name: ")
   pphone = input("Phone: ")
   myPhoneBook[nname] = pphone

def delone():
   nname = input("New Name: ")
   if nname in myPhoneBook:
       del myPhoneBook[nname]
   else:
       print(f'{nname} not in the phonebook')

while True:
   print ("My PhoneBook")
   print ("===============")
   print ("")
   print ("1- Look for a name")
   print ("2- Add a new name")
   print ("3- Del a name")
   print ("4- List all")
   print ("5- Quit")
   print ("")
   print ("What do you want to do: ")
   
   YourChoice = input()
   
   if YourChoice == "1":
       lookfor()
   
   elif YourChoice == "2":
       addone()
   
   elif YourChoice == "3":
       delone()
   
   elif YourChoice == "4":
       print(myPhoneBook)
   
   elif YourChoice == "5":
       print ("Bye Bye")
       break
   
   else:
       print("Stop kidding")
