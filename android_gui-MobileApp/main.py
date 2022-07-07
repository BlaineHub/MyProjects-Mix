from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json, glob
from datetime import datetime
from pathlib import Path
import random
from hoverable import HoverBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image



Builder.load_file('desighn.kv')

class LoginScreen(Screen):
    def forgot_pass(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'forgot_password_screen'

    def sign_up(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'sign_up_screen'
    
    def login(self, uname, pword):
            with open('users.json') as file:
                users = json.load(file)
                if uname in users and users[uname]['password'] == pword:
                    self.manager.transition.direction = 'left'
                    self.manager.current = 'login_screen_success'
                else:
                    self.ids.loginwrong.text = 'Wrong Username or Password'


class SignUpScreen(Screen):
    def add_user(self, uname, pword):
        with open('users.json') as file:
            users = json.load(file)
        users[uname] = {'username':uname,'password':pword,
        'created': datetime.now().strftime('%Y-%m-%d %H:%M:%Y')}
        
        with open('users.json', 'w') as file:
            json.dump(users,file)
        self.manager.current = 'sign_up_screen_success'

class SignUpScreenSuccess(Screen):
    def login(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'login_screen'

class LoginScreenSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'login_screen'
    def get_quote(self,feel):
        feel = feel.lower()
        available_feelings = glob.glob('quotes/*.txt')
        available_feelings = [ Path(filename).stem for filename in 
                                available_feelings]
        if feel in available_feelings:
            with open(f"quotes/{feel}.txt",encoding='utf-8') as file:
                quotes = file.readlines()
            self.ids.quote.text = random.choice(quotes)
        else:
            self.ids.quote.text = 'Opps! Pick Another Feeling'

class RootWidget(ScreenManager):
    pass

class ImageButton(HoverBehavior,ButtonBehavior,Image):
    pass

class ForgotPasswordScreen(Screen):
    def password_retrieval(self,uname):
        with open('users.json') as file:
            x=json.load(file)
            x={k.lower(): v for k, v in x.items()}
        uname = uname.lower()
        if uname in x:
            value = x[uname]['password']
            self.ids.password_show.text = value
        else:
            self.ids.password_show.text= 'Opps, No Matching Username'
        
    def login(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'login_screen'


class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()