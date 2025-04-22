
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from screens.students import StudentManagementScreen
from screens.teachers import TeacherManagementScreen

Builder.load_file('main.kv')

class MainWindow(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(StudentManagementScreen(name='students'))
        self.add_widget(TeacherManagementScreen(name='teachers'))

class StudentManagementApp(App):
    def build(self):
        return MainWindow()

if __name__ == '__main__':
    StudentManagementApp().run()
