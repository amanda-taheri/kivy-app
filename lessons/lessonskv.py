from kivy.uix.button import Button
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.app import App
from kivy.lang import Builder


class LessonsApp(App):

	def build(self):
		return Builder.load_string("""

Button:
	text:"click here to see your lesson,today we will learn Arabic"

	on_release:
		import webbrowser
		webbrowser.open('https://alaatv.com/c/5877')

		print("Today's lesson was seen")


								""")
  



LessonsApp().run()
