########################################
#              Imports
########################################

import socket
print(socket.gethostbyname(socket.getfqdn(socket.gethostname())))

from flask import Flask
app = Flask(__name__)

########################################
#            Configuration
########################################

# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')
app.config["CACHE_TYPE"] = "null"

# Database Config (SQL Alchemy / PyMongo / other)

########################################
#               Routes
########################################

# Section 1 - HTML/Web Pages
@app.route("/") # 127.0.0.1:5000/
def home():
    print('test')
    return render_template("index.html")


@app.route("/analyze")
def analyze():



# Section 2 - API Endpoints
@app.route('/resources') # 127.0.0.1:5000/resources
def resources():
  
  
########################################
#           Initialization
########################################

import threading
threading.Thread(target=app.run, kwargs={'host':'0.0.0.0','port':80}).start()

if __name__ == "__main__":
  app.run(debug=True)