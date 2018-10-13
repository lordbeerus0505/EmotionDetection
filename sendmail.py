# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 00:10:36 2018

@author: admin
"""

from Mails import Mail
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Label
from kivy.uix.screenmanager import Screen, SlideTransition

class SendMail(Screen):
    def disconnect(self):
        Window.size=(500,500)
        
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'screen3'
    def submit(self,content,subject,email):
        print(str(content))
        obj=Mail()
        obj.send_mail("abhiram.natarajan@gmai.com",email,subject,content)
        # input()
        # Y=Label(text="Sent mail successfully",font_size=24)
        # self.output.add_widget(Y)
