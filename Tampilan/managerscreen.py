from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.uix.screen import MDScreen
from pathlib import Path

kv_file = Path(__file__).resolve().parent

Builder.load_file(f'{kv_file}/managerscreen.kv')


class NavDrawLayout(MDScreen):
    pass
