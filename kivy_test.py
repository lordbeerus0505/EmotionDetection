from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.core.window import Window
import os
from neural_test import Neural

from connected import Connected
from Options import Options
from screen1 import Screen1
from screen2 import Screen2
from screen3 import Screen3
from sendmail import SendMail
from search import Search
from latest import Latest
from Mails import Mail

class Login(Screen):
    
    def do_login(self, loginText, passwordText):
        app = App.get_running_app()
        
        app.username = loginText
        app.password = passwordText
        if loginText=='root' and passwordText=='root':
            print("LOGGED IN")
            obj=Mail()
            obj.LatestMails()

        else:
            print("auth failed")
        
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'options'

        app.config.read(app.get_application_config())
        app.config.write()
    def validate(self):
        print(self.username)
        print(self.password)
        print("Inside validate")
        if self.username=='admin' and self.password=='admin':
            print("access granted")
            return 1
        else:
            print("HIII")

    def resetForm(self):
        self.ids['login'].text = ""
        self.ids['password'].text = ""

class LoginApp(App):
    username = StringProperty(None)
    password = StringProperty(None)
    
    def build(self):
        manager = ScreenManager()
        print("building")
        Window.size=(500,500)
        manager.add_widget(Login(name='login'))
        manager.add_widget(Connected(name='connected'))
        manager.add_widget(Options(name='options'))
        manager.add_widget(Screen1(name='screen1'))
        manager.add_widget(Screen2(name='screen2'))
        manager.add_widget(Screen3(name='screen3'))
        manager.add_widget(SendMail(name='sendmail'))
        manager.add_widget(Search(name='search'))
        manager.add_widget(Latest(name='latest'))
        #manager.add_widget(Done(name='done'))

        return manager

    def get_application_config(self):
        obj=LoginApp()
        if(not self.username):
            return super(LoginApp, self).get_application_config()

        conf_directory = self.user_data_dir + '/' + self.username

        if(not os.path.exists(conf_directory)):
            os.makedirs(conf_directory)

        return super(LoginApp, self).get_application_config(
            '%s/config.cfg' % (conf_directory)
        )
        
    


if __name__ == '__main__':
    obj=Neural()
    obj.initialise()
    LoginApp().run()