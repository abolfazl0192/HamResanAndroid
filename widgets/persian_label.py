from kivymd.uix.label import MDLabel
from kivy.properties import StringProperty

from utils.text import fa


class PersianLabel(MDLabel):

    fa_text = StringProperty("")

    def on_fa_text(self, instance, value):
        self.text = fa(value)