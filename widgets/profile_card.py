import json
import os

from kivymd.uix.card import MDCard


CONFIG_PATH = "config/device.json"


class ProfileCard(MDCard):

    device_name = "دستگاه من"


    def on_kv_post(self, base_widget):

        self.load_device_name()



    def load_device_name(self):

        if os.path.exists(CONFIG_PATH):

            try:

                with open(
                    CONFIG_PATH,
                    "r",
                    encoding="utf-8"
                ) as f:

                    data = json.load(f)


                self.device_name = data.get(
                    "name",
                    "دستگاه من"
                )


            except Exception:

                self.device_name = "دستگاه من"


        else:

            self.device_name = "دستگاه من"