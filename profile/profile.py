from kivymd.app import MDApp
from kivy.lang import Builder
import re
from kivy.properties import ObjectProperty
import datetime

class DataBase():
        def __init__(self, filename):
                self.filename = filename
                self.users = None
                self.file = None
                self.load()

        def load(self):
                self.file = open(self.filename, "r")
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

        def add_user(self , email , password , Fname , Lname , phone):
                if email.strip() not in self.users:
                        self.users[email.strip()] = (password.strip(), Fname.strip(), Lname.strip() , phone.strip() , DataBase.get_date())
                        self.save()
                        return 1
                else:
                        print("Email exists already")
                        return -1

        def validate(self, email, password):
                if self.get_user(email) != -1:
                        return self.users[email][0] == password
                else:
                        return False

        def save(self):
                with open(self.filename, "w") as f:
                        for user in self.users:
                                f.write(user + ";" + self.users[user][0] + ";" + self.users[user][1] + ";" + self.users[user][2] + ";" + self.users[user][3] + ";" + self.users[user][4] + "\n")

        @staticmethod
        def get_date():
                return str(datetime.datetime.now()).split(" ")[0]




class ProfileApp (MDApp):
        email = ObjectProperty(None)
        password = ObjectProperty(None)
        Fname = ObjectProperty(None)
        Lname = ObjectProperty(None)
        Phone = ObjectProperty(None)

        def build(self):
                self.theme_cls.theme_style = "Light"
                self.theme_cls.primary_palette = "Green"
                return Builder.load_file('profile.kv')

        def next(self):
               if ((self.root.ids.Fname.text != "") and (self.root.ids.Lname.text != "")):
                        self.root.ids.slide.load_next (mode = "next")
                        self.root.ids.Name.text_color = self.theme_cls.primary_color
                        self.root.ids.progress.value = 100
                        self.root.ids.name.text_color = self.theme_cls.primary_color
                        self.root.ids.name.icon = "check-decagram"
               else:
                       self.root.ids.Fname.helper_text = "Enter a text "
                       self.root.ids.Lname.helper_text = "Enter a text"
               
                        

        def next1(self): 
                regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b' 
                Tregex = r'09(1[0-9]|3[1-9]|2[0-9])-?[0-9]{3}-?[0-9]{4}'
                if ((self.root.ids.email.text != "") and (self.root.ids.phone.text != "")):
                        if ( (re.search (regex , self.root.ids.email.text) ) and (re.search (Tregex , self.root.ids.phone.text))):
                                self.root.ids.slide.load_next (mode = "next")
                                self.root.ids.Contact.text_color = self.theme_cls.primary_color
                                self.root.ids.progress1.value = 100
                                self.root.ids.contact.text_color = self.theme_cls.primary_color
                                self.root.ids.contact.icon = "check-decagram" 
                                self.root.ids.ErrorT.text = ""
                                
                        else:
                                self.reset()
                                self.root.ids.ErrorT.text = "Invalid Email or Phone number"
                
                else:   
                        self.root.ids.email.helper_text = "Enter your email"
                        self.root.ids.phone.helper_text = "Enter your phone number"
                        
                        
        def previous(self):
                self.root.ids.slide.load_previous()
                self.root.ids.name.text_color = 0, 0, 0,1
                self.root.ids.Name.text_color = 0, 0, 0,1
                self.root.ids.progress.value = 0
                self.root.ids.name.icon = "numeric-1-circle"
                

        def previous1(self):
                self.root.ids.slide.load_previous()
                self.root.ids.contact.text_color = 0, 0, 0,1
                self.root.ids.Contact.text_color = 0, 0, 0,1
                self.root.ids.progress1.value = 0
                self.root.ids.contact.icon = "numeric-2-circle"
                
        def submit(self):
                db = DataBase("users.txt")
                regexPd = r'^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).*$'
                if ((self.root.ids.password.text != "") and (self.root.ids.Cpass.text != "")):
                        if ((re.search (regexPd , self.root.ids.password.text)) and (self.root.ids.password.text == self.root.ids.Cpass.text) ):
                                self.root.ids.slide.load_next (mode = "next")
                                self.root.ids.submit.text_color = self.theme_cls.primary_color
                                self.root.ids.Submit.text_color = self.theme_cls.primary_color
                                self.root.ids.submit.icon = "check-decagram"
                                self.root.ids.ErrorP.text = ""
                                db.add_user(self.root.ids.email.text , self.root.ids.password.text , self.root.ids.Fname.text , 
                                       self.root.ids.Lname.text , self.root.ids.phone.text)
                        else:
                                
                                self.reset()
                                self.root.ids.ErrorP.text = "invalid password or confirmation" 
                                          
                        
                else:
                        self.root.ids.password.helper_text = "Enter your password"
                        self.root.ids.Cpass.helper_text = "confirm your password" 
        
        
        def reset(self):
                self.root.ids.email.text = ""
                self.root.ids.phone.text = ""
                self.root.ids.password.text = ""
                self.root.ids.Cpass.text = ""
      
        
       

ProfileApp().run()




