from bs4 import BeautifulSoup
from kivy.event import EventDispatcher
from kivy.properties import ListProperty
from pathlib import Path

list_file = Path(__file__).resolve().parent.parent

class LoaderModel(EventDispatcher):
    isi = ListProperty([])
    
    def loadXML(self):
        self.xmlfile = None
        with open(f'{list_file}/ListLagu/GendingList.xml', 'r') as f:
            self.xmlfile = f.read()
            
        self.data = BeautifulSoup(self.xmlfile, 'xml').find_all('gending')
        self.indexing = 0
        for i in self.data:
            # print(f"inisiasi index ke{self.indexing}")
            self.isi.append({'lagu': i['nama'],
                             'laras': i['namaLaras'],
                             'notasi': i.text.strip(),
                             'index': self.indexing,
                             'selectcolor': "#D9D9D9",
                             'statuspencet': False})
            self.indexing += 1
            
    def maxData(self):
        return self.indexing-1