import json
import os
import uuid

from kivymd.uix.screen import MDScreen


CONFIG_PATH = "config/device.json"


class StartScreen(MDScreen):


    def save_device(self, name):

        print("BUTTON CLICKED:", name)


        if not name.strip():

            print("EMPTY NAME")

            return


        os.makedirs(
            "config",
            exist_ok=True
        )


        data = {

            "device_name": name,

            "device_id": str(
                uuid.uuid4()
            ),

            "ip": "0.0.0.0"

        }


        with open(
            CONFIG_PATH,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                ensure_ascii=False,
                indent=4
            )


        print("DEVICE SAVED")

        print(data)


        self.manager.current = "home"