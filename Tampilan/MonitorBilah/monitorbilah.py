from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.behaviors.backgroundcolor_behavior import BackgroundColorBehavior
from kivy.lang.builder import Builder
from pathlib import Path

kv_file = Path(__file__).resolve().parent

Builder.load_file(f'{kv_file}/monitorbilah.kv')

class MonitorBilah(MDBoxLayout):
    pass

class Normal(MDCard, BackgroundColorBehavior):
    pass

class Peking(MDCard, BackgroundColorBehavior):
    pass

class Kenong(MDCard, BackgroundColorBehavior):
    pass

class Gong(MDCard, BackgroundColorBehavior):
    pass

class NormalMonitor(MDCard, BackgroundColorBehavior):
    pass

class PekingMonitor(MDCard, BackgroundColorBehavior):
    pass

class KenongMonitor(MDCard, BackgroundColorBehavior):
    pass

class GongMonitor(MDCard, BackgroundColorBehavior):
    pass