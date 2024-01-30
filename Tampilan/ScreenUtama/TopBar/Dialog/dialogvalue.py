from kivy.event import EventDispatcher
from kivy.properties import NumericProperty

class DialogValue(EventDispatcher):
    slider1 = NumericProperty(2)
    slider2 = NumericProperty(90)
    slider3 = NumericProperty(1)