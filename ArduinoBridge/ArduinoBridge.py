from serial import Serial
from serial.tools.list_ports import comports
from threading import Thread as TD
from queue import Queue
from time import sleep
from kivy.event import EventDispatcher
from kivymd.app import MDApp
from kivy.clock import mainthread
    


class ArduinoBridge(EventDispatcher):
    
    def __init__(self):
        self.antrian = Queue()
        self.arduino = Serial()
        
        
    
    def loopinganUtama(self):
        statusarduino = MDApp.get_running_app().koneksiarduino
        
        while True:
            self.cariKoneksi()
            
            while True:
                self.pengiriman()
                
                try:
                    self.serMessage = self.penerimaan()
                    print(self.serMessage)
                    self.logic(self.serMessage)
                except:
                    break
                
            sleep(1)
            print('putus')
            statusarduino.warna = '#F39090'
            statusarduino.pesan = 'Arduino\nNot Available'
                
                
    def cariKoneksi(self):
        self.com = comports()
        self.listcom = []
        
        statusarduino = MDApp.get_running_app().koneksiarduino
        
        
        for i in self.com:
            self.port = str(i).split(' ')[0]
            self.listcom.append(self.port)    
            
            
        for i in self.listcom:
            print(f"nyoba koneksi terhadap {i}")
            try:
                self.arduino.baudrate = 9600
                self.arduino.port = i
                self.arduino.timeout = 2
                self.arduino.open()
                self.serMessage = self.arduino.readline().decode().strip()
                if self.serMessage == 'ArduinoDevices':
                    print(self.serMessage)
                    statusarduino.warna = '#A4F390'
                    statusarduino.pesan = 'Arduino\nAvailable'
                    break
                else:
                    print('bukan')
                    statusarduino.warna = '#F39090'
                    statusarduino.pesan = 'Arduino\nNot Available'
                    self.arduino.close()
            except:
                self.arduino.close()
        
            
    def pengiriman(self):
        while self.antrian.empty() != True:
                try:
                    data = self.antrian.get()
                    self.arduino.write(data.encode())
                except:
                    print('putus')
                    break
                while True:
                    try:
                        message = self.arduino.readline().decode().strip()
                    except:
                        self.matiinmonitor()
                        break
                    finally:
                        if message == 'done' or self.antrian.empty():
                            print(message)
                            self.arduino.flush()
                            break
                    
    def penerimaan(self):
        return self.arduino.readline().decode().strip()
        
    def perintah(self, isi):
        self.antrian.put(isi)
    
    @mainthread    
    def logic(self, isi):
        
        pesan = str(isi).split(':')
        monitor = MDApp.get_running_app().monitor
        index = MDApp.get_running_app().slidervalue
        
        if pesan[0] == "finish":
            rv = MDApp.get_running_app().rv
            repeatstate = MDApp.get_running_app().repeatState
            print('masuk finish')
            if repeatstate.iconRepeat == 'repeat-off':
                print('masuk stop')
                rv.stop()
            elif repeatstate.iconRepeat == 'repeat':
                print('masuk ulang')
                rv.next()
            elif repeatstate.iconRepeat == 'repeat-once':
                rv.repeat()
            rv = None
        try:    
            kedipan = pesan[2]
            normal = kedipan[0]
            peking = kedipan[1]
            kenong = kedipan[2]
            gong = kedipan[3]
            TD(target=lambda: monitor.kedipnormal(normal), daemon=True).start()
            TD(target=lambda: monitor.kedippeking(peking), daemon=True).start()
            TD(target=lambda: monitor.kedipkenong(kenong), daemon=True).start()
            TD(target=lambda: monitor.kedipgong(gong), daemon=True).start()
            index.sliderIncr(pesan[4])
        except:
            pass
        
        if pesan[0] == "cal":
            try:
                mcal = pesan[1]
                normal = mcal[0]
                peking = mcal[1]
                kenong = mcal[2]
                gong = mcal[3]
                TD(target=lambda: monitor.kedipnormal(normal), daemon=True).start()
                TD(target=lambda: monitor.kedippeking(peking), daemon=True).start()
                TD(target=lambda: monitor.kedipkenong(kenong), daemon=True).start()
                TD(target=lambda: monitor.kedipgong(gong), daemon=True).start()
            except:
                pass
                
        
        if pesan[0] == "off":
            TD(target=lambda: monitor.offNormal(), daemon=True).start()
            TD(target=lambda: monitor.offPeking(), daemon=True).start()
            TD(target=lambda: monitor.offKenong(), daemon=True).start()
            TD(target=lambda: monitor.offGong(), daemon=True).start()
        
        
            
    def exit(self):
        print("keluar dari program")
        try:
            self.arduino.close()
            self.arduino.open()
            self.arduino.close()     
        except:
            pass   
        
    def modePlayer(self):
        self.perintah("player:\n")
        
    def modeKalibrasi(self):
        self.perintah("kalibrasi:\n")
        
    def matiinmonitor(self):
        monitor = MDApp.get_running_app().monitor
        TD(target=lambda: monitor.offNormal(), daemon=True).start()
        TD(target=lambda: monitor.offPeking(), daemon=True).start()
        TD(target=lambda: monitor.offKenong(), daemon=True).start()
        TD(target=lambda: monitor.offGong(), daemon=True).start()
        
        
    def run(self):
        TD(target=lambda: self.loopinganUtama(), daemon=True).start()
    
