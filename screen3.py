# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 23:17:15 2018

@author: admin
"""
from Mails import Mail
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.uix.label import Label

class Screen3(Screen):
    def disconnect(self):
        Window.size=(500,500)
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'connected'
    def send(self):
        Window.size=(500,650)
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'sendmail'
    def search(self):
        Window.size=(500,650)
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'search'
    def latest(self):
        Window.size=(500,650)

        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'latest' 
        y=Label(text=str("Testing"),font_size=24);
        # self.output.add_widget(y);
        