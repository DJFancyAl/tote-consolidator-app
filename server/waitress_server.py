from waitress import serve
from app import app

port=5000

if __name__ == '__main__':
    print(f'Running on port {port}...')
    serve(app, host="0.0.0.0", port=port)
