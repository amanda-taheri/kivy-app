from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import ObjectProperty
import datetime

class DataBase:
    
    def __init__(self, filename):
        self.filename = filename
        self.users = None
        self.file = None
        self.load()

    def load(self):
        self.file = open(self.filename , "r")
        self.users = {}

        for line in self.file:
            email , password , Fname , Lname , phone , created = line.strip().split(";")
            self.users[email] = (password , Fname , Lname , phone , created)

        self.file.close()

    def get_user(self, email):
        if email in self.users:
            return self.users[email]
        else:
            return -1

    def validate(self, email, password):
        if self.get_user(email) != -1:
            return self.users[email][0] == password
        else:
            return False
        

class Signin  (MDApp):
        email = ObjectProperty(None)
        password = ObjectProperty(None)
        def build (self):
            self.theme_cls.theme_style = 'Light'
            self.theme_cls.primary_palette='Green'
            return Builder.load_file('signin.kv')
     
        def logger(self):
            db = DataBase("users.txt")
            if ((self.root.ids.email.text != "") and (self.root.ids.password.text != "")):
                if db.validate(self.root.ids.email.text, self.root.ids.password.text):
                        self.reset()
                        self.root.ids.slide.load_next (mode = "next")
                           
                else:
                        self.root.ids.ErrorL.text = 'invalid email or password'
            else: 
                self.root.ids.email.helper_text = "Enter your email"
                self.root.ids.password.helper_text = "Enter you password"
                    
                
        
        def clear (self):
                self.root.ids.welcome_label.text = "Welcome"
                self.reset()
                
        def reset (self):
                self.root.ids.email.text = ""
                self.root.ids.password.text = ""
                
    

Signin().run()
