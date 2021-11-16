# ************************************************************************
# Ashlin Darius Govindasamy - ADGSTUDIOS 2021
# All rights reserved.
# Heroku Templete to Get Started
# ************************************************************************

# Import Modules
from flask import Flask, render_template, jsonify, request, abort

# App Config
app = Flask(__name__, template_folder='pages')

# Our Website Routes
@app.route('/')
def home():
    return render_template('index.html')


# Initialization of applications and run
if __name__ == "__main__":
    app.run('localhost', debug=False)
