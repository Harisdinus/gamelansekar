from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.behaviors.backgroundcolor_behavior import BackgroundColorBehavior
from kivy.lang.builder import Builder
from kivy.properties import BooleanProperty, ColorProperty
from kivy.event import EventDispatcher
from pathlib import Path

kv_file = Path(__file__).resolve().parent

Builder.load_file(f'{kv_file}/kartukalibrasi.kv')

class KartuKalibrasi(MDCard, BackgroundColorBehavior):
    pass

class IsiKalibrasi(MDBoxLayout):
    pass

class NormalKalibrasi(MDCard, BackgroundColorBehavior):
       
    
    def bilah1(self):
        kondisitombol = MDApp.get_running_app().kondisitombol
        if kondisitombol.tn1 == False:
            self.switch()
            kondisitombol.tn1 = True
            kondisitombol.bcn1 = '#AEAEAE'
        else:
            kondisitombol.tn1 = False
            kondisitombol.bcn1 = '#D9D9D9'
        
        arduino = MDApp.get_running_app().arduino
        arduino.perintah("normal1:\n")

    def bilah2(self):
        kondisitombol = MDApp.get_running_app().kondisitombol
        if kondisitombol.tn2 == False:
            self.switch()
            kondisitombol.tn2 = True
            kondisitombol.bcn2 = '#AEAEAE'
        else:
            kondisitombol.tn2 = False
            kondisitombol.bcn2 = '#D9D9D9'
        
        arduino = MDApp.get_running_app().arduino
        arduino.perintah("normal2:\n")

    def bilah3(self):
        kondisitombol = MDApp.get_running_app().kondisitombol
        if kondisitombol.tn3 == False:
            self.switch()
            kondisitombol.tn3 = True
            kondisitombol.bcn3 = '#AEAEAE'
        else:
            kondisitombol.tn3 = False
            kondisitombol.bcn3 = '#D9D9D9'
        
        arduino = MDApp.get_running_app().arduino
        arduino.perintah("normal3:\n")
        
    def bilah4(self):
        kondisitombol = MDApp.get_running_app().kondisitombol
        if kondisitombol.tn4 == False:
            self.switch()
            kondisitombol.tn4 = True
            kondisitombol.bcn4 = '#AEAEAE'
        else:
            kondisitombol.tn4 = False
            kondisitombol.bcn4 = '#D9D9D9'
        arduino = MDApp.get_running_app().arduino
        arduino.perintah("normal4:\n")

    def bilah5(self):
        kondisitombol = MDApp.get_running_app().kondisitombol
        if kondisitombol.tn5 == False:
            self.switch()
            kondisitombol.tn5 = True
            kondisitombol.bcn5 = '#AEAEAE'
        else:
            kondisitombol.tn5 = False
            kondisitombol.bcn5 = '#D9D9D9'
        
        arduino = MDApp.get_running_app().arduino
        arduino.perintah("normal5:\n")

    def bilah6(self):
        kondisitombol = MDApp.get_running_app().kondisitombol
        if kondisitombol.tn6 == False:
            self.switch()
            kondisitombol.tn6 = True
            kondisitombol.bcn6 = '#AEAEAE'
        else:
            kondisitombol.tn6 = False
            kondisitombol.bcn6 = '#D9D9D9'
        
        arduino = MDApp.get_running_app().arduino
        arduino.perintah("normal6:\n")

    def bilah7(self):
        kondisitombol = MDApp.get_running_app().kondisitombol
        if kondisitombol.tn7 == False:
            self.switch()
            kondisitombol.tn7 = True
            kondisitombol.bcn7 = '#AEAEAE'
        else:
            kondisitombol.tn7 = False
            kondisitombol.bcn7 = '#D9D9D9'
        
        arduino = MDApp.get_running_app().arduino
        arduino.perintah("normal7:\n")

        
    def switch(self):
        kondisitombol = MDApp.get_running_app().kondisitombol
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
        
        arduino = MDApp.get_running_app().arduino
        arduino.perintah("switchnormal:\n")
    

class PekingKalibrasi(MDCard, BackgroundColorBehavior):
       
    def bilah1(self):
        kondisitombol = MDApp.get_running_app().kondisitombol
        if kondisitombol.tp1 == False:
            self.switch()
            kondisitombol.tp1 = True
            kondisitombol.bcp1 = '#AEAEAE'
        else:
            kondisitombol.tp1 = False
            kondisitombol.bcp1 = '#D9D9D9'
        
        arduino = MDApp.get_running_app().arduino
        arduino.perintah("peking1:\n")

    def bilah2(self):
        kondisitombol = MDApp.get_running_app().kondisitombol
        if kondisitombol.tp2 == False:
            self.switch()
            kondisitombol.tp2 = True
            kondisitombol.bcp2 = '#AEAEAE'
        else:
            kondisitombol.tp2 = False
            kondisitombol.bcp2 = '#D9D9D9'
        
        arduino = MDApp.get_running_app().arduino
        arduino.perintah("peking2:\n")

    def bilah3(self):
        kondisitombol = MDApp.get_running_app().kondisitombol
        if kondisitombol.tp3 == False:
            self.switch()
            kondisitombol.tp3 = True
            kondisitombol.bcp3 = '#AEAEAE'
        else:
            kondisitombol.tp3 = False
            kondisitombol.bcp3 = '#D9D9D9'
        
        arduino = MDApp.get_running_app().arduino
        arduino.perintah("peking3:\n")

    def bilah4(self):
        kondisitombol = MDApp.get_running_app().kondisitombol
        if kondisitombol.tp4 == False:
            self.switch()
            kondisitombol.tp4 = True
            kondisitombol.bcp4 = '#AEAEAE'
        else:
            kondisitombol.tp4 = False
            kondisitombol.bcp4 = '#D9D9D9'
        
        arduino = MDApp.get_running_app().arduino
        arduino.perintah("peking4:\n")

    def bilah5(self):
        kondisitombol = MDApp.get_running_app().kondisitombol
        if kondisitombol.tp5 == False:
            self.switch()
            kondisitombol.tp5 = True
            kondisitombol.bcp5 = '#AEAEAE'
        else:
            kondisitombol.tp5 = False
            kondisitombol.bcp5 = '#D9D9D9'
        
        arduino = MDApp.get_running_app().arduino
        arduino.perintah("peking5:\n")

    def bilah6(self):
        kondisitombol = MDApp.get_running_app().kondisitombol
        if kondisitombol.tp6 == False:
            self.switch()
            kondisitombol.tp6 = True
            kondisitombol.bcp6 = '#AEAEAE'
        else:
            kondisitombol.tp6 = False
            kondisitombol.bcp6 = '#D9D9D9'
        
        arduino = MDApp.get_running_app().arduino
        arduino.perintah("peking6:\n")

    def bilah7(self):
        kondisitombol = MDApp.get_running_app().kondisitombol
        if kondisitombol.tp7 == False:
            self.switch()
            kondisitombol.tp7 = True
            kondisitombol.bcp7 = '#AEAEAE'
        else:
            kondisitombol.tp7 = False
            kondisitombol.bcp7 = '#D9D9D9'
        
        arduino = MDApp.get_running_app().arduino
        arduino.perintah("peking7:\n")

        
    def switch(self):
        kondisitombol = MDApp.get_running_app().kondisitombol
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
        kondisitombol.bcp3 = '#D9D9D9'
        kondisitombol.bcp5 = '#D9D9D9'
        kondisitombol.bcp6 = '#D9D9D9'
        kondisitombol.bcp7 = '#D9D9D9'
        
        arduino = MDApp.get_running_app().arduino
        arduino.perintah("switchpeking:\n")


class KenongKalibrasi(MDCard, BackgroundColorBehavior):
       
    
    def bilah1(self):
        kondisitombol = MDApp.get_running_app().kondisitombol
        if kondisitombol.tk1 == False:
            self.switch()
            kondisitombol.tk1 = True
            kondisitombol.bck1 = '#AEAEAE'
        else:
            kondisitombol.tk1 = False
            kondisitombol.bck1 = '#D9D9D9'
        
        arduino = MDApp.get_running_app().arduino
        arduino.perintah("kenong1:\n")

    def bilah2(self):
        kondisitombol = MDApp.get_running_app().kondisitombol
        if kondisitombol.tk2 == False:
            self.switch()
            kondisitombol.tk2 = True
            kondisitombol.bck2 = '#AEAEAE'
        else:
            kondisitombol.tk2 = False
            kondisitombol.bck2 = '#D9D9D9'
        
        arduino = MDApp.get_running_app().arduino
        arduino.perintah("kenong2:\n")

    def bilah3(self):
        kondisitombol = MDApp.get_running_app().kondisitombol
        if kondisitombol.tk3 == False:
            self.switch()
            kondisitombol.tk3 = True
            kondisitombol.bck3 = '#AEAEAE'
        else:
            kondisitombol.tk3 = False
            kondisitombol.bck3 = '#D9D9D9'
        
        arduino = MDApp.get_running_app().arduino
        arduino.perintah("kenong3:\n")

    def bilah5(self):
        kondisitombol = MDApp.get_running_app().kondisitombol
        if kondisitombol.tk5 == False:
            self.switch()
            kondisitombol.tk5 = True
            kondisitombol.bck5 = '#AEAEAE'
        else:
            kondisitombol.tk5 = False
            kondisitombol.bck5 = '#D9D9D9'
        
        arduino = MDApp.get_running_app().arduino
        arduino.perintah("kenong5:\n")

    def bilah6(self):
        kondisitombol = MDApp.get_running_app().kondisitombol
        if kondisitombol.tk6 == False:
            self.switch()
            kondisitombol.tk6 = True
            kondisitombol.bck6 = '#AEAEAE'
        else:
            kondisitombol.tk6 = False
            kondisitombol.bck6 = '#D9D9D9'
        
        arduino = MDApp.get_running_app().arduino
        arduino.perintah("kenong6:\n")

    def bilah7(self):
        kondisitombol = MDApp.get_running_app().kondisitombol
        if kondisitombol.tk7 == False:
            self.switch()
            kondisitombol.tk7 = True
            kondisitombol.bck7 = '#AEAEAE'
        else:
            kondisitombol.tk7 = False
            kondisitombol.bck7 = '#D9D9D9'
        
        arduino = MDApp.get_running_app().arduino
        arduino.perintah("kenong7:\n")

        
    def switch(self):
        kondisitombol = MDApp.get_running_app().kondisitombol
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
        
        arduino = MDApp.get_running_app().arduino
        arduino.perintah("switchkenong:\n")


class GongKalibrasi(MDCard, BackgroundColorBehavior):
    
    def gong(self):
        kondisitombol = MDApp.get_running_app().kondisitombol
        if kondisitombol.tg == False:
            kondisitombol.tg = True
            kondisitombol.bcg = '#AEAEAE'
        else:
            kondisitombol.tg = False
            kondisitombol.bcg = '#D9D9D9'
        arduino = MDApp.get_running_app().arduino
        arduino.perintah("gong:\n")
        
        

class TombolNormal(MDCard, BackgroundColorBehavior):
    pass

class TombolPeking(MDCard, BackgroundColorBehavior):
    pass

class TombolKenong(MDCard, BackgroundColorBehavior):
    pass

class TombolGong(MDCard, BackgroundColorBehavior):
    pass

class KondisiTombol(EventDispatcher):
    # Normal
    tn1 = BooleanProperty(False)
    tn2 = BooleanProperty(False)
    tn3 = BooleanProperty(False)
    tn4 = BooleanProperty(False)
    tn5 = BooleanProperty(False)
    tn6 = BooleanProperty(False)
    tn7 = BooleanProperty(False)

    bcn1 = ColorProperty('#D9D9D9')
    bcn2 = ColorProperty('#D9D9D9')
    bcn3 = ColorProperty('#D9D9D9')
    bcn4 = ColorProperty('#D9D9D9')
    bcn5 = ColorProperty('#D9D9D9')
    bcn6 = ColorProperty('#D9D9D9')
    bcn7 = ColorProperty('#D9D9D9')

    # Peking
    tp1 = BooleanProperty(False)
    tp2 = BooleanProperty(False)
    tp3 = BooleanProperty(False)
    tp4 = BooleanProperty(False)
    tp5 = BooleanProperty(False)
    tp6 = BooleanProperty(False)
    tp7 = BooleanProperty(False)

    bcp1 = ColorProperty('#D9D9D9')
    bcp2 = ColorProperty('#D9D9D9')
    bcp3 = ColorProperty('#D9D9D9')
    bcp4 = ColorProperty('#D9D9D9')
    bcp5 = ColorProperty('#D9D9D9')
    bcp6 = ColorProperty('#D9D9D9')
    bcp7 = ColorProperty('#D9D9D9')

    # Kenong
    tk1 = BooleanProperty(False)
    tk2 = BooleanProperty(False)
    tk3 = BooleanProperty(False)
    tk5 = BooleanProperty(False)
    tk6 = BooleanProperty(False)
    tk7 = BooleanProperty(False)
    
    bck1 = ColorProperty('#D9D9D9')
    bck2 = ColorProperty('#D9D9D9')
    bck3 = ColorProperty('#D9D9D9')
    bck5 = ColorProperty('#D9D9D9')
    bck6 = ColorProperty('#D9D9D9')
    bck7 = ColorProperty('#D9D9D9')
    
    # Gong
    tg = BooleanProperty(False)
    bcg = ColorProperty('#D9D9D9')
