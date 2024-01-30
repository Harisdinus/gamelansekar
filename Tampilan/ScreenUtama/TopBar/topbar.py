from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.lang.builder import Builder
from kivymd.uix.behaviors.backgroundcolor_behavior import BackgroundColorBehavior
from kivymd.uix.card import MDCard
from pathlib import Path

kv_file = Path(__file__).resolve().parent

Builder.load_file(f"{kv_file}/topbar.kv")

class TopBar(MDRelativeLayout):
    pass

class StatusArduino(MDCard):
    pass