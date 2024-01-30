from kivy.event import EventDispatcher
from kivy.properties import ColorProperty

class KedipanBilah(EventDispatcher):
    
    bilahnormal1 = ColorProperty("#D9D9D9")
    bilahnormal2 = ColorProperty("#D9D9D9")
    bilahnormal3 = ColorProperty("#D9D9D9")
    bilahnormal4 = ColorProperty("#D9D9D9")
    bilahnormal5 = ColorProperty("#D9D9D9")
    bilahnormal6 = ColorProperty("#D9D9D9")
    bilahnormal7 = ColorProperty("#D9D9D9")
    
    bilahpeking1 = ColorProperty("#D9D9D9")
    bilahpeking2 = ColorProperty("#D9D9D9")
    bilahpeking3 = ColorProperty("#D9D9D9")
    bilahpeking4 = ColorProperty("#D9D9D9")
    bilahpeking5 = ColorProperty("#D9D9D9")
    bilahpeking6 = ColorProperty("#D9D9D9")
    bilahpeking7 = ColorProperty("#D9D9D9")
    
    bilahkenong1 = ColorProperty("#D9D9D9")
    bilahkenong2 = ColorProperty("#D9D9D9")
    bilahkenong3 = ColorProperty("#D9D9D9")
    bilahkenong5 = ColorProperty("#D9D9D9")
    bilahkenong6 = ColorProperty("#D9D9D9")
    bilahkenong7 = ColorProperty("#D9D9D9")
    
    bilahgong = ColorProperty("#D9D9D9")
    
    
    
    def kedipnormal(self, bilah):
        if bilah == "1":
            self.bilahnormal1 = "#EDFF7D"
        elif bilah == "2":
            self.bilahnormal2 = "#EDFF7D"
        elif bilah == "3":
            self.bilahnormal3 = "#EDFF7D"
        elif bilah == "4":
            self.bilahnormal4 = "#EDFF7D"
        elif bilah == "5":
            self.bilahnormal5 = "#EDFF7D"
        elif bilah == "6":
            self.bilahnormal6 = "#EDFF7D"
        elif bilah == "7":
            self.bilahnormal7 = "#EDFF7D"
        else:
            pass
                
        
        
    def kedippeking(self, bilah):
        
        if bilah == "1":
            self.bilahpeking1 = "#EDFF7D"
        elif bilah == "2":
            self.bilahpeking2 = "#EDFF7D"
        elif bilah == "3":
            self.bilahpeking3 = "#EDFF7D"
        elif bilah == "4":
            self.bilahpeking4 = "#EDFF7D"
        elif bilah == "5":
            self.bilahpeking5 = "#EDFF7D"
        elif bilah == "6":
            self.bilahpeking6 = "#EDFF7D"
        elif bilah == "7":
            self.bilahpeking7 = "#EDFF7D"
        else:
            pass
        
    def kedipkenong(self, bilah):
        
        if bilah == "1":
            self.bilahkenong1 = "#EDFF7D"
        elif bilah == "2":
            self.bilahkenong2 = "#EDFF7D"
        elif bilah == "3":
            self.bilahkenong3 = "#EDFF7D"
        elif bilah == "4":
            self.bilahkenong4 = "#EDFF7D"
        elif bilah == "5":
            self.bilahkenong5 = "#EDFF7D"
        elif bilah == "6":
            self.bilahkenong6 = "#EDFF7D"
        elif bilah == "7":
            self.bilahkenong7 = "#EDFF7D"
        else:
            pass
        
    def kedipgong(self, bilah):
        if bilah == "1":
            self.bilahgong = "#EDFF7D"
        else:
            pass
            
            
    def offNormal(self):
        self.bilahnormal1 = "#D9D9D9"
        self.bilahnormal2 = "#D9D9D9"
        self.bilahnormal3 = "#D9D9D9"
        self.bilahnormal4 = "#D9D9D9"
        self.bilahnormal5 = "#D9D9D9"
        self.bilahnormal6 = "#D9D9D9"
        self.bilahnormal7 = "#D9D9D9"
        
    def offPeking(self):
        self.bilahpeking1 = "#D9D9D9"
        self.bilahpeking2 = "#D9D9D9"
        self.bilahpeking3 = "#D9D9D9"
        self.bilahpeking4 = "#D9D9D9"
        self.bilahpeking5 = "#D9D9D9"
        self.bilahpeking6 = "#D9D9D9"
        self.bilahpeking7 = "#D9D9D9"
        
    def offKenong(self):
        self.bilahkenong1 = "#D9D9D9"
        self.bilahkenong2 = "#D9D9D9"
        self.bilahkenong3 = "#D9D9D9"
        self.bilahkenong4 = "#D9D9D9"
        self.bilahkenong5 = "#D9D9D9"
        self.bilahkenong6 = "#D9D9D9"
        self.bilahkenong7 = "#D9D9D9"
        
    def offGong(self):
        self.bilahgong = "#D9D9D9"
            
        
        
    
        