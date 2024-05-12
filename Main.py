from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard

Kiwy= """
MDScreen:
  name: "main_screen"
  MDLabel:
    text: "Hello Tadashi"
    pos_hint: {"center_x": 0.5, "center_y": 0.5}
"""

class MyApp(MDApp):
  def build(self):
    screen= Builder.load_string(Kiwy)
    return screen

MyApp().run()
