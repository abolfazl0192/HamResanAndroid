import json
import os

from kivy.properties import StringProperty
from widgets.base_card import BaseCard


CONFIG_PATH = "config/device.json"


class DeviceCard(BaseCard):

    device_name = StringProperty("نام دستگاه")

    device_ip = StringProperty("بدون IP")


    def on_kv_post(self, base_widget):

        self.load_device()



    def load_device(self):

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
                    "نام دستگاه"
                )


                self.device_ip = data.get(
                    "ip",
                    "بدون IP"
                )


            except Exception as e:

                print("JSON ERROR:", e)