from website import create_app
from flask import Flask

app = create_app()

if __name__ == '__main__':
    app.run(debug = True, host = "0.0.0.0", ssl_context = ('D:\\Dev\\Website\\website\\certs\\cert.pem', 'D:\\Dev\\Website\\website\\certs\\key.pem'))