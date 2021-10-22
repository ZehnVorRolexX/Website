from website import create_app
from flask import Flask

app = create_app()

if __name__ == '__main__':
    #before commiting, comment the app.run(debug = True) and uncomment the line above
    app.run(debug = True, host = "0.0.0.0", ssl_context = ('/home/Basti/Website/Website/website/certs/haarstudio-mb.de_ssl_certificate.cer', '/home/Basti/Website/Website/website/certs/haarstudio-mb.de_private_key.key'), port='443')
    #app.run(debug = True)