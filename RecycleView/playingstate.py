from kivy.event import EventDispatcher
from kivy.properties import BooleanProperty, StringProperty


class PlayingState(EventDispatcher):
    played = BooleanProperty(False)
    iconPlayed = StringProperty('play')
    
class RepeatState(EventDispatcher):
    iconRepeat = StringProperty('repeat-off')