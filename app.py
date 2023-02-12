from flask import Flask, render_template
from flask_cors import CORS
from flask_restful import Api

from controllers.DogEmotionClassifier import DogEmotionClassifier
from controllers.DogVsNotDog import DogVsNotDog

DEBUG = True

app = Flask(__name__)
CORS(app)

api = Api(app)

# REST API endpoints
api.add_resource(DogEmotionClassifier, "/ai/classification/dogemotion") # Classify dog emotion
api.add_resource(DogVsNotDog, "/ai/classification/dogvsnotdog")  # Classify if picture has a dog

# Template routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/help")
def help():
    return render_template("help.html")


if __name__ == '__main__':
    app.run(debug=DEBUG)