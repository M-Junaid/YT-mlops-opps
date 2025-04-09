class Chatbook:
    __user_id =0


    def __init__ (self):
        self.id = Chatbook.__user_id
        Chatbook.__user_id += 1
        self.__name = 'Default user'
        self.username = ''
        self.password = ''
        self.loggin = False
        # self.menu()

    @staticmethod
    def get_id():
        return Chatbook.__user_id
    
    @staticmethod
    def set_id(val):
        Chatbook.__user_id = val

    def get_name(self):
        return self.__name

    def set_name(self,value):
        self.__name = value


    def menu(self):
        user_input = input("""welcome to chatbook
                           1. Press 1 to signup
                           2. Press 2 to singin
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press any other key to exit
                           -> """)
        
        if user_input == '1':
            self.singup()
        elif user_input == '2':
            self.singin()
        elif user_input == '3':
            self.my_post()
        elif user_input == '4':
            self.sendmsg()
        else:
            exit()


    def singup(self):
        email = input('Enter your email -> ')
        password = input('Enter your password')
        self.username = email
        self.password = password
        print('You have successfully signed up')
        print("\n")
        self.menu()

    def singin(self):
        if self.username == '' and self.password == '':
            print('Please singup first by pressing 1 in the main menu')
        else:
            uname = input('Enter your email/username')
            pword = input('Enter your password')
            if self.username == uname and self.password == pword:
                print('You have successfully signed in')
                self.loggin = True
            else:
                print('Invalid username or password')

        print("\n")
        self.menu()

    def my_post(self):
        if self.loggin == True:
            txt = input('Enter your message here -> ')
            print(f'your message has been posted{txt} ->')
        else:
            print('You need to signin to post a message')

        print("\n")
        self.menu()
    
    def sendmsg(self):
        if self.loggin == True:
            txt = input('Enter your message here')
            frnd = input('whom to send the message')
            print(f'your message has been sent to {frnd}')
        else:
            print('You need to sign to send a message')

        print("\n")
        self.menu()
                
            


#uaer1 = Chatbook()   



        
