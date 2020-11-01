from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file('design.kv') #To connect to .kv file

class LoginScreen(Screen):#This object inherent from Screen obj
    pass

#every rule has to have a class
class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget() #obj, not class

if __name__ == "__main__":
    MainApp().run()



