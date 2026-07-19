import json
import os

from kivymd.uix.screen import MDScreen


CONFIG_PATH = "config/device.json"


class ProfileScreen(MDScreen):


    def save_profile(self, name):

        if not name.strip():
            return


        os.makedirs(
            "config",
            exist_ok=True
        )


        data = {
            "name": name,
            "ip": "192.168.1.101"
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


        print("PROFILE SAVED:", data)


        self.manager.current = "home"