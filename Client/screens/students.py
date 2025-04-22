
from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from api_client import *

class StudentManagementScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_students()

    def load_students(self):
        self.ids.student_list.clear_widgets()
        students = get_students()
        for student in students:
            item = BoxLayout(size_hint_y=None, height=40)
            item.add_widget(Label(text=f"{student['name']} ({student['status']})"))
            self.ids.student_list.add_widget(item)

    def show_add_dialog(self):
        content = BoxLayout(orientation='vertical')
        # 添加输入字段...
        popup = Popup(title='添加学生', content=content)
        popup.open()
