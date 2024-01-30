from kivymd.uix.card import MDCard
from kivymd.uix.behaviors.backgroundcolor_behavior import BackgroundColorBehavior
from kivy.lang.builder import Builder
from pathlib import Path

kv_file = Path(__file__).resolve().parent

Builder.load_file(f'{kv_file}/playlistandmonitor.kv')

class KartuPlaylist(MDCard, BackgroundColorBehavior):
    pass

class KartuMonitor(MDCard, BackgroundColorBehavior):
    pass