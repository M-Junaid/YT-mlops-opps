class Employee:
    # special method/magic method/dunder method- constructor
    def __init__(self):
        print("Started Executing attributes/data")
        self.id = 123
        self.salary = 50000
        self.designation = "developer"
        print("Completed Executing attributes/data")

    def travel(self,desination):
        print("This is travel method was called manually")  
        print(f'Empleyee is now travelling to {desination}')


# create an obj/instance of class
sam = Employee()
# sam.name = 'junaid' 
# print(id(sam))
# print(sam.name)

# printing the attributes
# print(sam.salary)

# calling the method
# sam.travel("London")
# print(type(sam))


# junaid = Employee()
# print(id(junaid))


