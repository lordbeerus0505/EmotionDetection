# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 23:17:15 2018

@author: admin
"""
from neural_test import Neural
from kivy.app import App
import numpy as np
import json
import time
import nltk
from kivy.core.window import Window
from nltk.stem.lancaster import LancasterStemmer
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.uix.button import Label
#from kivy.uix.layout import Layout
class Screen1(Screen):
    #self.output=Label(text="Output");
    def submit(self,ip):
        print(ip)
        # dataset    
        # training_data = []
        
        obj=Neural()
        # Y.clear_widgets()
        # obj.classify(str(ip))
        Y=obj.classify(str(ip))
        s=''
        if(type(Y)==list):
            for x in Y:
                print(x)
                s+= x[0]
            Y=Label(text="Detected emotion : "+s+"\n",font_size=24)
        else:
            Y=Label(text=Y+"\n",font_size=24)
        self.output.add_widget(Y)
        
    def disconnect(self):
        Window.size=(500,500)
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'connected'