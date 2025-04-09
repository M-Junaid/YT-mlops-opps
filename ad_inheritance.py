# # Single or Basic Inheritance

# # Base Class
# class Parent:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         print(f"Hello, my name is {self.name}.")

# # Derived Class
# class Child(Parent):
#     def play(self):
#         print(f"{self.name} is playing.")

# # Create an instance of Child
# child = Child("Alice")
# child.greet()  # Output: Hello, my name is Alice.
# child.play()   # Output: Alice is playing.

# ----------------------------------------


# Multi-level Inheritance

# Base Class
# class Grandparent:
#     def __init__(self, name):
#         self.name = name

#     def tell_story(self):
#         print(f"{self.name} is telling a story.")

# # Intermediate Class    
# class Parent(Grandparent):
#     def work(self):
#         print(f"{self.name} is working.")   

# # Derived Class
# class Child(Parent):

#     def play(self):
#         print(f"{self.name} is playing.")   

# # Create an instance of Child
# child = Child("Alice")
# child.tell_story()  # Output: Alice is telling a story.
# child.work()        # Output: Alice is working.
# child.play()        # Output: Alice is playing

# ----------------------------------------     
# Hierarchical Inheritance    

# Base Class

# class Parent:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         print(f"Hello, my name is {self.name}.")

# # Derived Class 1
# class Child1(Parent):

#     def play(self):
#         print(f"{self.name} is playing.")

# # Derived Class 2
# class Child2(Parent):

#     def study(self):
#         print(f"{self.name} is studying.")

# # Create instances of Child1 and Child2
# child1 = Child1("Alice")
# child2 = Child2("Bob")

# child1.greet()  # Output: Hello, my name is Alice.
# child1.play()   # Output: Alice is playing.

# child2.greet()  # Output: Hello, my name is Bob.
# child2.study()  # Output: Bob is studying.
# # ----------------------------------------

# Multiple Inheritance

# comman base class

# class A:
#     def __init__(self,name):
#         self.name = name

#     def greet(self):
#         print(f"Hello from class A {self.name}.")

# # Inherited class 1
# class B(A):
#     def greet(self):
#         print(f"Hello from class B {self.name}.")
#         super().greet()

# # Inherited class 2
# class C(A):
#     def greet(self):
#         print(f"Hello from class C {self.name}.")
#         super().greet()

# # Derived class
# class D(B,C):
#     def greet(self):
#         print(f"Hello from class D {self.name}.")
#         super().greet() 

# # Create an instance of D
# d = D("Alice")
# d.greet()   

# Output:
# Hello from class D Alice.
# Hello from class B Alice.
# Hello from class C Alice.
# Hello from class A Alice.

# ----------------------------------------

# Hybrid Inheritance

# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# intermediate class 1 (Hierarchical)
class Mammal(Animal):
    def feed(self):
        print(f"{self.name} is being feding milk.")

# intermediate class 2 (Multiple)
class Bird(Animal):
    def fly(self):
        print(f"{self.name} is flying.")

# Derived class (Multiple Inheritance)
class Bat(Mammal, Bird):
    def __init__(self, name):
    
        Mammal.__init__(self, name) # Explictly calling the constructor

    def nocturnal(self):
        print(f"{self.name} is nocturnal.")

# Create an instance of Bat
bat = Bat("Bruce")

bat.speak()  # Output: Bruce makes a sound.
bat.feed()   # Output: Bruce is being feding milk.
bat.fly()    # Output: Bruce is flying.
bat.nocturnal()  # Output: Bruce is nocturnal.




    