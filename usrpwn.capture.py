from kivy.app import App
from kivy.lang import Builder


kv = Builder.load_string("""
Screen:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'We Be Jammin'
        Button:
            text: 'Exit'
            on_release: app.stop()
""")


class SettingScreen(App):

    def build(self):
        return kv


if __name__ == "__main__":
    SettingScreen().run()


