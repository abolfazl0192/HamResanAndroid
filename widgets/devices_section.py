from kivymd.uix.card import MDCard
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel

from kivy.metrics import dp



class DevicesSection(MDCard):


    def set_loading(self, text):

        try:

            self.ids.loading_text.fa_text = text

        except Exception as e:

            print("خطا در تغییر متن وضعیت:")

            print(e)




    def device_clicked(self, device):

        print("دستگاه انتخاب شد:")

        print(
            device["name"],
            device["ip"]
        )

        # بعداً اینجا اتصال یا ارسال فایل قرار می‌گیرد




    def show_devices(self, devices):


        self.set_loading(
            "دستگاه‌های پیدا شده"
        )


        self.ids.devices_list.clear_widgets()



        for device in devices:



            card = MDCard(

                size_hint_y=None,

                height=dp(45),

                radius=[dp(10)],

                elevation=1,

                ripple_behavior=True

            )



            item = MDBoxLayout(

                orientation="horizontal",

                spacing=dp(10),

                padding=[dp(10),0]

            )



            name = MDLabel(

                text=device.get(
                    "name",
                    "Unknown"
                ),

                halign="right",

                font_name="Vazir"

            )



            ip = MDLabel(

                text=device.get(
                    "ip",
                    ""
                ),

                halign="left",

                font_name="Vazir"

            )



            item.add_widget(name)

            item.add_widget(ip)



            card.add_widget(item)



            # کلیک روی کارت

            card.bind(

                on_release=lambda x, d=device:
                self.device_clicked(d)

            )



            self.ids.devices_list.add_widget(card)