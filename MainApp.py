from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import FadeTransition
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.clock import Clock
from Tampilan import *
from RecycleView import *
from ArduinoBridge import *
from kivy.core.window import Window
Window.size = (1080, 640)
# Window.fullscreen = 'auto '




class MainApp(MDApp):
    title = "Gamelan Sekar"
    
    dialog = None
    
    def build(self):
        
        self.kondisitombol = KondisiTombol()
        self.koneksiarduino = StateArduino()
        
        self.monitor = KedipanBilah()

        self.dialogValue = DialogValue()
        
        self.slidervalue = SliderFormat()
        
        self.arduino = ArduinoBridge()
        self.arduino.run()
        
        self.modelnotasi = LoaderModel()
        self.modelnotasi.loadXML()
        self.totalData = self.modelnotasi.maxData()
        
        self.playingState = PlayingState()
        self.repeatState = RepeatState()
        
        self.rv = None
        
        self.buatDialog()
        
        
        self.sm = ScreenManager()
        self.sm.add_widget(BlankScreen(name='blank'))
        self.sm.add_widget(SekarLogoScreen(name='logosekar'))
        self.sm.add_widget(UdinusLogoScreen(name='logoudinus'))
        self.sm.add_widget(NavDrawLayout(name='utama'))
        
        
        return self.sm
    
    def on_start(self):
        Clock.schedule_once(lambda x: self.splashswitch('blank'), 2)
        Clock.schedule_once(lambda x: self.splashswitch('logoudinus'), 4)
        Clock.schedule_once(lambda x: self.splashswitch('blank'), 6)
        Clock.schedule_once(lambda x: self.splashswitch('logosekar'), 8)
        Clock.schedule_once(lambda x: self.splashswitch('blank'), 10)
        Clock.schedule_once(lambda x: self.splashswitch('utama'), 12)
        
    
    def on_stop(self):
        self.arduino.exit()

        
    
    def buatDialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                type="custom",
                content_cls=ContentDialog(),
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        on_release=self.close_dialog
                    ),
                    MDFlatButton(
                        text="OKE",
                        on_release=self.close_dialog
                    ),
                ],
            )
    
    def bukaDialog(self):
        self.dialog.open()

    def close_dialog(self, *args):
        self.dialog.dismiss()

    def submit_dialog(self, *args):
        self.dialog.dismiss()
        
    def splashswitch(self, screenname):
        self.sm.transition = FadeTransition()
        self.sm.current = screenname


MainApp().run()
