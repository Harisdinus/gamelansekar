from kivy.event import EventDispatcher
from kivy.properties import ColorProperty, StringProperty

class StateArduino(EventDispatcher):
    warna = ColorProperty('#F39090')
    pesan = StringProperty('Arduino\nNot Available')