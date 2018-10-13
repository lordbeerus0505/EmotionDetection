from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, SlideTransition

class Options(Screen):
   
    def detect(self):
        Window.size=(800,600)   
        print("Emotion Detection")
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'screen1'
        
    def scrape(self):
        Window.size=(800,600) 
        print("Scrape from Amazon")
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'screen2'
        
    def mail(self):
        Window.size=(800,600) 
        print("Connect to Gmail")
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'screen3'
        