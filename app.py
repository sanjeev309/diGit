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
    return '''<h2>diGit API Server by Sanjeev  </h2>
    <h4><a href="https://www.linkedin.com/in/sanjeev309/" target="_blank">[LinkedIn]</a> <a href="https://www.github.com/sanjeev309/diGit" target="_blank">[Github]</a></h4>
        <p>Server is running</p>
        <h3> How to use: </h3>
        
        <p> diGit return an image with number when a number is passed to the API</p>
        <b>For example: </b>
        </br></br>
        Digits: <a href="https://digit-server.herokuapp.com/digit?n=420" target="_blank"> Send request for 420</a> : gives <img src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/wAALCAAFAA8BAREA/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/9oACAEBAAA/AMPwVcS+Kr7wTE6x2c63Go2izW0k0ZYxafbJG7FZFbOEQEIyAgY4ySbmr2V4fhj8RLye/wA+R4gu4Z4YkKRzSPc2ZEm0scbfLYAHcQJDz1z/AP/Z" width=60px height=20px alt="digit test">
        </br>
        Blank space: use <a href="https://digit-server.herokuapp.com/spacer" target="_blank"> spacer</a> : gives <img src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/wAALCAAFAAIBAREA/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/9oACAEBAAA/APn+v//Z" width=8px height=20px alt='spacer_test'>
        </br></br>
        
        All responses are base64 encoded and can be directly used for rendering.
        '''


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

    image = d.digitize(number)

    rawBytes = io.BytesIO()

    image.save(rawBytes, "JPEG")
    rawBytes.seek(0)

    img_base64 = base64.b64encode(rawBytes.read())

    print(img_base64)
    return "data:image/jpeg;base64," + img_base64.decode('utf-8')


@app.route('/spacer', methods=['GET'])
def spacer_api():
    spacer = d.get_spacer()
    rawBytes = io.BytesIO()

    spacer.save(rawBytes, "JPEG")
    rawBytes.seek(0)

    img_base64 = base64.b64encode(rawBytes.read())

    return "data:image/jpeg;base64," + img_base64.decode('utf-8')


# RUN FLASK APPLICATION
if __name__ == '__main__':
    # RUNNING FLASK APP
    app.run(debug=False, host='0.0.0.0', port=5000)
