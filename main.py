import PIL.Image
import flask
from flask import *
import random
import os
from flask_docs import *
from flask import *
from PIL import *
app = Flask(__name__)

app.config["API_DOC_MEMBER"] = ["api"]

app.config["API_DOC_URL_PREFIX"] = "/docs"
app.config["API_DOC_METHODS_LIST"] = ["GET", "POST"]
ApiDoc(
    app,
    title="Dish Server",
    version="1.0.0",
    description="A dish server",
)

api = flask.Blueprint("api", __name__)

# Assume we have a directory called 'dishes' with images of dishes
DISHES_DIR = 'segregated'
app.config['UPLOAD_FOLDER'] = DISHES_DIR
@app.route("/api/*")
def none():
    """
    Nothing to see here!
    """
    return "This area does not exist"
@api.route('/random-dish', methods=['GET'])
def random_dish():
    """
    Returns a random dish
    """
    try:
        dir = os.listdir("all")
        print(random.choice(dir))

        return flask.send_file(os.path.join(DISHES_DIR, random.choice(dir)))

    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500
@api.route('/dish-course', methods=['GET'])
def dishcourse():
    """
    Returns a specific course
    """

    try:
        v=request.headers["course"]
        print(v)
        if v == "dinner":
            t=os.listdir("segregated/dinner")
            print(t)
            z= "segregated/dinner/" + random.choice(t)
            return flask.send_file(z)
        if v == "lunch":
            t = os.listdir("segregated/lunch")
            print(t)
            return flask.send_file("segregated/lunch/" +random.choice(t))
        if v == "breakfast":
            t = os.listdir("segregated/breakfast")
            print(t)
            return flask.send_file("segregated/breakfast/" + random.choice(t))
        else:
            return "401"
    except Exception as e:
        return jsonify({"error": str(e)}), 500
@api.route('/all', methods=['GET'])
def returnAll():
    """
    Returns ALL available dishes
    """
    try:
        noExtension = []
        for i in os.listdir('all'):
            temp = i.removesuffix(".jpg")
            noExtension.append(temp)
        return jsonify(noExtension)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.errorhandler(404)
def not_found(e):
    return jsonify("Sorry, the given endpoint was not found. Please check your spelling and the documentation and try again")

app.register_blueprint(api, url_prefix="/api")

if __name__ == '__main__':
    app.run(debug=True)