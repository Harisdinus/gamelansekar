from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang.builder import Builder
from kivy.properties import NumericProperty
from kivymd.app import MDApp
from pathlib import Path

kv_file = Path(__file__).resolve().parent

Builder.load_file(f'{kv_file}/contentDialog.kv')

class ContentDialog(MDBoxLayout):
    
    def pencet1(self, value):
        arduino = MDApp.get_running_app().arduino
        dval = MDApp.get_running_app().dialogValue
        nilai = int(value)
        kiriman = ""
        if dval.slider1 != value:
            print(int(value)/2)
            match nilai:
                case 1:
                    kiriman = "750"
                case 2:
                    kiriman = "500"
                case 3:
                    kiriman = "350"
                
            arduino.perintah(f"kecepatan:{kiriman}:")
        dval.slider1 = value
        
    def pencet2(self, value):
        arduino = MDApp.get_running_app().arduino
        dval = MDApp.get_running_app().dialogValue
        if dval.slider2 != value:
            print(int(value))
            arduino.perintah(f"touchtime:{int(value)}:")
        dval.slider2 = value
        
    def pencet3(self, value):
        dval = MDApp.get_running_app().dialogValue
        if dval.slider3 != value:
            print(int(value))
        dval.slider3 = value