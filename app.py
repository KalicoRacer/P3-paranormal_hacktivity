########################################
#              Imports
########################################
from flask import Flask, jsonify, render_template, send_from_directory
import pandas as pd

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

# Section 2 - API Endpoints
@app.route('/resources') # 127.0.0.1:5000/resources
def resources():
  
  
########################################
#           Initialization
########################################
if __name__ == "__main__":
  app.run(debug=True)