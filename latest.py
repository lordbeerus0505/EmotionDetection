# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 22:12:44 2018

@author: admin
"""

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.uix.button import Label
from Mails import Mail
#from kivy.uix.layout import Layout
class Latest(Screen):
    #self.output=Label(text="Output");
    def submit(self):
        obj=Mail()
        ip=obj.LatestMails()
        
        print(ip)
        # ip="Hello \n How are you"
        self.remove_widget(self.output.children[0])
        y=Label(text=str(ip),font_size=24)
        self.output.add_widget(y)
        
    def disconnect(self):
        Window.size=(500,500)
        #self.remove_widget(self.widget[2]);
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'screen3'