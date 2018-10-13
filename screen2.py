# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 23:17:15 2018

@author: admin
"""
from scrape_amazon import Amazon
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.uix.label import Label 

class Screen2(Screen):
    def submit(self,ip):
        print(ip)
        y=Label(text=str(ip),font_size=24)
        #pass y to amazon scrape
        print(str(ip)," Y has been extracted")
        obj=Amazon()
        y=obj.input_func(str(ip))
        # preprocess
        x=''
        for a in y:
            x=x+a
        y=Label(text=str(x),font_size=16)
        self.output.add_widget(y)
    def disconnect(self):
        Window.size=(600,600)
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'connected'