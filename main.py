import PIL.Image
import flask
from flask import Flask, jsonify, send_file, request
import random
import os
from flask_docs import *
from flask import *
from PIL import *
app = Flask(__name__)
ApiDoc(
    app,
    title="Dish Server",
    version="1.0.0",
    description="A dish return"
                "",
)
app.config["API_DOC_URL_PREFIX"] = "*"
# Assume we have a directory called 'dishes' with images of dishes
DISHES_DIR = 'dishes'
app.config['UPLOAD_FOLDER'] = DISHES_DIR
@app.route("/*")
def none():
    return "This area does not exist"
@app.route('/random-dish', methods=['GET'])
def random_dish():
    try:
        dir = os.listdir(DISHES_DIR)
        print(random.choice(dir))

        return flask.send_file(os.path.join(DISHES_DIR, random.choice(dir)))

    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500
@app.route('/add-dish', methods=['POST'])

def add_dish():
    for file in request.files:
        print(str(file))
    return "done"

if __name__ == '__main__':
    app.run(debug=True)
