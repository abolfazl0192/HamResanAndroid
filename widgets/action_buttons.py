from kivy.uix.boxlayout import BoxLayout

from threading import Thread

from kivy.clock import Clock



class ActionButtons(BoxLayout):


    def scan_network(self):

        print("شروع اسکن شبکه")


        # نمایش وضعیت اسکن

        Clock.schedule_once(
            lambda dt: self.show_loading()
        )


        Thread(
            target=self._scan_thread,
            daemon=True
        ).start()



    def show_loading(self):

        try:

            home = self.parent.parent.parent.parent


            home.ids.devices_section.set_loading(
                "در حال جستجوی شبکه..."
            )


        except Exception as e:

            print("خطا در نمایش لودینگ:")

            print(e)



    def _scan_thread(self):


        from services.network_scanner import NetworkScanner


        scanner = NetworkScanner()


        devices = scanner.scan()



        print("دستگاه های پیدا شده:")


        for device in devices:

            print(
                device["name"],
                device["ip"]
            )



        Clock.schedule_once(

            lambda dt:
            self.update_devices(devices)

        )




    def update_devices(self, devices):


        try:


            home = self.parent.parent.parent.parent


            home.ids.devices_section.show_devices(
                devices
            )


        except Exception as e:


            print("خطا در نمایش دستگاه‌ها:")

            print(e)