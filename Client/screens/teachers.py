
# 在frontend/screens/teachers.py中添加
from kivy.uix.webview import WebView

def show_location(self, coords):
    map_html = f"""
    <!DOCTYPE html>
    <html>
    <body>
        <div id="map" style="width:100%; height:100%"></div>
        <script>
            var map = L.map('map').setView([{coords[1]}, {coords[0]}], 16);
            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);
            L.marker([{coords[1]}, {coords[0]}]).addTo(map);
        </script>
    </body>
    </html>
    """
    webview = WebView()
    webview.load_html(map_html)
    popup = Popup(title='办公室位置', content=webview)
    popup.open()
