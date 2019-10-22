class Person:
   def __init__(self, name, email, phone):
       self.name = name
       self.email = email
       self.phone = phone
   def greet(self, other_person):
       print('Hello {}, I am {}!'.format(other_person.name, self.name))

person1 = Person("Sonny", "sonny@hotmail.com", "483-123-456")
person2 = Person("Jordan", "jordan@aol.com", "463-456-789")

person1.greet(person2)
person2.greet(person1)

print(person1.email, person1.phone)
print(person2.email, person2.phone)