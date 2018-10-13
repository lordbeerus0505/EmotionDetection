from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, SlideTransition

class Connected(Screen):
    def disconnect(self):
        Window.size=(500,500)
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'options'
        # self.manager.get_screen('login').resetForm()
    def stop(self):
        App.get_running_app().stop()