import sys
import os
import ctypes
import threading
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from cefpython3 import cefpython as cef
from kivy.clock import Clock
Clock.schedule_once(lambda dt: threading.Thread(...).start())


class CefBrowser(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_cef()

    def start_cef(self):
        def _start_cef():
            # 设置CEF环境变量
            os.environ['CEF_PYTHON'] = "1"
            settings = {
                "windowless_rendering_enabled": True,
                "context_menu": {
                    "enabled": False
                }
            }
            cef.Initialize(settings=settings)

            window_info = cef.WindowInfo()
            window_info.SetAsChild(
                self.get_window_handle(),
                [0, 0, self.width, self.height]
            )
            cef.CreateBrowserSync(
                window_info,
                url="https://www.openstreetmap.org"
            )
            cef.MessageLoop()

        threading.Thread(target=_start_cef, daemon=True).start()

    def get_window_handle(self):
        if sys.platform == 'win32':
            # 解决Windows高DPI问题
            ctypes.windll.user32.SetProcessDPIAware()
            return ctypes.windll.user32.GetParent(self.get_system_window())
        return 0


class MyApp(App):
    def build(self):
        return CefBrowser()


if __name__ == '__main__':
    # 确保Kivy配置正确
    os.environ['KIVY_NO_CONSOLELOG'] = '1'
    os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
    MyApp().run()