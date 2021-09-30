from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.picker import MDDatePicker, MDTimePicker




class ProfileApp (MDApp):

        def build(self):
                self.theme_cls.theme_style = "Light"
                self.theme_cls.primary_palette = "Green"
                
                return Builder.load_file('reservekv.kv')

        def next(self):
                self.root.ids.slide.load_next (mode = "next")
                self.root.ids.Date.text_color = self.theme_cls.primary_color
                self.root.ids.progress.value = 100
                self.root.ids.date.text_color = self.theme_cls.primary_color
                self.root.ids.date.icon = "check-decagram"

        def next1(self):
                self.root.ids.slide.load_next (mode = "next")
                self.root.ids.Time.text_color = self.theme_cls.primary_color
                self.root.ids.progress1.value = 100
                self.root.ids.time.text_color = self.theme_cls.primary_color
                self.root.ids.time.icon = "check-decagram"

        def previous(self):
                self.root.ids.slide.load_previous()
                self.root.ids.date.text_color = 0, 0, 0, 1
                self.root.ids.Date.text_color = 0, 0, 0, 1
                self.root.ids.progress.value = 0
                self.root.ids.date.icon = "calendar"

        def previous1(self):
                self.root.ids.slide.load_previous()
                self.root.ids.time.text_color = 0, 0, 0, 1
                self.root.ids.Time.text_color = 0, 0, 0, 1
                self.root.ids.progress1.value = 0
                self.root.ids.time.icon = "clock"
                
        def on_save (self, instance , value , date_range):
               self.root.ids.date_label.text = str(value)
               
               
               

        def on_cancel (self, instance , value):
               self.root.ids.date_label.text = "you haven't selected a date"
               

        def show_date_picker(self):
                date_dialog = MDDatePicker()
                date_dialog.bind(on_save = self.on_save, on_cancel = self.on_cancel)
                date_dialog.open()

        def get_time (self, instance , time):
                self.root.ids.time_label.text = str(time)
                
                
                
        def on_cancel1 (self , instance , time):
                self.root.ids.time_label.text = "you haven't selected a time"
                
        def show_time_picker (self):
                time_dialog = MDTimePicker()
                time_dialog.bind(time = self.get_time , on_cancel = self.on_cancel1)
                time_dialog.open()

ProfileApp().run()
