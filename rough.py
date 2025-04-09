# lst = [1,2,3,4]
# my_str = 'hello'
# my_int = 123

# print(type(my_str))
# print(type(my_int))
# print(type(lst))

from oop_project import Chatbook
user1 = Chatbook()
print(user1.id)

# using static method directly from class rather than obj 
# Chatbook.set_id(10)

# user2 = Chatbook()
# print(user2.id)

# user3 = Chatbook()
# print(user3.id)

# getter and setter
# print(user1.get_name())
# user1.set_name('Junaid aslam')
# print(user1.get_name())


# # function vs method below
# lst = [1,2,3,4]

# # function
# a1 = len(lst)

# print(a1)

# user1 = Chatbook()
# user1.sendmsg()