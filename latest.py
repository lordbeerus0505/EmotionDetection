# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 22:12:44 2018

@author: admin
"""

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.uix.button import Label
#from kivy.uix.layout import Layout
class Latest(Screen):
    #self.output=Label(text="Output");
    def submit(self,ip):
        print(ip);
        y=Label(text=str(ip),font_size=24);
        self.output.add_widget(y);
        
    def disconnect(self):
        Window.size=(500,500)
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'screen3'