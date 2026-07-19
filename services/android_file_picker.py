from kivy.utils import platform


class AndroidFilePicker:


    def open_picker(self):

        if platform != "android":
            print("File picker فقط روی اندروید فعال است")
            return


        from jnius import autoclass


        Intent = autoclass(
            "android.content.Intent"
        )

        PythonActivity = autoclass(
            "org.kivy.android.PythonActivity"
        )


        intent = Intent(
            Intent.ACTION_OPEN_DOCUMENT
        )

        intent.addCategory(
            Intent.CATEGORY_OPENABLE
        )

        intent.setType(
            "*/*"
        )


        PythonActivity.mActivity.startActivityForResult(
            intent,
            1001
        )