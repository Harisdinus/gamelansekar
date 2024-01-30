from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from pathlib import Path

kv_file = Path(__file__).resolve().parent

Builder.load_file(f'{kv_file}/bottombar.kv')

class BottomBar(MDRelativeLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = MDApp.get_running_app()
        self.rv = MDApp.get_running_app().rv
        
    def next(self):
        self.rv.next()
        
    def previous(self):
        self.rv.previous()
        
    def play(self):
        self.rv.play()
        
    def repeatState(self):
        repeatstate = MDApp.get_running_app().repeatState
        if repeatstate.iconRepeat == 'repeat-off':
            repeatstate.iconRepeat = 'repeat'
        elif repeatstate.iconRepeat == 'repeat':
            repeatstate.iconRepeat = 'repeat-once'
        elif repeatstate.iconRepeat == 'repeat-once':
            repeatstate.iconRepeat = 'repeat-off'
