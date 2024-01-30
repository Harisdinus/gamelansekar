from kivymd.uix.screen import MDScreen
from kivy.lang.builder import Builder
from pathlib import Path

kv_file = Path(__file__).resolve().parent

Builder.load_file(f"{kv_file}/screenkedua.kv")

class ScreenKedua(MDScreen):
    pass