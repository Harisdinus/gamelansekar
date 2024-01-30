from kivy.lang.builder import Builder
from kivymd.uix.recycleview import MDRecycleView
from kivymd.uix.card import MDCard
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.behaviors.backgroundcolor_behavior import BackgroundColorBehavior
from kivy.properties import StringProperty, ColorProperty, BooleanProperty, NumericProperty
from kivymd.app import MDApp
from queue import Queue
from pathlib import Path

kv_file = Path(__file__).resolve().parent

Builder.load_file(f'{kv_file}/recycleview.kv')

class RV(MDRecycleView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = MDApp.get_running_app()
        self.app.rv = self
        self.rv = self.app.rv
        self.totalData = self.app.totalData
        
        self.arduino = self.app.arduino
        self.state = self.app.playingState
        
        self.selectedIsi = Queue()
        
    def clicked(self, index):
        if self.selectedIsi.empty() == True:
            self.pencet(index)
            self.selectedIsi.put(index)
        else:
            checkindex = self.selectedIsi.get()
            if checkindex != index:
                self.pencet(checkindex)
                self.pencet(index)
                self.selectedIsi.put(index)
            else:
                self.pencet(checkindex)
        
        
    
    def pencet(self, index):
        slidervalue = MDApp.get_running_app().slidervalue
        panjanglagu = MDApp.get_running_app().dialogValue
        if self.rv.data[index]['statuspencet'] == False:
            self.rv.data[index]['statuspencet'] = True
            self.rv.data[index]['selectcolor'] = '#B8ADAD'
            self.notasiSplit(self.rv.data[index]['notasi'])
            self.arduino.perintah(f"play:\n")
            slidervalue.endMusic = (int(len(self.rv.data[index]['notasi'])) * int(panjanglagu.slider3))-1
            
            self.state.iconPlayed = 'pause'
        else:
            self.arduino.perintah(f"stop:\n")
            self.rv.data[index]['statuspencet'] = False
            self.rv.data[index]['selectcolor'] = '#D9D9D9'
            slidervalue.endMusic = 0
            slidervalue.indexMusic = 0
            self.state.played = False
            self.state.iconPlayed = 'play'
        self.refresh_from_data()
        
            
    def next(self):
        if self.selectedIsi.empty() != True:
            checkindex = self.selectedIsi.get()
            print(f"index ke {checkindex}")
            if checkindex < self.totalData:
                self.pencet(checkindex)
                self.pencet(checkindex+1)
                self.selectedIsi.put(checkindex+1)
            else:
                self.pencet(checkindex)
                self.pencet(0)
                self.selectedIsi.put(0)
        else:
            print("gak valid")
         
    
    def previous(self):
        if self.selectedIsi.empty() != True:
            checkindex = self.selectedIsi.get()
            print(f"index ke {checkindex}")
            if checkindex > 0:
                self.pencet(checkindex)
                self.pencet(checkindex-1)
                self.selectedIsi.put(checkindex-1)
            else:
                self.selectedIsi.put(checkindex)
        else:
            print("gak valid")
        
        
    def play(self):
        if self.selectedIsi.empty() == True:
            self.pencet(0)
            self.selectedIsi.put(0)
            self.state.iconPlayed = 'pause'
            self.state.played = True
        else:
            if self.state.played == True:
                self.state.played = False
                self.arduino.perintah(f"pause:\n")
                self.state.iconPlayed = 'play'
            else:
                self.state.played = True
                self.arduino.perintah(f"lanjut:\n")
                self.state.iconPlayed = 'pause'
                
    def stop(self):
        checkindex = self.selectedIsi.get()
        self.pencet(checkindex)
        
    def repeat(self):
        checkindex = self.selectedIsi.get()
        self.pencet(checkindex)
        self.pencet(checkindex)
        self.selectedIsi.put(checkindex)
                
    def notasiSplit(self, value):
        dialog = MDApp.get_running_app().dialogValue
        value = value * int(dialog.slider3)
        
        notasi = str(value)
        splitter = 255
        iteration = int(len(notasi)/splitter)+1
        
        for i in range(iteration):
            if len(notasi) >= splitter:
                self.arduino.perintah(f"notasi:{notasi[:splitter]}:\n")
                notasi = notasi[splitter:]
            else:
                if notasi[:] != "":
                    self.arduino.perintah(f"notasi:{notasi[:]}:\n")
                    
        
            
        
            
        
        
class IsiPlaylist(MDCard, BackgroundColorBehavior, ButtonBehavior):
    selectcolor = ColorProperty('#D9D9D9') 
    statuspencet = BooleanProperty(False)
    index = NumericProperty(0)
    
            
    

        
