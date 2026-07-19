import os

from kivy.core.text import LabelBase
from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager


# ---------------- Widgets ----------------

from widgets.bottom_nav import BottomNav
from widgets.profile_card import ProfileCard
from widgets.app_bar import AppBar
from widgets.device_card import DeviceCard
from widgets.action_buttons import ActionButtons
from widgets.devices_section import DevicesSection
from widgets.base_card import BaseCard
from widgets.history_section import HistorySection
from widgets.history_item import HistoryItem
from widgets.persian_label import PersianLabel



# ---------------- Screens ----------------

from screens.profile import ProfileScreen
from screens.home_screen import HomeScreen



# ---------------- Font ----------------

LabelBase.register(
    name="Vazir",
    fn_regular="assets/fonts/Vazirmatn-Regular.ttf",
)



# ---------------- Config ----------------

CONFIG_PATH = "config/device.json"



class HamResanApp(MDApp):


    def build(self):

        self.theme_cls.theme_style = "Dark"



        # ---------------- Widget KV ----------------


        Builder.load_file(
            "kv/widgets/bottom_nav.kv"
        )


        Builder.load_file(
            "kv/widgets/base_card.kv"
        )


        Builder.load_file(
            "kv/widgets/profile_card.kv"
        )


        Builder.load_file(
            "kv/widgets/app_bar.kv"
        )


        Builder.load_file(
            "kv/widgets/device_card.kv"
        )


        # اضافه شد


        Builder.load_file(
            "kv/widgets/action_buttons.kv"
        )


        Builder.load_file(
            "kv/widgets/devices_section.kv"
        )


        Builder.load_file(
            "kv/widgets/history_item.kv"
        )


        Builder.load_file(
            "kv/widgets/history_section.kv"
        )



        # ---------------- Screen KV ----------------



        Builder.load_file(
            "kv/screens/home.kv"
        )


        Builder.load_file(
            "kv/screens/profile.kv"
        )



        # ---------------- Screen Manager ----------------


        sm = MDScreenManager()



        sm.add_widget(
            HomeScreen(
                name="home"
            )
        )



        sm.add_widget(
            ProfileScreen(
                name="profile"
            )
        )



        # ---------------- First Run ----------------


        if os.path.exists(CONFIG_PATH):

            sm.current = "home"

        else:

            sm.current = "profile"



        return sm



    # ---------------- Navigation ----------------


    def open_profile(self):

        self.root.current = "profile"



    def open_home(self):

        self.root.current = "home"




if __name__ == "__main__":

    HamResanApp().run()