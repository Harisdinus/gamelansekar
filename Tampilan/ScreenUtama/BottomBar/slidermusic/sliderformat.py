from kivy.event import EventDispatcher
from kivy.properties import NumericProperty, StringProperty
from kivymd.app import MDApp
from time import sleep


class SliderFormat(EventDispatcher):
    indexMusic = NumericProperty(0)
    endMusic = NumericProperty(0)

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.touchdown = False
    
    def sliderIndex(self, value):
        arduino = MDApp.get_running_app().arduino
        self.touchdown = False
        if self.indexMusic != value:
            print(int(value))
            arduino.arduino.reset_input_buffer()
            arduino.perintah(f"index:{value}:")
        self.indexMusic = value
        
    def sliderDown(self):
        self.touchdown = True       
      

    def sliderIncr(self, value):
        if self.touchdown != True:
            self.indexMusic = int(value)
        