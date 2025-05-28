import os
import webview
import threading

def run_django_server():
    os.system('python manage.py runserver 8000')
    
def open_webview():
    webview.create_window('Telefonia Tripoloni', 'http://localhost:8000', maximized=True)
    webview.start()
    
if __name__ == '__main__':
    django_thread = threading.Thread(target=run_django_server)
    django_thread.daemon = True
    django_thread.start()
    
    open_webview()