# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 23:17:15 2018

@author: admin
"""

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.uix.button import Label
from Mails import Mail
#from kivy.uix.layout import Layout
class Search(Screen):
    #self.output=Label(text="Output");
    def submit(self,ip):
        print(ip)
        obj=Mail()
        s=obj.show_mails(ip)
        print(s)
        y=Label(text=str(s),font_size=24)
        self.output.add_widget(y)
        
    def disconnect(self):
        Window.size=(500,500)
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'screen3'