from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from pathlib import Path

kv_file = Path(__file__).resolve().parent

Builder.load_file(f'{kv_file}/bottombar2.kv')

class BottomBar2(MDRelativeLayout):
    def reseter(self):
        kondisitombol = MDApp.get_running_app().kondisitombol
        # Normal
        kondisitombol.tn1 = False
        kondisitombol.tn2 = False
        kondisitombol.tn3 = False
        kondisitombol.tn4 = False
        kondisitombol.tn5 = False
        kondisitombol.tn6 = False
        kondisitombol.tn7 = False

        kondisitombol.bcn1 = '#D9D9D9'
        kondisitombol.bcn2 = '#D9D9D9'
        kondisitombol.bcn3 = '#D9D9D9'
        kondisitombol.bcn4 = '#D9D9D9'
        kondisitombol.bcn5 = '#D9D9D9'
        kondisitombol.bcn6 = '#D9D9D9'
        kondisitombol.bcn7 = '#D9D9D9'

        # Peking
        kondisitombol.tp1 = False
        kondisitombol.tp2 = False
        kondisitombol.tp3 = False
        kondisitombol.tp4 = False
        kondisitombol.tp5 = False
        kondisitombol.tp6 = False
        kondisitombol.tp7 = False

        kondisitombol.bcp1 = '#D9D9D9'
        kondisitombol.bcp2 = '#D9D9D9'
        kondisitombol.bcp3 = '#D9D9D9'
        kondisitombol.bcp4 = '#D9D9D9'
        kondisitombol.bcp5 = '#D9D9D9'
        kondisitombol.bcp6 = '#D9D9D9'
        kondisitombol.bcp7 = '#D9D9D9'

        # Kenong
        kondisitombol.tk1 = False
        kondisitombol.tk2 = False
        kondisitombol.tk3 = False
        kondisitombol.tk5 = False
        kondisitombol.tk6 = False
        kondisitombol.tk7 = False
        
        kondisitombol.bck1 = '#D9D9D9'
        kondisitombol.bck2 = '#D9D9D9'
        kondisitombol.bck3 = '#D9D9D9'
        kondisitombol.bck5 = '#D9D9D9'
        kondisitombol.bck6 = '#D9D9D9'
        kondisitombol.bck7 = '#D9D9D9'
        
        # Gong
        kondisitombol.tg = False
        kondisitombol.bcg = '#D9D9D9'
        
        arduino = MDApp.get_running_app().arduino
        arduino.perintah("reseter:\n")