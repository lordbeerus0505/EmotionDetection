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
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class SendMail(Screen):
    def disconnect(self):
        Window.size=(500,500)
        
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'screen3'
    def submit(self,content,subject,email):
        print(str(content))
        if email.find("@")==-1 or email.find('.com')==-1 and email.find('.edu.in')==-1:
            print("Wrong mail ID")
            box1=BoxLayout(orientation='vertical',padding=(10))
            box1.add_widget(Label(text="Incorrect Email ID!"))
            btn1=Button(text='Close')
            box1.add_widget(btn1)
            popup1=Popup(title='Please Correct the Email ID',title_size=(30),title_align='center',content=box1,size_hint=(None,None),size=(400,200),auto_dismiss=False)
            btn1.bind(on_press=popup1.dismiss)
            popup1.open()
            return
        obj=Mail()
        obj.send_mail("abhiram.natarajan@gmail.com",email,subject,content)
        box=BoxLayout(orientation='vertical',padding=(10))
        box.add_widget(Label(text="Mail Sent Successfully!"))
        btn1=Button(text='Close')
        box.add_widget(btn1)
        popup=Popup(title='Mail Sent',title_size=(30),title_align='center',content=box,size_hint=(None,None),size=(400,200),auto_dismiss=False)
        btn1.bind(on_press=popup.dismiss)
        popup.open()
        # input()
        # Y=Label(text="Sent mail successfully",font_size=24)
        # self.output.add_widget(Y)
