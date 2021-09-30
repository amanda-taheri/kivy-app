from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivy.metrics import dp
from kivymd.uix.snackbar import Snackbar
from kivy.uix.image import Image, AsyncImage
import re
import urllib.parse
import sys



class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class HippocampusApp(MDApp):
    def build(self):
        data = { 'Python' : 'language-python' }
        return Builder.load_file('title.kv')
    

    def callback(self, button):
        Snackbar(text='''
        Tel: 021-284 281 54
        WhatsApp: +98 937 376 0065
        Instagram: @Hippocampus_sabz

        ''', height="60 dp", elevation="6 dp").open()


HippocampusApp().run()
