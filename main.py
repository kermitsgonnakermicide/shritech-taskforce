import PIL.Image
import flask
from flask import *
import random
import os
from flask_docs import *
from flask import *
from PIL import *
app = Flask(__name__)

app.config["API_DOC_URL_PREFIX"] = "/docs"
ApiDoc(
    app,
    title="Dish Server",
    version="1.0.0",
    description="A dish server",
)
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
@app.route('/specific', methods=['POST'])
def test():
    v=request.args

    if v["course"] == "dinner":
        t=os.listdir(os.path.join(DISHES_DIR, "/dinner"))
        print(t)
        return flask.send_file(random.choice(t))
    return "200"
def add_dish():

    for file in request.files:
        print(str(file))
    return "done"

if __name__ == '__main__':
    app.run(debug=True)
