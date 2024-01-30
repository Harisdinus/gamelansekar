from kivymd.uix.screen import MDScreen
from kivy.lang.builder import Builder
from pathlib import Path

kv_file = Path(__file__).resolve().parent

Builder.load_file(f'{kv_file}/splashscreen.kv')

class BlankScreen(MDScreen):
    pass

class SekarLogoScreen(MDScreen):
    pass

class UdinusLogoScreen(MDScreen):
    pass