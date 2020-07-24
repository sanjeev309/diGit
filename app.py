import os
import base64
import io

from flask import Flask, request, send_from_directory, jsonify
from flask_cors import CORS

from digit import digit

# Create Flask application
app = Flask(__name__)
CORS(app)

# Initialise Query Object in global scope
d = digit()


# # The route where POST queries are received
# @app.route('/', methods=['POST'])
# def home():
#

# To show static text if the server url is opened in a browser
@app.route('/', methods=['GET'])
def index():
    return '''<h1>diGit API Server by Sanjeev Tripathi  : <a href="https://www.linkedin.com/in/sanjeev309/" target="_blank">[LinkedIn]</a></h1>
        </br><p>Server is running</p>'''


# Helps get rid of favicon 404 in request on heroku
@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static',
                               'favicon.png', mimetype='image/png')


@app.route('/digit', methods=['GET'])
def number_api():
    if 'n' not in request.args:
        return {"error": "No number in request"}

    number = request.args['n']

    image = d.get_digit(number)

    rawBytes = io.BytesIO()

    image.save(rawBytes, "JPEG")
    rawBytes.seek(0)

    img_base64 = base64.b64encode(rawBytes.read())

    return jsonify({'image': str(img_base64)})


@app.route('/spacer', methods=['GET'])
def spacer_api():
    spacer = d.get_spacer()
    rawBytes = io.BytesIO()

    spacer.save(rawBytes, "JPEG")
    rawBytes.seek(0)

    img_base64 = base64.b64encode(rawBytes.read())

    return jsonify({'image': str(img_base64)})


# RUN FLASK APPLICATION
if __name__ == '__main__':
    # RUNNING FLASK APP
    app.run(debug=False, host='0.0.0.0', port=5000)
