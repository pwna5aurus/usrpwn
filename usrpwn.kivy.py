from typing import Text
from kivy.core.window import Window
import kivy
from kivy.uix.widget import Widget
import os

kivy.require('2.1.0')  # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout



class HomePage(BoxLayout):

    def __init__(self, **kwargs):
        super(HomePage, self).__init__(**kwargs)

        butt1 = Button(text='Jammers')
        butt1.bind(on_press =lambda x:self.jam())
        butt2 = Button(text='Capture')
        butt2.bind(on_press =lambda x:self.capture())
        butt3 = Button(text='Replay')
        butt3.bind(on_press =lambda x:self.replay())
        butt4 = Button(text='Scan')
        butt4.bind(on_press =lambda x:self.scan())
        butt5 = Button(text='Tuners')
        butt5.bind(on_press =lambda x:self.tuners())
        butt6 = Button(text='Exit')
        butt6.bind(on_release=lambda x:exit())

        self.add_widget(butt1)
        self.add_widget(butt2)
        self.add_widget(butt3)
        self.add_widget(butt4)
        self.add_widget(butt5)
        self.add_widget(butt6)

    def jam(self):
        print("We be jammin'")
        cwd = os.getcwd()
        from subprocess import Popen, PIPE
        process = Popen(['python3', f'{cwd}/usrpwn.jam.py'], stdout=PIPE, stderr=PIPE)

    def capture(self):
        print("We be cappin'")
        cwd = os.getcwd()
        from subprocess import Popen, PIPE
        process = Popen(['python3', f'{cwd}/usrpwn.capture.py'], stdout=PIPE, stderr=PIPE)
    def replay(self):
        print("We be replayin'")
        cwd = os.getcwd()
        from subprocess import Popen, PIPE
        process = Popen(['python3', f'{cwd}/usrpwn.replay.py'], stdout=PIPE, stderr=PIPE)
    def scan(self):
        print("We be scannin'")
        cwd = os.getcwd()
        from subprocess import Popen, PIPE
        process = Popen(['python3', f'{cwd}/usrpwn.scan.py'], stdout=PIPE, stderr=PIPE)
    def tuners(self):
        print("We be tunin'")
        cwd = os.getcwd()
        from subprocess import Popen, PIPE
        process = Popen(['python3', f'{cwd}/usrpwn.tune.py'], stdout=PIPE, stderr=PIPE)
class MyApp(App):
    def build(self):
        return HomePage()


if __name__ == '__main__':
    Window.maximize()
    MyApp().run()
