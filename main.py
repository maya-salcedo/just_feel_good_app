from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.animation import Animation
from hoverable import HoverBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
import json, glob
from pathlib import Path
import random
from datetime import datetime

Builder.load_file('design.kv') #To connect to .kv file

class LoginScreen(Screen):#This object inherent from Screen obj, Screen is the parent, LoginScreen is a child
    def sign_up(self):
        self.manager.current = "sign_up_screen" #when the sign up button is pressed, it goes to
        # sign_up_screen
    def login(self, uname, pword):
        with open("users.JSON") as file:
            users = json.load(file)
        if uname in users and users[uname]['password'] == pword:
            self.manager.current = "login_success_screen"
        else:
            anim = Animation(color= (0.6, 0.7, 0.1, 1))
            anim.start(self.ids.login_wrong)
            self.ids.login_wrong.text = "Wrong username or password!"





class SignUpScreen(Screen):
    def add_user(self, uname, pword):
        with open("users.JSON") as file:
            users = json.load(file)
        users[uname] = {"username": uname, "password": pword,
                        "created": datetime.now().strftime("%Y-%m-%d %H-%M-%S")}
        with open("users.JSON", "w") as file:
            json.dump(users, file) #will add the new user to the json file
        self.manager.current = "sign_up_screen_success" #when the submit button is pressed,
        # it directs to this screen in <RootWidget>

class SignUpScreenSuccess(Screen):
    def go_to_login(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"



class LoginScreenSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"

    def get_quote(self, feel):
        feel = feel.lower()
        available_feelings = glob.glob("quotes/*txt")
        available_feelings = [Path(filename).stem for filename in available_feelings] #to have
        # the available feeling in a list
        if feel in available_feelings:
            with open(f"quotes/{feel}.txt", encoding="utf-8") as file:
                quotes = file.readlines()
            self.ids.quote.text = random.choice(quotes)
        else:
            self.ids.quote.text = "Please try another feeling"


class ImageButton(ButtonBehavior, HoverBehavior, Image):
    #this class behaves like these 3 objects
    pass




#every rule has to have a class
class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget() #obj, not class

if __name__ == "__main__":
    MainApp().run()



