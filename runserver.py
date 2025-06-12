from waitress import serve
from p_telefonia_tripoloni.wsgi import application  

if __name__ == '__main__':
    print("Iniciando servidor com Waitress em http://0.0.0.0:8000 ...")
    serve(application, host='0.0.0.0', port=8000, _quiet=False, threads=8)