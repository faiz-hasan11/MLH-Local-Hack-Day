from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
import requests
Builder.load_string("""
<Test>:
    l:lbl
    Label:
        id:lbl
        pos:350,300
        text:"Generate Quote"
        font_size:"30dp"
    Button:
        size:170,75
        pos:300,150
        text:"Click to Get Quote"
        on_press:root.change_quote()
""")


class Test(Widget):
    def change_quote(self):
        try:
            api = "http://api.quotable.io/random"
            quote = requests.get(api).json()
            quote = quote['content']
            self.l.text = quote
        except:
            self.l.text = "Try Again"


class FirstApp(App):
    def build(self):
        return Test()


FirstApp().run()
