from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivy.metrics import dp
from kivymd.uix.snackbar import Snackbar
from kivy.uix.image import Image , AsyncImage



title = '''
<ContentNavigationDrawer>:

    ScrollView:

        MDList:
                    
            OneLineListItem:
                text: "Main Page"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 0"

            OneLineListItem:
                text: "Profile"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 1"

            OneLineListItem:
                text: "Daily Report"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 2"
            
            OneLineListItem:
                text: "My Scores"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 3" 

         
            OneLineListItem:
                text: "Percentage of tests"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 4" 
         
            OneLineListItem:
                text: "Lessons"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 5" 
                            
            OneLineListItem:
                text: "Recieve consulting time"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 6" 
                                
            OneLineListItem:
                text: "About us"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 7" 
                    
            OneLineAvatarItem
                                          



i

  

    MDToolbar:
        md_bg_color: 75/255 , 131/255 , 108/255 , 1
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 10
        title: "Hippocampus"
        canvas:
            Rectangle:
                source: 'img/logo.jpg'
                pos: (((self.parent.size[0])/2)-30,self.pos[1])
                size: (60, 60)
                
        
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
        right_action_items: [["dots-vertical", lambda x: app.callback(x), "contact"]]

    MDNavigationLayout:
        x: toolbar.height

        ScreenManager:
            id: screen_manager
            
            Screen:
                name: "scr 0"
                
                MDLabel:
                    text: "Screen 0"
                    halign: "center"
             
                
               
            Screen:
                name: "scr 1"

                MDLabel:
                    text: "Screen 1"
                    halign: "center"

            Screen:
                name: "scr 2"

                MDLabel:
                    text: "Screen 2"
                    halign: "center"


            Screen:
                name: "scr 3"

                MDLabel:
                    text: "Screen 3"
                    halign: "center"
                    
            Screen:
                name: "scr 4"

                MDLabel:
                    text: "Screen 4"
                    halign: "center"
                    
                    
                    
            Screen:
                name: "scr 5"

                MDLabel:
                    text: "Screen 5"
                    halign: "center"
                    
                    
            Screen:
                name: "scr 6"

                MDLabel:
                    text: "Screen 6"
                    halign: "center"
                    
            
            Screen:
                name: "scr 7"

                MDLabel:
                    text: "Screen 7"
                    halign: "center"



        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
'''


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class HippocampusApp(MDApp):
    def build(self):
        return Builder.load_string(title)

    def callback(self, button):
        Snackbar(text='''
        Tel: 021-284 281 54
        WhatsApp: +98 937 376 0065
        Instagram: @Hippocampus_sabz

        ''', height="60 dp", elevation="6 dp").open()


HippocampusApp().run()
